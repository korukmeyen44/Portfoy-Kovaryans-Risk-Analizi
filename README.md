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
    * * `Seaborn` ile portföy kovaryanslarının ısı grafiğikleri.

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

Belirtilen dönemde trader ve kurnaz kişisinin kümülatif hisse değerleri:<img width="1466" height="645" alt="image" src="https://github.com/user-attachments/assets/73cc7589-e63d-4692-b757-f5fc02a1ef3d" />
Porföylerin korelasyon matrislerinin ısı grafikleri:<img width="1556" height="590" alt="image" src="https://github.com/user-attachments/assets/4592136b-3209-4d84-b849-4adb2f8285e8" />


## 📝 Lisans

Bu proje [MIT](LICENSE) lisansı altında lisanslanmıştır.
