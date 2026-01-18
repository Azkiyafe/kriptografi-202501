# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: TinyCoin ERC20
Nama: Azkiya Fe Sabella 
NIM: 230202802  
Kelas: 5 IKKA  

## 1. Tujuan
## Capaian Kegiatan
Pada akhir sesi ini mahasiswa menghasilkan:  
- Implementasi **smart contract ERC20 (TinyCoin)** menggunakan Solidity.  
- Dokumentasi proyek di repository Git (kode, README, laporan).  
- Laporan teknis berisi penjelasan implementasi, hasil pengujian, serta analisis keamanan dasar.  
- Commit Git dengan format `week15-tinycoin-erc20`.  

## 2. Dasar Teori
# Teori Dasar Smart Contract ERC20 (TinyCoin)

## Pengertian Smart Contract
Smart contract adalah program komputer yang berjalan di atas blockchain dan dieksekusi secara otomatis ketika kondisi yang telah ditentukan terpenuhi. Smart contract bersifat terdesentralisasi, transparan, dan immutable, sehingga tidak dapat diubah setelah dideploy ke jaringan blockchain.

Dalam ekosistem Ethereum, smart contract ditulis menggunakan bahasa pemrograman **Solidity** dan dijalankan pada **Ethereum Virtual Machine (EVM)**.

---

## Standar ERC20
ERC20 merupakan standar teknis yang digunakan untuk membuat token fungible pada blockchain Ethereum. Token fungible adalah token yang memiliki nilai yang sama satu sama lain dan dapat dipertukarkan secara bebas.

Standar ERC20 mendefinisikan sekumpulan fungsi dan event wajib yang harus diimplementasikan agar token dapat digunakan secara kompatibel dengan wallet, exchange, dan aplikasi terdesentralisasi.

Fungsi utama yang didefinisikan dalam ERC20 antara lain:
- `totalSupply()` untuk mengetahui jumlah total token
- `balanceOf()` untuk mengecek saldo token suatu alamat
- `transfer()` untuk mentransfer token ke alamat lain
- `approve()` dan `transferFrom()` untuk mekanisme delegasi transfer

Event penting dalam ERC20:
- `Transfer`
- `Approval`

---

## Konsep TinyCoin
TinyCoin adalah contoh implementasi token ERC20 sederhana yang digunakan untuk tujuan pembelajaran. TinyCoin mengikuti aturan dan struktur standar ERC20, namun dengan fitur yang minimal agar mudah dipahami.

TinyCoin digunakan untuk mensimulasikan proses:
- Pembuatan token
- Distribusi token awal
- Transfer token antar pengguna
- Pencatatan transaksi ke dalam blockchain

---

## Mekanisme Kerja TinyCoin
Pada saat smart contract TinyCoin dideploy:
1. Jumlah total token (`totalSupply`) ditentukan
2. Token awal dialokasikan ke alamat pembuat kontrak
3. Saldo pengguna disimpan dalam struktur data `mapping`
4. Fungsi `transfer` digunakan untuk memindahkan token
5. Event `Transfer` dicatat setiap terjadi transaksi

Mekanisme ini memastikan bahwa setiap perubahan saldo tercatat secara transparan dan dapat diverifikasi oleh siapa pun melalui blockchain explorer.

---

## Keunggulan dan Keterbatasan ERC20
### Keunggulan:
- Standarisasi token yang luas
- Kompatibel dengan berbagai wallet dan exchange
- Mudah diimplementasikan dan dikembangkan

### Keterbatasan:
- Tidak mendukung fitur kompleks secara bawaan
- Rentan terhadap kesalahan implementasi jika tidak diaudit
- Biaya transaksi bergantung pada gas fee Ethereum

---

## Kesimpulan
Smart contract ERC20 seperti TinyCoin memberikan pemahaman dasar tentang bagaimana token digital dibuat dan dikelola dalam blockchain Ethereum. Dengan mengikuti standar ERC20, TinyCoin dapat berfungsi secara konsisten dalam ekosistem blockchain, namun pengembang tetap perlu memperhatikan aspek keamanan dan efisiensi dalam implementasinya.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
## Panduan Langkah demi Langkah

### Langkah 1 — Membuat Kontrak ERC20
Contoh kontrak sederhana `TinyCoin.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}
```

---

