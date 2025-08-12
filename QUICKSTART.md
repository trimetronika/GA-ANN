# ⚡ Quick Start Guide - GA-ANN IHSG

## 🚀 Instalasi Cepat (5 Menit)

### Windows
```bash
# Double-click file install.bat
# Atau jalankan di Command Prompt:
install.bat
```

### Linux/Mac
```bash
chmod +x install.sh
./install.sh
```

## 🎯 Menjalankan Proyek

### 1. Start Jupyter Notebook
```bash
jupyter notebook GA-ANN-Final.ipynb
```

### 2. Atau buka file langsung
- Buka file `GA-ANN-Final.ipynb` dengan Jupyter Notebook
- Jalankan semua cell secara berurutan

## 🔧 Jika Ada Error

### Python tidak ditemukan
1. Install Python dari [python.org](https://www.python.org/downloads/)
2. **PENTING**: Centang "Add Python to PATH"
3. Restart Command Prompt

### Dependencies error
```bash
pip install -r requirements.txt
```

### Setuptools error
```bash
pip install setuptools>=65.0 wheel>=0.40.0
```

## 📊 Struktur Data

Pastikan folder `data/` berisi:
- `raw/` - Data mentah IHSG
- `preprocessing/` - Data yang sudah diproses
- `acf_pacf/` - Analisis ACF dan PACF

## 🎮 Eksperimen

Proyek ini menjalankan **12 eksperimen** dengan kombinasi parameter berbeda:
- Selection Methods: Tournament, RWS
- Population: 50, 100
- Generations: 50, 100, 150

Hasil eksperimen tersimpan di folder `experiments/`.

## 📞 Support

- **Email**: tribusonowibowo@gmail.com
- **GitHub**: [@trimetronika](https://github.com/trimetronika)
- **Dokumentasi Lengkap**: [INSTALLATION.md](INSTALLATION.md)

---

**Penulis**: Tri Busono Wibowo  
**Proyek**: Peramalan IHSG dengan GA-ANN
