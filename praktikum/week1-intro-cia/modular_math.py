# file: src/modular_math.py
"""
Program Python Implementasi Lengkap:
- Modular Arithmetic (add, sub, mul, exp)
- GCD & Euclidean Algorithm
- Extended Euclidean & Modular Inverse
- Discrete Logarithm Sederhana
"""

def modular_add(a, b, mod):
    """
    Penjumlahan modular: (a + b) mod n
    """
    return (a % mod + b % mod) % mod

def modular_sub(a, b, mod):
    """
    Pengurangan modular: (a - b) mod n
    """
    return (a % mod - b % mod) % mod

def modular_mul(a, b, mod):
    """
    Perkalian modular: (a * b) mod n
    """
    return (a % mod * b % mod) % mod

def modular_exp(base, exp, mod):
    """
    Eksponensial modular: (base^exp) mod n
    Menggunakan metode eksponensial cepat (fast exponentiation)
    """
    result = 1
    base = base % mod
    
    while exp > 0:
        # Jika exp ganjil, kalikan result dengan base
        if exp % 2 == 1:
            result = (result * base) % mod
        
        # exp sekarang genap
        exp = exp // 2
        base = (base * base) % mod
    
    return result

def gcd_euclidean(a, b):
    """
    Mencari GCD menggunakan Algoritma Euclidean
    """
    # Ubah ke nilai absolut
    a = abs(a)
    b = abs(b)
    
    # Algoritma Euclidean
    while b != 0:
        a, b = b, a % b
    
    return a

