# Portfoy-Kovaryans-Risk-Analizi

Bu proje, Python kullanarak iki farklı yatırım stratejisinin ("Kurnaz" ve "Trader") risk ve getiri performanslarını analiz eder. Analiz, 2008 Küresel Finans Krizini (Ekim 2007 - Mart 2009) kapsayan yüksek volatilite döneminde gerçekleştirilmiştir.

Proje, modern portföy teorisi prensiplerini kullanarak varlıklar arasındaki **Korelasyon** ve **Kovaryans** matrislerini hesaplar ve görselleştirir.

## 🚀 Özellikler

* **Otomatik Veri Çekme:** `yfinance` API kullanılarak Yahoo Finance üzerinden hisse senedi ve kur verileri çekilir.
* **Matris İşlemleri:** Portföy varyansı ve standart sapması, lineer cebir yöntemleri (dot product) ile hesaplanır.
* **Risk Analizi:**
    * Yıllıklandırılmış Kovaryans Matrisi
    * Portföy Volatilitesi (Standart Sapma)
* **Görselleştirme:**
    * `Matplotlib` ile Kümülatif Getiri karşılaştırması.
    * `Seaborn` ile portföy kovaryanslarının ısı grafiğikleri.

## 📊 Portföyler

Analiz edilen iki farklı strateji şunlardır:

1.  **Kurnaz Portföyü (Yüksek Risk/Yüksek Korelasyon):** Tamamen BIST (İstanbul Borsası) varlıklarına dayalıdır (Garanti, Ereğli, THY). Kriz dönemlerinde varlıkların birlikte hareket etme eğilimini (korelasyon artışı) gösterir.
2.  **Trader Portföyü (Hedge/Çeşitlendirilmiş):** BIST 100 endeksi ile birlikte defansif bir varlık olan **USD/TRY** kurunu içerir. Negatif veya düşük korelasyonlu varlıkların portföy riskini nasıl düşürdüğünü simüle eder.

## 🧮 Matematiksel Altyapı

Portföy varyansı ($\sigma_p^2$), ağırlık vektörü ($w$) ve kovaryans matrisi ($\Sigma$) kullanılarak şu formülle hesaplanmıştır:

$$\sigma_p^2 = w^T \cdot \Sigma \cdot w$$

## 🛠️ Kurulum ve Kullanım

Projeyi yerel ortamınızda çalıştırmak için:

1.  Repoyu klonlayın:
    ```bash
    git clone [https://github.com/korukmeyen44/Portfoy-Kovaryans-Risk-Analizi.git](https://github.com/korukmeyen44/Portfoy-Kovaryans-Risk-Analizi.git)
    cd Portfoy-Kovaryans-Risk-Analizi
    ```

2.  Gereksinimleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3.  Analizi çalıştırın:
    ```bash
    python analysis.py
    ```

## 📈 Çıktılar

    ```
    --- Kurnazın Portföyü ---
      Portföy Varyansı (sigma kare): 0.2415
      Standart Sapma: 0.4915
      
      Kovaryans Matrisi (Yıllık):
      Ticker    EREGL.IS  GARAN.IS  THYAO.IS
      Ticker                                
      EREGL.IS  0.363108  0.216462  0.149580
      GARAN.IS  0.216462  0.345996  0.187808
      THYAO.IS  0.149580  0.187808  0.282703
      
      Korelasyon Matrisi (İlişki Tablosu):
      Ticker    EREGL.IS  GARAN.IS  THYAO.IS
      Ticker                                
      EREGL.IS  1.000000  0.610701  0.466865
      GARAN.IS  0.610701  1.000000  0.600501
      THYAO.IS  0.466865  0.600501  1.000000
      
      ==============================
      
      --- Traderin Portföyü ---
      Portföy Varyansı (sigma kare): 0.0557
      Standart Sapma: 0.2359
      
      Kovaryans Matrisi (Yıllık):
      Ticker    CCOLA.IS     TRY=X  XU100.IS
      Ticker                                
      CCOLA.IS  0.229856 -0.016350  0.078354
      TRY=X    -0.016350  0.058531 -0.052909
      XU100.IS  0.078354 -0.052909  0.158064
      
      Korelasyon Matrisi (İlişki Tablosu):
      Ticker    CCOLA.IS     TRY=X  XU100.IS
      Ticker                                
      CCOLA.IS  1.000000 -0.140963  0.411071
      TRY=X    -0.140963  1.000000 -0.550067
      XU100.IS  0.411071 -0.550067  1.000000
    ```
Belirtilen dönemde trader ve kurnaz kişisinin kümülatif hisse değerleri:<img width="1466" height="645" alt="image" src="https://github.com/user-attachments/assets/73cc7589-e63d-4692-b757-f5fc02a1ef3d" />
Porföylerin korelasyon matrislerinin ısı grafikleri:<img width="1566" height="590" alt="image" src="https://github.com/user-attachments/assets/05c02c6f-b905-4e41-a1ec-d984748babb9" />
 />


## 📝 Lisans

Bu proje [MIT](LICENSE) lisansı altında lisanslanmıştır.
