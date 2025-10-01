# Laporan Minggu 1 - Intro CIA


## 1. Deskripsi Fungsi

### Fungsi `encrypt(text, key)`
Fungsi ini menerima input berupa teks dan angka kunci (key). Teks akan digeser berdasarkan nilai kunci, sesuai aturan Caesar Cipher. Huruf kapital dan kecil tetap dipertahankan. Karakter non-huruf tidak berubah.

### Fungsi `decrypt(cipher_text, key)`
Fungsi ini digunakan untuk mengembalikan teks terenkripsi ke bentuk aslinya dengan cara menggeser huruf ke arah sebaliknya. Implementasinya memanggil fungsi `encrypt` dengan nilai kunci negatif.

---

## 2. Penjelasan Hasil Uji Coba

### Input:
```text
Teks: Kriptografi Modern
