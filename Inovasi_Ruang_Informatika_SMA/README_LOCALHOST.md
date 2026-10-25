# Ruang Informatika SMA — Folder untuk localhost

## Cara paling mudah di Windows
1. Ekstrak seluruh ZIP ini ke folder biasa, misalnya `C:\Ruang_Informatika_SMA_Localhost`.
2. Pastikan Python 3 terpasang. Unduh di https://www.python.org/downloads/ bila belum ada. Saat instalasi, aktifkan **Add Python to PATH**.
3. Klik dua kali `mulai_localhost.bat`.
4. Browser akan terbuka ke `http://127.0.0.1:8000/`.
5. Biarkan jendela terminal tetap terbuka selama web digunakan. Tekan `Ctrl+C` di jendela terminal untuk menghentikan server.

## Menjalankan melalui VS Code / terminal
Buka folder ini di VS Code. Pilih **Terminal → New Terminal**, lalu jalankan:

```bash
python start_localhost.py
```

Pada Windows, perintah alternatif:

```powershell
py -3 start_localhost.py
```

Jika port 8000 sedang digunakan, gunakan port lain:

```bash
python start_localhost.py --port 8001
```

Kemudian buka alamat yang dicetak oleh server, misalnya `http://127.0.0.1:8001/`.

## Alternatif tanpa skrip launcher
Dari terminal yang lokasinya di folder ini, jalankan:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Lalu buka `http://127.0.0.1:8000/`.

## Isi folder
- `index.html` — halaman utama Ruang Informatika SMA; CSS dan JavaScript utama sudah ada di dalamnya.
- `assets/materi/` — enam PDF bahan presentasi pertemuan Informatika.
- `assets/referensi/` — modul ajar PjBL Konten Digital dan modul ajar Sorting.
- Berkas LK 1–4 dalam DOCX dan PDF.
- `start_localhost.py`, `mulai_localhost.bat`, dan `mulai_localhost.command` — launcher server lokal.

## Catatan
- Tidak perlu `npm install` atau mengunduh library JavaScript. Server memakai Python standard library.
- Jalankan melalui `localhost` alih-alih membuka HTML dengan klik dua kali. Ini membuat tautan PDF relatif dan penyimpanan browser berjalan lebih konsisten.
- Login masih berupa simulasi antarmuka, bukan autentikasi sekolah. Isi nama/email dan kata sandi untuk masuk; tidak ada akun sekolah yang diverifikasi.
- Progres, jawaban, nilai demo, dan pengaturan disimpan di browser pada komputer tersebut, bukan database terpusat. Data tidak otomatis tersinkron ke perangkat lain.
- Folder berisi roster nama murid kelas X-C. Simpan dengan aman dan jangan unggah ke server publik.
- Pertahankan struktur `assets/` supaya tautan PDF tidak putus.


Catatan ukuran: PDF bahan presentasi dalam paket ini dioptimalkan untuk tampilan layar agar unduhan lebih ringan. Isi visual dan urutan halaman dipertahankan; file PDF tidak lagi berupa teks yang dapat dipilih/cari.
