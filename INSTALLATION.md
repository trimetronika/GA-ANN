# 📦 Panduan Instalasi GA-ANN IHSG

## 🎯 Overview

Dokumen ini berisi panduan lengkap untuk menginstal dan menjalankan proyek **Peramalan IHSG dengan Algoritma Genetika dan Jaringan Saraf Tiruan**.

## 🔧 Prerequisites

### 1. Python Installation

**Minimum Requirements:**
- Python 3.8 atau lebih tinggi
- pip (biasanya terinstal dengan Python)

**Cara Install Python:**

#### Windows:
1. Download Python dari [python.org](https://www.python.org/downloads/)
2. **PENTING**: Centang "Add Python to PATH" saat instalasi
3. Restart Command Prompt setelah instalasi

#### Linux/Mac:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# macOS (dengan Homebrew)
brew install python3
```

### 2. Git (Optional)
```bash
# Windows: Download dari git-scm.com
# Linux:
sudo apt install git
# macOS:
brew install git
```

## 🚀 Instalasi Cepat

### Metode 1: Script Otomatis (Direkomendasikan)

#### Windows:
```bash
# Double-click file install.bat
# Atau jalankan di Command Prompt:
install.bat
```

#### Linux/Mac:
```bash
chmod +x install.sh
./install.sh
```

### Metode 2: Manual Installation

```bash
# 1. Clone repository (jika belum)
git clone https://github.com/trimetronika/GA-ANN.git
cd GA-ANN

# 2. Upgrade pip dan install setuptools
python -m pip install --upgrade pip
python -m pip install setuptools>=65.0 wheel>=0.40.0

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install package dalam mode development
pip install -e .
```

## 🔍 Troubleshooting

### Error: "Python was not found"

**Solusi:**
1. Pastikan Python terinstal dengan benar
2. Pastikan "Add Python to PATH" dicentang saat instalasi
3. Restart Command Prompt/Terminal
4. Coba command: `python --version` atau `python3 --version`

### Error: "Import setuptools could not be resolved"

**Solusi:**
```bash
# Install setuptools secara manual
pip install setuptools>=65.0 wheel>=0.40.0
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

### Error: "Module not found"

**Solusi:**
```bash
# Install semua dependencies termasuk yang optional
pip install -r requirements.txt
pip install -e ".[dev]"
```

## 🐍 Virtual Environment (Direkomendasikan)

### Membuat Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Install dalam Virtual Environment

```bash
# Setelah virtual environment aktif
pip install -r requirements.txt
pip install -e .
```

## 📊 Verifikasi Instalasi

### Test Import Dependencies

```python
# Jalankan di Python console
import pandas
import numpy
import tensorflow
import keras
import deap
import matplotlib
import seaborn
import statsmodels
import scipy
import jupyter

print("✅ Semua dependencies berhasil diimport!")
```

### Test Setup

```bash
# Test apakah package dapat diimport
python -c "import ga_ann_ihsg; print('✅ Package berhasil diimport!')"
```

## 🎮 Menjalankan Proyek

### 1. Jupyter Notebook

```bash
# Start Jupyter
jupyter notebook

# Atau langsung buka file
jupyter notebook GA-ANN-Final.ipynb
```

### 2. Development Mode

```bash
# Install dalam mode development
pip install -e ".[dev]"

# Run tests (jika ada)
pytest
```

## 📁 Struktur File Setelah Instalasi

```
penelitian/
├── venv/                          # Virtual environment (jika dibuat)
├── data/                          # Data preprocessing
├── experiments/                   # Hasil eksperimen
├── GA-ANN-Final.ipynb            # Notebook utama
├── requirements.txt               # Dependencies
├── setup.py                      # Setup configuration
├── pyproject.toml                # Modern Python packaging
├── install.bat                   # Windows installer
├── install.sh                    # Linux/Mac installer
└── README.md                     # Dokumentasi utama
```

## 🆘 Support

Jika mengalami masalah:

1. **Cek versi Python**: `python --version`
2. **Cek versi pip**: `pip --version`
3. **Cek PATH**: `echo $PATH` (Linux/Mac) atau `echo %PATH%` (Windows)
4. **Buat issue** di GitHub: [https://github.com/trimetronika/GA-ANN/issues](https://github.com/trimetronika/GA-ANN/issues)
5. **Kontak email**: tribusonowibowo@gmail.com

## 📝 Notes

- Pastikan menggunakan Python 3.8+ untuk kompatibilitas
- Gunakan virtual environment untuk isolasi dependencies
- Backup data penting sebelum menjalankan eksperimen
- Monitor penggunaan memori saat menjalankan model besar

---

**Penulis**: Tri Busono Wibowo  
**Email**: tribusonowibowo@gmail.com  
**GitHub**: [@trimetronika](https://github.com/trimetronika)
