# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Ahmad Ismut Thoriequddin
NIM: 2225250011
Kelas: 3A

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan
python3 praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan

| Kategori | Syarat / Kondisi | Contoh Masukan |
| :--- | :--- | :--- |
| Validasi Tipe | Masukan bukan berupa angka / float | `ujian = "abc"` |
| Validasi Ujian | `ujian < 0` atau `ujian > 100` | `ujian = 105` |
| Validasi Tugas | `tugas < 0` atau `tugas > 100` | `tugas = -10` |
| Validasi Kehadiran | `hadir < 0` atau `hadir > 100` | `hadir = 150` |
| Kehadiran Kurang | `hadir < 80` | `ujian = 85, tugas = 90, hadir = 75` |
| Predikat A & Lulus | `akhir >= 85` dan `hadir >= 80` | `ujian = 90, tugas = 85, hadir = 90` |
| Predikat B & Lulus | `70 <= akhir < 85` dan `hadir >= 80` | `ujian = 75, tugas = 80, hadir = 85` |
| Predikat C & Lulus | `60 <= akhir < 70` dan `hadir >= 80` | `ujian = 65, tugas = 60, hadir = 90` |
| Predikat D & Belum Lulus | `50 <= akhir < 60` dan `hadir >= 80` | `ujian = 55, tugas = 50, hadir = 85` |
| Predikat E & Belum Lulus | `akhir < 50` dan `hadir >= 80` | `ujian = 40, tugas = 30, hadir = 80` |

## Hasil Pengujian

| Skenario Pengujian | Masukan (Ujian, Tugas, Hadir) | Keluaran Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| Input non-angka | `abc`, `80`, `90` | Masukan ditolak: seluruh data harus berupa angka. | Masukan ditolak: seluruh data harus berupa angka. | Sesuai |
| Ujian di luar rentang | `105`, `80`, `90` | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. | Sesuai |
| Tugas di luar rentang | `80`, `-5`, `90` | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100. | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100. | Sesuai |
| Kehadiran di luar rentang | `80`, `80`, `120` | Masukan ditolak: kehadiran di luar rentang 0 sampai 100. | Masukan ditolak: kehadiran di luar rentang 0 sampai 100. | Sesuai |
| Kehadiran kurang dari 80% | `90`, `90`, `75` | Nilai akhir = 90.00<br>Predikat = -<br>Status = Tidak memenuhi syarat kehadiran | Nilai akhir = 90.00<br>Predikat = -<br>Status = Tidak memenuhi syarat kehadiran | Sesuai |
| Nilai Predikat A (Lulus) | `90`, `85`, `100` | Nilai akhir = 88.00<br>Predikat = A<br>Status = Lulus | Nilai akhir = 88.00<br>Predikat = A<br>Status = Lulus | Sesuai |
| Nilai Predikat B (Lulus) | `75`, `80`, `90` | Nilai akhir = 77.00<br>Predikat = B<br>Status = Lulus | Nilai akhir = 77.00<br>Predikat = B<br>Status = Lulus | Sesuai |
| Nilai Predikat C (Lulus) | `65`, `60`, `85` | Nilai akhir = 63.00<br>Predikat = C<br>Status = Lulus | Nilai akhir = 63.00<br>Predikat = C<br>Status = Lulus | Sesuai |
| Nilai Predikat D (Belum Lulus) | `55`, `50`, `80` | Nilai akhir = 53.00<br>Predikat = D<br>Status = Belum Lulus | Nilai akhir = 53.00<br>Predikat = D<br>Status = Belum Lulus | Sesuai |
| Nilai Predikat E (Belum Lulus) | `40`, `30`, `80` | Nilai akhir = 36.00<br>Predikat = E<br>Status = Belum Lulus | Nilai akhir = 36.00<br>Predikat = E<br>Status = Belum Lulus | Sesuai |

## Refleksi
Salah satu masukan tidak valid yang semula terlewat adalah masukan bernilai kosong (string kosong/spasi saja) atau karakter non-numerik saat penginputan nilai. Hal ini sebelumnya dapat menyebabkan program mengalami *runtime error* (`ValueError`). 

Masalah tersebut berhasil ditangani dengan menerapkan penanganan eksepsi menggunakan blok `try-except ValueError` untuk mengonversi masukan teks menjadi tipe data `float` secara aman, serta menambahkan metode `.strip()` untuk membersihkan spasi tambahan sebelum konversi dilakukan.