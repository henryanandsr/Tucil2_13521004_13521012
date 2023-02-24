# Tugas Kecil II - Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer
## Deskripsi Tugas
Mencari sepasang titik terdekat dengan Algoritma Divide and Conquer sudah dijelaskan di dalam kuliah. Persoalan tersebut dirumuskan untuk titik pada bidang datar (2D). Pada Tucil 2 kali ini Anda diminta mengembangkan algoritma mencari sepasang titik terdekat pada bidang 3D. Misalkan terdapat n buah titik pada ruang 3D. Setiap titik P di dalam ruang dinyatakan dengan koordinat P = (x, y, z). Carilah sepasang titik yang mempunyai jarak terdekat satu sama lain. Jarak dua buah titk P1 = (x1, y1, z1) dan P2 = (x2, y2, z2) dihitung dengan rumus Euclidean.
## Anggota Kelompok
| NIM | Nama |
| :---: | :---: |
| 13521004 | Henry Anand Septian Radityo |
| 13521012 | Haikal Ardzi Shofiyyurrohm |
## Implementasi Algoritma Divide and Conquer
Algoritma divide and conquer dilakukan untuk membagi permasalahan pencarian titik terdekat dengan membagi dua untuk titik - titik secara rekursif hingga mendapatkan titik yang berjumlah 2 atau 3. Titik yang berjumlah 2 atau 3 nantinya akan digunakan sebagai basis untuk menghitung jarak terpendek.
## Instalasi
1. Pastikan device Anda sudah terinstall Python
2. Lakukan instalasi matplotlib untuk mendukung visualisasi 
```
python -m pip install -U pip
python -m pip install -U matplotlib
```
3. Lakukan clone pada repository dengan memasukkan kode berikut di terminal
`git clone https://github.com/henryanandsr/Tucil2_Strategi-Algoritma/`
4. Lakukan run dengan mengetikkan `py main.py` pada terminal yang sesuai dengan lokasi clone
## Struktur Program
```
.
│   README.md
|   .gitignore
├───doc
│       Tucil2_13521004_13521012.pdf
│       
└───src
        _pycache_
        Point.py
        main.py
```