def extended_euclidean(a, b):
    """
    Algoritma Euclidean Diperluas
    Mengembalikan (gcd, x, y) sehingga ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_euclidean(b % a, a)
    
    # Update x dan y menggunakan rekursi
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def modular_inverse(a, mod):
    """
    Mencari invers modular a modulo n
    a * inverse ≡ 1 (mod n)
    """
    gcd, x, y = extended_euclidean(a, mod)
    
    # Invers hanya ada jika gcd(a, n) = 1
    if gcd != 1:
        raise ValueError(f"Tidak ada invers modular untuk {a} modulo {mod}. gcd({a}, {mod}) = {gcd}")
    
    # x adalah invers modular, tapi perlu disesuaikan ke range [0, mod-1]
    inverse = x % mod
    return inverse

def discrete_log_simple(base, result, mod):
    """
    Mencari diskrit log sederhana: mencari x sehingga base^x ≡ result (mod mod)
    Menggunakan brute-force (hanya untuk modulus kecil)
    """
    # Cek apakah base dan modulus coprime
    if gcd_euclidean(base, mod) != 1:
        print(f"Peringatan: base={base} dan mod={mod} tidak coprime")
    
    # Brute-force search
    current = 1
    for x in range(mod):
        if current == result % mod:
            return x
        current = (current * base) % mod
    
    return None  # Tidak ditemukan

def solve_linear_congruence(a, b, mod):
    """
    Menyelesaikan persamaan linear modular: ax ≡ b (mod n)
    """
    d = gcd_euclidean(a, mod)
    
    # Jika d tidak membagi b, tidak ada solusi
    if b % d != 0:
        return []
    
    # Normalisasi
    a, b, mod = a // d, b // d, mod // d
    
    # Cari invers modular dari a modulo mod
    inv = modular_inverse(a, mod)
    
    # Solusi khusus
    x0 = (b * inv) % mod
    
    # Semua solusi: x0 + k*mod untuk k = 0, 1, ..., d-1
    solutions = [(x0 + k * mod) % (mod * d) for k in range(d)]
    
    return sorted(solutions)

def chinese_remainder_theorem(congruences):
    """
    Menyelesaikan sistem persamaan kongruensi menggunakan Chinese Remainder Theorem
    Input: list of tuples [(a1, n1), (a2, n2), ...] untuk x ≡ a1 mod n1, x ≡ a2 mod n2, ...
    """
    if not congruences:
        return None
    
    # Inisialisasi solusi dengan kongruensi pertama
    x = congruences[0][0]
    mod_product = congruences[0][1]
    
    for i in range(1, len(congruences)):
        a, n = congruences[i]
        
        # Cek apakah moduli coprime
        if gcd_euclidean(mod_product, n) != 1:
            raise ValueError(f"Moduli tidak coprime: {mod_product} dan {n}")
        
        # Cari koefisien untuk kombinasi
        m1, m2 = mod_product, n
        _, inv1, inv2 = extended_euclidean(m1, m2)
        
        # Update solusi
        x = (x * m2 * inv2 + a * m1 * inv1) % (m1 * m2)
        mod_product *= n
    
    return x

def demo():
    """
    Demonstrasi semua fungsi
    """
    print("=" * 60)
    print("DEMONSTRASI MODULAR ARITHMETIC DAN GCD")
    print("=" * 60)
    
    # Contoh bilangan untuk demo
    a, b, mod = 17, 19, 26
    
    print(f"\n1. OPERASI MODULAR DASAR (mod {mod})")
    print(f"   {a} + {b} mod {mod} = {modular_add(a, b, mod)}")
    print(f"   {a} - {b} mod {mod} = {modular_sub(a, b, mod)}")
    print(f"   {a} * {b} mod {mod} = {modular_mul(a, b, mod)}")
    print(f"   {a}^{3} mod {mod} = {modular_exp(a, 3, mod)}")
    
    print(f"\n2. GCD DAN ALGORITMA EUCLIDEAN")
    gcd_ab = gcd_euclidean(a, b)
    print(f"   gcd({a}, {b}) = {gcd_ab}")
    print(f"   gcd(48, 18) = {gcd_euclidean(48, 18)}")
    print(f"   gcd(35, 14) = {gcd_euclidean(35, 14)}")
    
    print(f"\n3. EXTENDED EUCLIDEAN DAN INVERS MODULAR")
    gcd, x, y = extended_euclidean(a, mod)
    print(f"   Extended Euclidean: {a}*{x} + {mod}*{y} = {gcd}")
    
    # Contoh invers modular
    a_inv = 7
    mod_inv = 26
    try:
        inv = modular_inverse(a_inv, mod_inv)
        print(f"   Invers modular dari {a_inv} modulo {mod_inv} = {inv}")
        print(f"   Verifikasi: {a_inv} * {inv} mod {mod_inv} = {(a_inv * inv) % mod_inv}")
    except ValueError as e:
        print(f"   {e}")
    
    print(f"\n4. DISKRIT LOG SEDERHANA")
    base, target, mod_log = 3, 13, 17
    log_result = discrete_log_simple(base, target, mod_log)
    if log_result is not None:
        print(f"   {base}^{log_result} ≡ {target} (mod {mod_log})")
        print(f"   Verifikasi: {base}^{log_result} mod {mod_log} = {modular_exp(base, log_result, mod_log)}")
    else:
        print(f"   Tidak ditemukan x sehingga {base}^x ≡ {target} (mod {mod_log})")
    
    print(f"\n5. PERSAMAAN LINEAR MODULAR")
    a_lin, b_lin, mod_lin = 6, 3, 15
    solutions = solve_linear_congruence(a_lin, b_lin, mod_lin)
    if solutions:
        print(f"   Solusi {a_lin}x ≡ {b_lin} (mod {mod_lin}): {solutions}")
    else:
        print(f"   Tidak ada solusi untuk {a_lin}x ≡ {b_lin} (mod {mod_lin})")
    
    print(f"\n6. CHINESE REMAINDER THEOREM")
    congruences = [(2, 3), (3, 5), (2, 7)]
    print(f"   Sistem kongruensi: {congruences}")
    try:
        crt_solution = chinese_remainder_theorem(congruences)
        print(f"   Solusi: x ≡ {crt_solution} mod {3*5*7}")
        
        # Verifikasi
        print("   Verifikasi:")
        for a, n in congruences:
            print(f"     {crt_solution} mod {n} = {crt_solution % n} ≡ {a} (mod {n})")
    except ValueError as e:
        print(f"   Error: {e}")
    
    print(f"\n7. CONTOH APLIKASI KRIPTOGRAFI SEDERHANA")
    # Enkripsi sederhana: C = M^e mod n
    message = 15
    e, n = 5, 91
    encrypted = modular_exp(message, e, n)
    print(f"   Enkripsi: {message}^{e} mod {n} = {encrypted}")
    
    # Dekripsi (diasumsikan kita tahu d)
    d = 29  # Kunci privat
    decrypted = modular_exp(encrypted, d, n)
    print(f"   Dekripsi: {encrypted}^{d} mod {n} = {decrypted}")
    print(f"   Pesan asli: {message}, Hasil dekripsi: {decrypted}")

def interactive_mode():
    """
    Mode interaktif untuk pengguna
    """
    print("\n" + "=" * 60)
    print("MODE INTERAKTIF")
    print("=" * 60)
    
    while True:
        print("\nPilih operasi:")
        print("1. Operasi Modular Dasar")
        print("2. Hitung GCD")
        print("3. Cari Invers Modular")
        print("4. Diskrit Log (Brute-force)")
        print("5. Selesaikan Persamaan Linear Modular")
        print("6. Chinese Remainder Theorem")
        print("7. Demo Semua Fungsi")
        print("8. Keluar")
        
        choice = input("\nPilihan Anda (1-8): ").strip()
        
        if choice == '1':
            try:
                a = int(input("Masukkan a: "))
                b = int(input("Masukkan b: "))
                mod = int(input("Masukkan modulus n: "))
                
                print(f"\nHasil:")
                print(f"  ({a} + {b}) mod {mod} = {modular_add(a, b, mod)}")
                print(f"  ({a} - {b}) mod {mod} = {modular_sub(a, b, mod)}")
                print(f"  ({a} * {b}) mod {mod} = {modular_mul(a, b, mod)}")
                
                exp = int(input("Masukkan eksponen untuk perpangkatan: "))
                print(f"  {a}^{exp} mod {mod} = {modular_exp(a, exp, mod)}")
            except ValueError:
                print("Input tidak valid!")
                
        elif choice == '2':
            try:
                a = int(input("Masukkan bilangan pertama: "))
                b = int(input("Masukkan bilangan kedua: "))
                gcd_val = gcd_euclidean(a, b)
                print(f"\ngcd({a}, {b}) = {gcd_val}")
                
                # Extended Euclidean
                gcd_ext, x, y = extended_euclidean(a, b)
                print(f"Extended: {a}*{x} + {b}*{y} = {gcd_ext}")
            except ValueError:
                print("Input tidak valid!")
                
        elif choice == '3':
            try:
                a = int(input("Masukkan bilangan a: "))
                mod = int(input("Masukkan modulus n: "))
                inv = modular_inverse(a, mod)
                print(f"\nInvers modular dari {a} modulo {mod} = {inv}")
                print(f"Verifikasi: {a} * {inv} mod {mod} = {(a * inv) % mod}")
            except ValueError as e:
                print(f"\nError: {e}")
            except Exception:
                print("Input tidak valid!")
                
        elif choice == '4':
            try:
                base = int(input("Masukkan basis: "))
                target = int(input("Masukkan target: "))
                mod = int(input("Masukkan modulus: "))
                
                result = discrete_log_simple(base, target, mod)
                if result is not None:
                    print(f"\n{base}^{result} ≡ {target} (mod {mod})")
                    print(f"Verifikasi: {base}^{result} mod {mod} = {modular_exp(base, result, mod)}")
                else:
                    print(f"\nTidak ditemukan x sehingga {base}^x ≡ {target} (mod {mod})")
            except ValueError:
                print("Input tidak valid!")
                
        elif choice == '5':
            try:
                a = int(input("Masukkan koefisien a: "))
                b = int(input("Masukkan konstanta b: "))
                mod = int(input("Masukkan modulus n: "))
                
                solutions = solve_linear_congruence(a, b, mod)
                if solutions:
                    print(f"\nSolusi {a}x ≡ {b} (mod {mod}):")
                    print(f"  {solutions}")
                else:
                    print(f"\nTidak ada solusi untuk {a}x ≡ {b} (mod {mod})")
            except ValueError:
                print("Input tidak valid!")
                
        elif choice == '6':
            try:
                n = int(input("Berapa banyak kongruensi? "))
                congruences = []
                for i in range(n):
                    a = int(input(f"Masukkan a{i+1}: "))
                    mod = int(input(f"Masukkan n{i+1}: "))
                    congruences.append((a, mod))
                
                solution = chinese_remainder_theorem(congruences)
                if solution is not None:
                    product = 1
                    for _, n in congruences:
                        product *= n
                    print(f"\nSolusi: x ≡ {solution} (mod {product})")
                    
                    # Verifikasi
                    print("\nVerifikasi:")
                    for a, n in congruences:
                        print(f"  {solution} mod {n} = {solution % n} ≡ {a} (mod {n})")
            except ValueError as e:
                print(f"\nError: {e}")
            except Exception:
                print("Input tidak valid!")
                
        elif choice == '7':
            demo()
            
        elif choice == '8':
            print("Terima kasih telah menggunakan program ini!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan pilih 1-8.")

if __name__ == "__main__":
    print("PROGRAM IMPLEMENTASI MODULAR ARITHMETIC DAN GCD")
    print("=" * 60)
    
    # Jalankan demo terlebih dahulu
    demo()
    
    # Tanya apakah ingin mode interaktif
    response = input("\nIngin mencoba mode interaktif? (y/n): ").strip().lower()
    if response == 'y':
        interactive_mode()
    else:
        print("\nProgram selesai. Anda dapat mengimpor fungsi dari modul ini.")
        print("Contoh penggunaan:")
        print("  from modular_math import modular_inverse, gcd_euclidean")
        print("  inv = modular_inverse(7, 26)")
        print("  print(inv)  # Output: 15")