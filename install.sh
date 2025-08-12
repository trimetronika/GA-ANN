#!/bin/bash

echo "========================================"
echo "   GA-ANN IHSG - Installer Script"
echo "========================================"
echo

echo "[1/4] Upgrade pip..."
python3 -m pip install --upgrade pip

echo
echo "[2/4] Install setuptools dan wheel..."
python3 -m pip install "setuptools>=65.0" "wheel>=0.40.0"

echo
echo "[3/4] Install dependencies dari requirements.txt..."
python3 -m pip install -r requirements.txt

echo
echo "[4/4] Install package dalam mode development..."
python3 -m pip install -e .

echo
echo "========================================"
echo "   Instalasi selesai!"
echo "========================================"
echo
echo "Package GA-ANN IHSG siap digunakan."
echo
