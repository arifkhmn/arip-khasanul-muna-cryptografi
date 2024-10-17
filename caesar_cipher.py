def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char  # Tidak mengubah karakter non-huruf
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)  # Menggunakan fungsi yang sama dengan shift negatif

# Contoh penggunaan
if __name__ == "__main__":
    message = "Hello, World!"
    shift_value = 3

    encrypted = caesar_encrypt(message, shift_value)
    print("Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift_value)
    print("Decrypted:", decrypted)
