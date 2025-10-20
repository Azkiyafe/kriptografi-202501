# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: [judul praktikum]  
Nama: Azkiya Fe Sabella  
NIM: 230202802  
Kelas: 5 IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
Menyiapkan repositori GitHub sebagai media kerja praktikum.

---

## 2. Dasar Teori
Cipher klasik adalah metode penyandian pesan yang digunakan sebelum munculnya teknologi komputer modern. Prinsip dasarnya adalah mengubah pesan asli (plaintext) menjadi bentuk tidak terbaca (ciphertext) menggunakan operasi sederhana seperti pergeseran huruf, penggantian karakter, atau pengacakan posisi huruf. Contoh cipher klasik yang terkenal adalah Caesar Cipher, di mana setiap huruf digeser sejauh beberapa posisi dalam alfabet, dan Vigenère Cipher yang menggunakan kata kunci untuk menentukan pola pergeseran. Tujuan utama cipher klasik adalah menjaga kerahasiaan pesan agar tidak mudah dipahami oleh pihak yang tidak berhak.

Dalam proses enkripsi pada cipher klasik, konsep modular aritmetika memegang peran penting. Modular aritmetika merupakan sistem bilangan yang melakukan operasi berdasarkan nilai sisa pembagian dengan angka tertentu yang disebut modulus. Misalnya, (7 \mod 5 = 2) karena sisa pembagian 7 dengan 5 adalah 2. Dalam kriptografi, operasi ini digunakan untuk menjaga agar hasil pergeseran huruf tetap berada dalam rentang alfabet. Pada Caesar Cipher, perhitungannya dinyatakan dengan rumus (C = (P + K) \mod 26), di mana 26 mewakili jumlah huruf dalam alfabet Latin.

Jenis cipher klasik terbagi menjadi dua kategori utama, yaitu substitution cipher dan transposition cipher. Substitution cipher mengganti setiap huruf dengan huruf lain berdasarkan pola tertentu, sedangkan transposition cipher hanya mengubah posisi huruf tanpa mengubah karakter aslinya. Contohnya, pada substitution cipher, huruf A bisa diganti menjadi D jika menggunakan pergeseran tiga posisi, sedangkan pada transposition cipher, urutan huruf dalam kata diacak mengikuti pola tertentu untuk menghasilkan ciphertext yang berbeda dari bentuk aslinya.

Keamanan dalam cipher klasik sangat bergantung pada kunci (key) yang digunakan. Tanpa kunci yang tepat, pesan sulit dikembalikan ke bentuk semula. Namun, seiring waktu, cipher klasik menjadi mudah dipecahkan dengan metode analisis frekuensi, yaitu teknik yang memanfaatkan pola kemunculan huruf dalam suatu bahasa. Meskipun demikian, konsep dasar dari cipher klasik tetap menjadi fondasi penting dalam pengembangan sistem kriptografi modern yang lebih kompleks dan aman

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Claude Elwood Shannon (1916–2001) adalah seorang matematikawan, insinyur listrik, dan ilmuwan Amerika yang dikenal sebagai pelopor teori informasi dan kriptografi modern. Pada tahun 1949, ia menerbitkan karya monumental berjudul “Communication Theory of Secrecy Systems”, yang menjelaskan dasar-dasar ilmiah dari sistem kriptografi menggunakan prinsip matematika dan teori probabilitas.   
- Pertanyaan 2: Beberapa algoritma kunci publik yang populer digunakan saat ini antara lain RSA (Rivest–Shamir–Adleman) yang mengandalkan kesulitan memfaktorkan bilangan besar, ECC (Elliptic Curve Cryptography) yang menawarkan keamanan tinggi dengan ukuran kunci lebih kecil dan efisien untuk perangkat modern, Diffie–Hellman untuk pertukaran kunci secara aman, ElGamal untuk enkripsi berbasis prinsip Diffie–Hellman, serta DSA (Digital Signature Algorithm) yang digunakan khusus untuk tanda tangan digital. Di antara algoritma tersebut, RSA dan ECC merupakan yang paling banyak digunakan dalam berbagai sistem keamanan modern seperti HTTPS, enkripsi email, dan tanda tangan digital.
- Pertanyaan 3: Kriptografi klasik dan kriptografi modern berbeda terutama pada metode dan tingkat keamanannya. Kriptografi klasik menggunakan teknik sederhana seperti substitusi dan transposisi huruf, dengan satu kunci yang sama untuk enkripsi dan dekripsi, sehingga mudah dipecahkan menggunakan analisis frekuensi. Sementara itu, kriptografi modern bekerja pada data digital dan didasarkan pada prinsip matematika kompleks dengan penggunaan kunci simetris maupun asimetris. Keamanan kriptografi modern bergantung pada kerahasiaan kunci, bukan algoritma, sehingga jauh lebih kuat dan banyak digunakan dalam sistem digital seperti internet, perbankan, dan komunikasi elektronik
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Azkiya Fe Sabella <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
