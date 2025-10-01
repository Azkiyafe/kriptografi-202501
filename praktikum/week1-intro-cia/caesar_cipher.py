"""
Caesar Cipher Sederhana
- Hanya menggeser huruf A-Z atau a-z.
- Karakter non-alfabet (spasi, angka, tanda baca) tidak diubah.
"""

def encrypt(plaintext, key):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            # normalisasi ke 0-25, geser, lalu kembalikan ke kode ASCII awal
            ciphertext.append(chr((ord(char) - shift + key) % 26 + shift))
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            plaintext.append(chr((ord(char) - shift - key) % 26 + shift))
        else:
            plaintext.append(char)
    return "".join(plaintext)

def main():
    message = "Kriptografi Modern"
    key = 3

    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext :", message)
    print("Ciphertext:", encrypted)
    print("Decrypted :", decrypted)

if __name__ == "__main__":
    main()