@echo off
echo ========================================
echo    GA-ANN IHSG - Installer Script
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found in PATH. Trying alternatives...
    py --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo.
        echo ========================================
        echo    ERROR: Python not found!
        echo ========================================
        echo.
        echo Please install Python from: https://www.python.org/downloads/
        echo Make sure to check "Add Python to PATH" during installation.
        echo.
        echo After installing Python, run this script again.
        echo.
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=py
        echo Found Python using 'py' command
    )
) else (
    set PYTHON_CMD=python
    echo Found Python using 'python' command
)

echo.
echo [1/4] Upgrade pip...
%PYTHON_CMD% -m pip install --upgrade pip

echo.
echo [2/4] Install setuptools dan wheel...
%PYTHON_CMD% -m pip install setuptools>=65.0 wheel>=0.40.0

echo.
echo [3/4] Install dependencies dari requirements.txt...
%PYTHON_CMD% -m pip install -r requirements.txt

echo.
echo [4/4] Install package dalam mode development...
%PYTHON_CMD% -m pip install -e .

echo.
echo ========================================
echo    Instalasi selesai!
echo ========================================
echo.
echo Package GA-ANN IHSG siap digunakan.
echo.
echo Untuk menjalankan notebook:
echo %PYTHON_CMD% -m jupyter notebook GA-ANN-Final.ipynb
echo.
pause
