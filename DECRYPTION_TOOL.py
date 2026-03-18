#BASIC TEXT DECRYPTION USING CAESAR, XOR and VIGENERE CIPHERS

# Caesar Cipher Decryption
def caesar_cipher_decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result

# XOR Cipher Decryption (same as encryption for XOR)
def xor_cipher_decrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

# Vigenère Cipher Decryption
def vigenere_cipher_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# UI
def main():
    print("=== DECRYPTION TOOL ===")
    print("Choose the cipher method used for encryption:")
    print("1. Caesar Cipher")
    print("2. XOR Cipher")
    print("3. Vigenère Cipher")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice in ['1', '2', '3']:
                break
            else:
                print("Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return
    
    encrypted_text = input("Enter the encrypted text: ")
    
    if choice == '1':  # Caesar Cipher
        while True:
            try:
                key = int(input("Enter the shift key used for encryption: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        
        decrypted = caesar_cipher_decrypt(encrypted_text, key)
        print(f"\nEncrypted text: {encrypted_text}")
        print(f"Caesar key: {key}")
        print(f"Decrypted text: {decrypted}")
    
    elif choice == '2':  # XOR Cipher
        while True:
            try:
                key = int(input("Enter the XOR key used for encryption (1-255): "))
                if 1 <= key <= 255:
                    break
                else:
                    print("Please enter a number between 1 and 255.")
            except ValueError:
                print("Please enter a valid number.")
        
        decrypted = xor_cipher_decrypt(encrypted_text, key)
        print(f"\nEncrypted text: {encrypted_text}")
        print(f"XOR key: {key}")
        print(f"Decrypted text: {decrypted}")
    
    elif choice == '3':  # Vigenère Cipher
        while True:
            key = input("Enter the Vigenère key used for encryption: ").strip()
            if key.isalpha():
                break
            else:
                print("Please enter only alphabetic characters.")
        
        decrypted = vigenere_cipher_decrypt(encrypted_text, key)
        print(f"\nEncrypted text: {encrypted_text}")
        print(f"Vigenère key: {key}")
        print(f"Decrypted text: {decrypted}")

if __name__ == "__main__":
    main()