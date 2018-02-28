# Kuliah AMS
AMS Adalah kepanjangan dari Analisa Media Sosial.  Kuliah ini menggunakan bahasa pemrograman pyhton versi 2.7 . Livbrary yang digunakan adalah Snap. 

## Instalasi 
1. Download Python 2.7 versi 64 bit(Library hanya bisa berjalan di 64 bit) di [python-2.7.amd64.msi](https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi) . Kemudian Install
2. Download Library Snap di [snap-4.0.0-4.0-Win-x64-py2.7.zip](https://snap.stanford.edu/snappy/release/snap-4.0.0-4.0-Win-x64-py2.7.zip)
3. Pastikan Path Python sudah ada di enviroment system. Untuk mengeceknya, buka CMD , kemudian klik python. Jika Berhasil maka cmd akan masuk ke dalam terminal python jika gagal cmd akan memunculkan error "Python Not Recognized"
4. Estrak Zip Snap
5. Buka CMD. Jalankan perintah :
```
cd (Path Hasil Ektraksi Library Snap)
Contoh : Cd Downloads/snap
```
6. Jalankan Perintah :
 ```
python setup.py install
```
> Ket : Instalasi dilakukan di OS Windows 10 - 64bit
7. Untuk mengeceknya buat file python sembarang isi dengan :
```
import snap
```
Jalankan . Jika Berhasil maka tidak muncul error :)


## Tugas 1

### Tujuan:

Mampu melakukan deteksi figur sentral padajaringan pertemanan

### Uraian Tugas:

Obyek garapan: File  [Jaringan Pertemanan](https://snap.stanford.edu/data/facebook.tar.gz) pada  [https://snap.stanford.edu/data/egonets-Facebook.html](https://snap.stanford.edu/data/egonets-Facebook.html)  untuk 5 user. Yang harus dikerjakan:

1.  Membuka file  [facebook.tar.gz](https://snap.stanford.edu/data/facebook.tar.gz)  pada  [https://snap.stanford.edu/data/egonets-Facebook.html. Di dalamnya terdapat file circles, edges, egofeat, feat, dan featnames. Jaringan pertemanan terdapat pada file berekstensi edges.](https://snap.stanford.edu/data/egonets-Facebook.html)
2.  Memilih salah satu user di antara 3980 user di dalam file  [facebook.tar.gz](https://snap.stanford.edu/data/facebook.tar.gz)
3.  Menyusun graph berdasarkan file edges. Misalkan bila memilihi user 0, maka edge antar vertex di dalam jaringan pertemanan user 0 adalah 0.edges.
4.  Menghitung Eigenvector Centrality dan menentukan ranking 5 users sebagai central node tertinggi pada jaringan pertemanan user 0 tersebut.
5.  Menghitung Centrality berdasarkan Page Rank dan menentukan ranking 5 users sebagai central node tertinggi pada jaringan pertemanan user 0 tersebut.
6.  Mengulangi seluruh langkah di atas untuk 4 user yang lain, sehingga total 5 user dapat diketahui siapa tokoh sentralnya.

Metode penghitungan: Mengikuti petunjuk slide 19 dan slide 28 pada File Power Point SMM-Slides-ch3.

### Luaran Tugas:

Tugas dilaksanakan berkelompok, maks 3 anggota. Tiap anggota kelompok, perlu mengupload satu file dalam format PDF hasil tugas ini. File tersebut hendaknya berisi 5 tabel, untuk 5 user. Tiap tabel berisi nomor index 5 tokoh paling sentral dalam jaringan pertemanan milik user tersebut.

> Catatan : Md File dibuat menggunakan situs stackedit.io
