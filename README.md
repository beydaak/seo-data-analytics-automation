#  E-Commerce SEO Automation & Marketing Analytics Pipeline

This repository contains Python-based data analytics and automation scripts designed to optimize e-commerce organic growth, implement Next-Gen SEO strategies, and uncover high-potential search intent data. 

The methodologies here were successfully implemented to achieve a **1400% increase in AI/AIO Search Visibility (from 0 to 14 score on Semrush)** for a live e-commerce brand.

---

##  Key Features

* **Hot Opportunities Finder:** Automatically filters and clusters keywords ranking between positions `10.1` and `10.5` (the edge of Page 1) using `Pandas` and `NumPy` to maximize ROI.
* **Data Masking & Security:** All proprietary brand data, API credentials, and performance metrics have been completely masked and replaced with anonymized datasets for privacy compliance.
* **Semantic SEO Preparation:** Automation of keyword grouping to feed custom schema markup layouts and E-E-A-T oriented content structures.

---

## 📊 Veri Görselleştirme & İş Zekası (Looker Studio)

Projenin otomasyon çıktısı, daha rahat stratejik kararlar alabilmek ve üst yönetime sunum hazırlayabilmek adına **Google Looker Studio** paneline entegre edilmiştir.

###  Dashboard Yapısı ve Analiz Kriterleri:
* **Isı Haritası (Heat Map) Entegrasyonu:** Google arama sonuçlarında 2. sayfanın en başında (`10.1` - `10.5`) sıkışmış ve acil optimizasyon bekleyen tüm yüksek potansiyelli kelimeler, panel üzerinde özel bir koşullu biçimlendirme ile ısı haritası şeklinde izole edilmiştir.
* **Gelişmiş Metrik Yönetimi (CTR Hesaplama):** Panel içerisinde özel bir hesaplanan alan (Calculated Field) oluşturularak `Tıklama / Gösterim` formülüyle anlık **CTR (%)** takibi entegre edilmiştir. Böylece pazar hacmi yüksek ama tıklama oranı düşük sayfalar anında tespit edilir.
* **Veri Tipi Senkronizasyonu (Data Integrity):** Veri entegrasyonu (Data Pipeline) sürecinde sıklıkla karşılaşılan, ondalıklı pozisyon verilerinin otomatik olarak "Tarih" formatına dönüştürülerek bozulması krizi (Data Type Mismatch), kaynak düzeyinde çözülerek %100 veri tutarlılığı sağlanmıştır.
* **Veri Maskeleme & Gizlilik:** Projede kullanılan tüm e-ticaret marka verileri ve hassas performans metrikleri, veri güvenliği ve gizlilik kurallarına uygun olarak tamamen maskelenmiştir (Data Masking).

---

##  Tech Stack & Libraries

* **Language:** Python 3.x
* **Data Analysis:** `pandas`, `numpy`
* **Data Fetching / Scraping:** `requests`, `beautifulsoup4`
* **Business Intelligence:** Integrated seamlessly with Google Looker Studio for executive reporting.

---

##  Repository Structure

```text
├── data/
│   └── sample_keywords.csv       # Anonymized mock dataset for demonstration
├── scripts/
│   └── opportunity_analyzer.py   # Main Python automation script
├── .gitignore                    # Prevents local credentials (.env) from being pushed
└── README.md                     # Project documentation
