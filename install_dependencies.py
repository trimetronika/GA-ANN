#!/usr/bin/env python3
"""
Script untuk menginstal dependencies yang diperlukan untuk proyek GA-ANN IHSG.
Script ini akan memastikan setuptools terinstal sebelum menjalankan setup.py
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Menjalankan command dan menangani error"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} berhasil")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} gagal: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    print("🚀 Memulai instalasi dependencies untuk GA-ANN IHSG...")
    
    # Upgrade pip terlebih dahulu
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrade pip"):
        print("⚠️  Gagal upgrade pip, melanjutkan...")
    
    # Install setuptools dan wheel
    if not run_command(f"{sys.executable} -m pip install setuptools>=65.0 wheel>=0.40.0", "Install setuptools dan wheel"):
        print("❌ Gagal menginstal setuptools dan wheel. Instalasi dihentikan.")
        return False
    
    # Install dependencies dari requirements.txt
    if os.path.exists("requirements.txt"):
        if not run_command(f"{sys.executable} -m pip install -r requirements.txt", "Install dependencies dari requirements.txt"):
            print("❌ Gagal menginstal dependencies dari requirements.txt")
            return False
    
    # Install package dalam mode development
    if not run_command(f"{sys.executable} -m pip install -e .", "Install package dalam mode development"):
        print("❌ Gagal menginstal package dalam mode development")
        return False
    
    print("🎉 Instalasi selesai! Package GA-ANN IHSG siap digunakan.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
