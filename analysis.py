import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

baslangic_tarih = "2007-10-01"
bitis_tarih = "2009-03-31"

varlik_kurnaz = ["GARAN.IS", "EREGL.IS", "THYAO.IS"]
adlar_kurnaz = ["GARANTI BANK", "EREGLI", "TURK HAVA YOLLARI"]
w_kurnaz = np.array([0.40, 0.35, 0.25])

varlik_trader = ["XU100.IS", "CCOLA.IS", "TRY=X"]
adlar_trader = ["BIST 100", "COCA COLA", "USD/TRY Kuru"]
w_trader = np.array([0.40, 0.35, 0.25])

def veri_cekme(varlik, baslangic_tarih, bitis_tarih):
    # yfinanceden veri ceker
    data = yf.download(varlik, start=baslangic_tarih, end=bitis_tarih, progress=False)["Close"]
    data = data.dropna()
    cikti = data.pct_change().dropna()
    return cikti

def metrik_hesapla(cikti, agirlik):
    # 1. Kovaryans Matrisi
    kov_matrisi = cikti.cov()
    
    # 2. Korelasyon Matrisi
    korelasyon_matrisi = cikti.corr()

    # Finansal analiz standartlarindan dolayi yillik kovaryans
    yillik_kov_matrisi = kov_matrisi * 252

    # Portfoy varyansi
    carpim1 = np.dot(agirlik.T, yillik_kov_matrisi)
    portfoy_varyans = np.dot(carpim1, agirlik)
    
    # Fonksiyon artık korelasyon matrisini de döndürüyor
    return yillik_kov_matrisi, portfoy_varyans, korelasyon_matrisi

# --- KURNAZ HESAPLAMA ---
cikti_kurnaz = veri_cekme(varlik_kurnaz, baslangic_tarih, bitis_tarih)

kov_matrisi_kurnaz, varyans_kurnaz, kor_matrisi_kurnaz = metrik_hesapla(cikti_kurnaz, w_kurnaz)
ssapma_kurnaz = np.sqrt(varyans_kurnaz)

print('--- Kurnazın Portföyü ---')
print(f"Portföy Varyansı (sigma kare): {varyans_kurnaz:.4f}")
print(f'Standart Sapma: {ssapma_kurnaz:.4f}\n')

print('Kovaryans Matrisi (Yıllık):')
print(kov_matrisi_kurnaz)
print('\nKorelasyon Matrisi (İlişki Tablosu):')
print(kor_matrisi_kurnaz)
print('\n' + '='*30 + '\n')

# --- TRADER HESAPLAMA ---
cikti_trader = veri_cekme(varlik_trader, baslangic_tarih, bitis_tarih)
kov_matrisi_trader, varyans_trader, kor_matrisi_trader = metrik_hesapla(cikti_trader, w_trader)
ssapma_trader = np.sqrt(varyans_trader)

print('--- Traderin Portföyü ---')
print(f"Portföy Varyansı (sigma kare): {varyans_trader:.4f}")
print(f'Standart Sapma: {ssapma_trader:.4f}\n')

print('Kovaryans Matrisi (Yıllık):')
print(kov_matrisi_trader)
print('\nKorelasyon Matrisi (İlişki Tablosu):')
print(kor_matrisi_trader)
# Butun varliklari ekleme
varlik_butun = varlik_kurnaz + varlik_trader
data = yf.download(varlik_butun, start=baslangic_tarih, end=bitis_tarih)['Close']
data = data.dropna() # Eksik verileri temizle

# Kumulatif getiri hesaplama
# Gunluk getiri hesaplama
gunluk_getiri = data.pct_change()
gunluk_getiri.iloc[0] = 0 # Ilk gun getiri nan olmamasi icin

# Oransal iliskiler kurabilmek icin baslangic 1 dir
kumulatif_getiri = (1 + gunluk_getiri).cumprod()

# Grafik olusturma
fig, axes = plt.subplots(1, 2, figsize=(18, 7)) # İki alt grafik oluştur

# Kurnaz'in Portfoy Varliklari
ax1 = axes[0]
for i, varlik in enumerate(varlik_kurnaz):
    ax1.plot(kumulatif_getiri[varlik], label=adlar_kurnaz[i])

ax1.axhline(1, color='black')
ax1.set_title(f"Kurnaz'ın Varlıkları (Yüksek Kovaryans)\n{baslangic_tarih} - {bitis_tarih}")
ax1.set_xlabel("Tarih")
ax1.set_ylabel("Kümülatif Getiri")
ax1.legend()
ax1.tick_params(axis='x')

# Trader'ın Portföy Varkliklari
ax2 = axes[1]
for i, varlik in enumerate(varlik_trader):
    ax2.plot(kumulatif_getiri[varlik], label=adlar_trader[i])

ax2.axhline(1, color='black') 
ax2.set_title(f"Trader'ın Varlıkları (Düşük/Negatif Kovaryans)\n{baslangic_tarih} - {bitis_tarih}")
ax2.set_xlabel("Tarih")
ax2.set_ylabel("Kümülatif Getiri")
ax2.legend()
ax2.tick_params(axis='x')

plt.show()
