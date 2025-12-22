import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. AYARLAR VE VARLIK TANIMLARI ---
baslangic_tarih = "2007-10-01"
bitis_tarih = "2009-03-31"

# Kurnaz Portföy Tanımları
varlik_kurnaz = ["GARAN.IS", "EREGL.IS", "THYAO.IS"]
adlar_kurnaz = ["GARANTI BANK", "EREGLI", "TURK HAVA YOLLARI"]
w_kurnaz = np.array([0.40, 0.35, 0.25])

# Trader Portföy Tanımları
varlik_trader = ["XU100.IS", "CCOLA.IS", "TRY=X"]
adlar_trader = ["BIST 100", "COCA COLA", "USD/TRY Kuru"]
w_trader = np.array([0.40, 0.35, 0.25])

# --- 2. FONKSİYONLAR ---
def veri_cekme(varlik, baslangic_tarih, bitis_tarih):
    """
    Belirtilen varlıklar için verileri çeker ve yüzdesel getiriyi hesaplar.
    """
    # progress=False ile gereksiz çıktı kirliliğini önledik
    data = yf.download(varlik, start=baslangic_tarih, end=bitis_tarih, progress=False)["Close"]
    data = data.dropna()
    cikti = data.pct_change().dropna()
    return cikti

def metrik_hesapla(cikti, agirlik):
    """
    Kovaryans, korelasyon ve portföy varyansını hesaplar.
    """
    # 1. Kovaryans Matrisi
    kov_matrisi = cikti.cov()
    
    # 2. Korelasyon Matrisi
    korelasyon_matrisi = cikti.corr()

    # Finansal analiz standartlarından dolayı yıllık kovaryans (252 işlem günü)
    yillik_kov_matrisi = kov_matrisi * 252

    # Portföy varyansı (Matris çarpımı: w^T * Cov * w)
    carpim1 = np.dot(agirlik.T, yillik_kov_matrisi)
    portfoy_varyans = np.dot(carpim1, agirlik)
    
    return yillik_kov_matrisi, portfoy_varyans, korelasyon_matrisi

# --- 3. HESAPLAMA VE RAPORLAMA ---

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

# --- 4. GÖRSELLEŞTİRME (GRAFİK) ---

# Bütün varlıkları birleştirme
varlik_butun = varlik_kurnaz + varlik_trader

# Grafik için veriyi tekrar çekiyoruz (Tüm varlıkların tarih hizalaması için)
data_grafik = yf.download(varlik_butun, start=baslangic_tarih, end=bitis_tarih, progress=False)['Close']
data_grafik = data_grafik.dropna() # Eksik verileri temizle

# Kümülatif getiri hesaplama
gunluk_getiri = data_grafik.pct_change()
gunluk_getiri.iloc[0] = 0 # İlk gün getiri NaN olmaması için 0 kabul edilir

# Oransal ilişkiler kurabilmek için başlangıç 1'dir (Normalize edilmiş fiyat)
kumulatif_getiri = (1 + gunluk_getiri).cumprod()

# Grafik oluşturma
fig, axes = plt.subplots(1, 2, figsize=(18, 7)) # İki alt grafik oluştur

# Kurnaz'ın Portföy Varlıkları
ax1 = axes[0]
for i, varlik in enumerate(varlik_kurnaz):
    ax1.plot(kumulatif_getiri.index, kumulatif_getiri[varlik], label=adlar_kurnaz[i])

ax1.axhline(1, color='black', linestyle='--') # Başlangıç çizgisi
ax1.set_title(f"Kurnaz'ın Varlıkları (Yüksek Kovaryans)\n{baslangic_tarih} - {bitis_tarih}")
ax1.set_xlabel("Tarih")
ax1.set_ylabel("Kümülatif Getiri (Başlangıç=1)")
ax1.legend()
ax1.grid(True, alpha=0.3)

# Trader'ın Portföy Varlıkları
ax2 = axes[1]
for i, varlik in enumerate(varlik_trader):
    ax2.plot(kumulatif_getiri.index, kumulatif_getiri[varlik], label=adlar_trader[i])

ax2.axhline(1, color='black', linestyle='--') 
ax2.set_title(f"Trader'ın Varlıkları (Düşük/Negatif Kovaryans)\n{baslangic_tarih} - {bitis_tarih}")
ax2.set_xlabel("Tarih")
ax2.set_ylabel("Kümülatif Getiri (Başlangıç=1)")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# --- 5. KORELASYON ISI HARİTASI (HEATMAP) ---

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Kurnaz Portföyü Heatmap
sns.heatmap(kor_matrisi_kurnaz, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
            fmt=".2f", linewidths=.5, ax=axes[0])

axes[0].set_title("Kurnaz Portföyü Korelasyon Matrisi\n(Benzer Varlıklar)", fontsize=12)
axes[0].set_xticklabels(adlar_kurnaz, rotation=45)
axes[0].set_yticklabels(adlar_kurnaz, rotation=0)

# Trader Portföyü Heatmap
sns.heatmap(kor_matrisi_trader, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
            fmt=".2f", linewidths=.5, ax=axes[1])

axes[1].set_title("Trader Portföyü Korelasyon Matrisi\n(Ters/Düşük İlişkili Varlıklar)", fontsize=12)
axes[1].set_xticklabels(adlar_trader, rotation=45)
axes[1].set_yticklabels(adlar_trader, rotation=0)

plt.tight_layout()
plt.show()
