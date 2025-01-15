def encrypt_text(n, m):
    def shift_char(char):
        if 'a' <= char <= 'm':
            return chr(((ord(char) - ord('a') + (n * m)) % 13) + ord('a'))
        elif 'n' <= char <= 'z':
            return chr(((ord(char) - ord('n') - (n + m)) % 13) + ord('n'))
        elif 'A' <= char <= 'M':
            return chr(((ord(char) - ord('A') - n) % 13) + ord('A'))
        elif 'N' <= char <= 'Z':
            return chr(((ord(char) - ord('N') + (m ** 2)) % 13) + ord('N'))
        else:
            return char

    try:
        with open("raw_text.txt", "r") as file:
            raw_text = file.read()
        
        encrypted_text = "".join(shift_char(char) for char in raw_text)

        with open("encrypted_text.txt", "w") as file:
            file.write(encrypted_text)
            print("Encrypted Text:", encrypted_text)

        print("Encryption complete. Encrypted text saved to 'encrypted_text.txt'.")
    except FileNotFoundError:
        print("File 'raw_text.txt' not found.")


def decrypt_text(n, m):
    def reverse_shift_char(char):
        if 'a' <= char <= 'm':
            return chr(((ord(char) - ord('a') - (n * m)) % 13) + ord('a'))
        elif 'n' <= char <= 'z':
            return chr(((ord(char) - ord('n') + (n + m)) % 13) + ord('n'))
        elif 'A' <= char <= 'M':
            return chr(((ord(char) - ord('A') + n) % 13) + ord('A'))
        elif 'N' <= char <= 'Z':
            return chr(((ord(char) - ord('N') - (m ** 2)) % 13) + ord('N'))
        else:
            return char

    try:
        with open("encrypted_text.txt", "r") as file:
            encrypted_text = file.read()

        decrypted_text = "".join(reverse_shift_char(char) for char in encrypted_text)

        print("Decryption complete.")
        return decrypted_text
    except FileNotFoundError:
        print("File 'encrypted_text.txt' not found.")
        return ""


def verify_decryption(raw_text, decrypted_text):
    if raw_text == decrypted_text:
        print("Decryption verified: The original and decrypted texts match.")
    else:
        print("Decryption failed: The original and decrypted texts do not match.")


# Example usage
if __name__ == "__main__":
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    encrypt_text(n, m)

    try:
        with open("raw_text.txt", "r") as file:
            original_text = file.read()

        decrypted = decrypt_text(n, m)
        verify_decryption(original_text, decrypted)
    except FileNotFoundError:
        print("File 'raw_text.txt' not found. Cannot verify decryption.")
