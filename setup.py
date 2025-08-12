try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    def find_packages():
        return []

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ga-ann-ihsg",
    version="1.0.0",
    author="Tri Busono Wibowo",
    author_email="tribusonowibowo@gmail.com",
    description="Peramalan IHSG menggunakan Algoritma Genetika dan Jaringan Saraf Tiruan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trimetronika/GA-ANN",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black>=23.0.0,<24.0.0",
            "flake8>=6.0.0,<7.0.0",
            "pytest>=7.4.0,<8.0.0",
            "mypy>=1.5.0,<2.0.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
