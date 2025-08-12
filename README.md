# Peramalan IHSG dengan Algoritma Genetika dan Jaringan Saraf Tiruan

Proyek penelitian ini bertujuan untuk melakukan peramalan harga penutupan Indeks Harga Saham Gabungan (IHSG) menggunakan kombinasi Algoritma Genetika (GA) dan Jaringan Saraf Tiruan (ANN). Penelitian ini membandingkan performa dari tiga model: **GANN** (Genetic Algorithm Neural Network), **GADAM** (Genetic Algorithm with Adam optimizer), dan **ADAM** (Adam optimizer standar).

## 🎯 Tujuan Penelitian

- Mengembangkan model peramalan IHSG yang akurat menggunakan kombinasi GA dan ANN
- Membandingkan performa tiga pendekatan optimasi: GANN, GADAM, dan ADAM
- Menemukan konfigurasi parameter terbaik untuk setiap model
- Menganalisis stabilitas dan konsistensi model dalam berbagai kondisi pasar

## 🔬 Metodologi

Eksperimen ini dijalankan dengan **12 kombinasi parameter** yang berbeda untuk menemukan konfigurasi terbaik:

- **Selection Methods**: Tournament Selection, Roulette Wheel Selection (RWS)
- **Population Sizes**: 50, 100
- **Generation Counts**: 50, 100, 150

## 📂 Struktur Proyek

```
penelitian/
├── data/                          # Data preprocessing dan hasil
│   ├── acf_pacf/                  # Analisis ACF dan PACF
│   ├── preprocessing/             # Data latih dan uji
│   └── raw/                       # Data mentah
├── experiments/                   # Hasil eksperimen
│   ├── 1. tournament_pop50_gen50/ # Eksperimen 1
│   ├── 2. tournament_pop50_gen100/# Eksperimen 2
│   └── ...                        # Eksperimen lainnya
├── docs/                          # Dokumentasi
├── img/                           # Gambar dan diagram
├── results/                       # Hasil analisis
├── GA-ANN-Final.ipynb            # Notebook utama
└── README.md                      # Dokumentasi proyek
```

## 🚀 Cara Menjalankan

> **⚡ Untuk instalasi cepat (5 menit), lihat [QUICKSTART.md](QUICKSTART.md)**  
> **📖 Untuk panduan instalasi lengkap, lihat [INSTALLATION.md](INSTALLATION.md)**

### Metode 1: Menggunakan pip (Direkomendasikan)

1. **Clone repository**:
   ```bash
   git clone https://github.com/trimetronika/GA-ANN.git
   cd GA-ANN
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan notebook**:
   ```bash
   jupyter notebook GA-ANN-Final.ipynb
   ```

### Metode 2: Menggunakan setup.py

```bash
git clone https://github.com/trimetronika/GA-ANN.git
cd GA-ANN
pip install -e .
```

### Metode 3: Menggunakan pyproject.toml (Modern)

```bash
git clone https://github.com/trimetronika/GA-ANN.git
cd GA-ANN
pip install -e .
```

### Development Setup

Untuk development dan testing:

```bash
pip install -e ".[dev]"
```

### Environment Setup

Disarankan menggunakan virtual environment:

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🔧 Troubleshooting

### Error: "Import setuptools could not be resolved"

Jika Anda mengalami error terkait `setuptools`, gunakan salah satu metode berikut:

#### Metode 1: Menggunakan Script Installer (Direkomendasikan)

**Windows:**
```bash
install.bat
```

**Linux/Mac:**
```bash
chmod +x install.sh
./install.sh
```

#### Metode 2: Manual Installation

```bash
# Upgrade pip dan install setuptools
python -m pip install --upgrade pip
python -m pip install setuptools>=65.0 wheel>=0.40.0

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

#### Metode 3: Menggunakan Python Script

```bash
python install_dependencies.py
```

### Error: "Module not found"

Jika ada module yang tidak ditemukan:

```bash
# Install semua dependencies termasuk yang optional
pip install -r requirements.txt
pip install -e ".[dev]"
```

### Error: "Permission denied"

**Windows:**
- Jalankan Command Prompt sebagai Administrator
- Atau gunakan: `pip install --user -r requirements.txt`

**Linux/Mac:**
```bash
sudo pip install -r requirements.txt
# Atau gunakan virtual environment
```
```

## 📊 Hasil Utama

- **Model Terbaik**: [Akan diisi setelah analisis selesai]
- **Akurasi**: [Akan diisi setelah analisis selesai]
- **Stabilitas**: [Akan diisi setelah analisis selesai]

## 📈 Metrik Evaluasi

- **RMSE** (Root Mean Square Error)
- **MAE** (Mean Absolute Error)
- **MAPE** (Mean Absolute Percentage Error)

## 👨‍💻 Penulis

**Tri Busono Wibowo** - Peneliti Machine Learning

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan buat pull request atau buka issue untuk diskusi.

## 📞 Kontak

- GitHub: [@trimetronika](https://github.com/trimetronika)
- Email: tribusonowibowo@gmail.com

---

**Catatan**: Proyek ini merupakan bagian dari tugas akhir penelitian. Semua hasil dan analisis akan diperbarui secara berkala.