### Langkah 2 — Deploy Kontrak
- Buka **Remix IDE** → buat file `TinyCoin.sol`.  
- Kompilasi dengan Solidity Compiler.  
- Deploy ke jaringan **JavaScript VM** atau testnet Ethereum.  
- Catat alamat kontrak hasil deployment.  

---

### Langkah 3 — Uji Fungsionalitas
- Cek saldo awal dengan fungsi `balanceOf(address)`.  
- Lakukan transfer token dengan fungsi `transfer(address, amount)`.  
- Uji apakah total supply tetap konsisten setelah transaksi.  

---

### Langkah 4 — Dokumentasi
- Simpan tangkapan layar proses deployment & transaksi.  
- Dokumentasikan alur kontrak (fungsi utama: `constructor`, `mint`, `transfer`).  
- Tambahkan analisis singkat tentang potensi keamanan smart contract (contoh: reentrancy, overflow – walaupun mitigasi sudah ada di Solidity >=0.8).  

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
### 1. Apa fungsi utama ERC20 dalam ekosistem blockchain?

ERC20 adalah standar smart contract pada blockchain Ethereum yang digunakan untuk membuat dan mengelola **token fungible**, yaitu token yang memiliki nilai yang sama satu sama lain.

Fungsi utama ERC20 dalam ekosistem blockchain adalah:
- Menyediakan standar yang seragam untuk pembuatan token
- Memudahkan integrasi token dengan wallet, exchange, dan aplikasi terdesentralisasi (DApp)
- Menjamin kompatibilitas antar token dalam ekosistem Ethereum
- Menyederhanakan proses transfer dan pengecekan saldo token

Dengan adanya standar ERC20, pengembang tidak perlu membuat sistem token dari awal karena telah tersedia aturan dan fungsi baku.

---

### 2. Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20?

Mekanisme transfer token dalam kontrak ERC20 bekerja dengan cara memindahkan sejumlah token dari satu alamat ke alamat lain melalui fungsi `transfer`.

Alur mekanisme transfer token ERC20:
1. Pengguna memanggil fungsi `transfer`
2. Smart contract memverifikasi saldo pengirim
3. Saldo pengirim dikurangi sesuai jumlah token
4. Saldo penerima ditambahkan
5. Event `Transfer` dicatat ke blockchain

Contoh implementasi fungsi transfer:
```solidity
mapping(address => uint256) balances;

function transfer(address to, uint256 amount) public returns (bool) {
    require(balances[msg.sender] >= amount, "Saldo tidak mencukupi");

    balances[msg.sender] -= amount;
    balances[to] += amount;

    emit Transfer(msg.sender, to, amount);
    return true;
}

### 3. Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya?

Smart contract memiliki sifat **immutable**, yaitu tidak dapat diubah setelah dideploy ke blockchain. Oleh karena itu, kesalahan dalam implementasi dapat menyebabkan kerugian permanen.

### Risiko utama dalam implementasi smart contract:
- **Bug atau kesalahan logika kode**
- **Reentrancy attack**
- **Kontrol akses yang lemah**
- **Kurangnya validasi input**
- **Kesalahan pengelolaan aset atau saldo**

### Contoh risiko: Reentrancy Attack
```solidity
function withdraw() public {
    uint256 amount = balances[msg.sender];
    require(amount > 0);

    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);

    balances[msg.sender] = 0;
}

## 8. Kesimpulan

Berdasarkan percobaan dan pembahasan mengenai standar ERC20 dan implementasi smart contract, dapat disimpulkan bahwa ERC20 berperan penting dalam standarisasi pembuatan dan pengelolaan token pada blockchain Ethereum. Dengan adanya standar ini, proses integrasi token dengan berbagai wallet, exchange, dan aplikasi terdesentralisasi dapat dilakukan dengan lebih mudah dan konsisten.

Mekanisme transfer token ERC20 bekerja dengan prinsip pemindahan saldo dari pengirim ke penerima yang disertai pencatatan event `Transfer` ke dalam blockchain, sehingga seluruh transaksi dapat dipantau secara transparan dan aman.

Selain itu, percobaan ini menunjukkan bahwa implementasi smart contract memiliki risiko keamanan yang perlu diperhatikan, seperti kesalahan logika dan serangan reentrancy. Oleh karena itu, penerapan praktik pengembangan yang baik seperti penggunaan pola Checks-Effects-Interactions, audit kode, serta pemanfaatan library terpercaya sangat diperlukan untuk meminimalkan risiko dan memastikan keamanan smart contract sebelum digunakan secara luas.


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
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
