# Kampüs Yönetim Sistemi (Campus Management System)

Bu proje, **Gümüşhane Üniversitesi Yazılım Mühendisliği** programı kapsamında geliştirilmiş, kampüs sınırları içerisindeki öğrencileri, etkinlikleri ve kulüpleri yönetmek için tasarlanmış Python tabanlı bir uygulamadır.

## 🚀 Proje Özellikleri

Uygulama, modüler bir yapıda tasarlanmıştır ve şu işlevleri sunar:

* **Öğrenci Yönetimi (`students.py`):** Yeni öğrenci kayıtlarının oluşturulması ve mevcut bilgilerin yönetilmesi.
* **Etkinlik Takibi (`events.py`):** Kampüs etkinliklerinin planlanması ve katılımcı listelerinin takibi.
* **Veri Depolama (`data_store.py`):** Verilerin sistemde kalıcı olarak saklanması ve dosya yönetimi.
* **Raporlama Modülü (`reports.py`):** Sistemdeki verilerden anlamlı özetler ve raporlar çıkarılması.
* **Demo Akışı (`demo.py`):** Sistemin tüm özelliklerini test etmek için hazırlanan ana giriş noktası.

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Depoyu klonlayın:**
    ```bash
    git clone [https://github.com/evrimcolakoglu/Python-Kampus-Yonetim-Sistemi.git](https://github.com/evrimcolakoglu/Python-Kampus-Yonetim-Sistemi.git)
    ```
2.  **Proje dizinine gidin:**
    ```bash
    cd Python-Kampus-Yonetim-Sistemi
    ```
3.  **Uygulamayı başlatın:**
    ```bash
    python demo.py
    ```

## 📂 Dosya Yapısı

```text
.
├── data_store.py    # Veri yönetimi katmanı
├── demo.py          # Uygulama ana giriş ve test akışı
├── events.py        # Etkinlik ve kulüp mantığı
├── reports.py       # Raporlama ve analiz araçları
├── students.py      # Öğrenci veri sınıfları
└── .gitignore       # Gereksiz dosyaların (pycache vb.) engellenmesi
