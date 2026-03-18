#BASIC TEXT ENCRYPTION TO0L USING CAESAR, XOR and VIGENERE CIPHERS
#THE TOOL USES CAESAR, XOR AND  VIGENERE CIPHERS TO ENCRYPT TEXTS LIKE PASSWORDS ETC. 
# Caesar Cipher
def caesar_cipher_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

# XOR Cipher
def xor_cipher_encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

# Vigenere Cipher
def vigenere_cipher_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

#UI
def main():
    print("=== TEXT ENCRYPTION TOOL ===")
    print("Choose a cipher method:")
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
    
    text = input("Enter the text to encrypt: ")
    
    if choice == '1':  # Caesar Cipher
        while True:
            try:
                key = int(input("Enter the shift key (number): "))
                break
            except ValueError:
                print("Please enter a valid number.")
        
        encrypted = caesar_cipher_encrypt(text, key)
        print(f"\nOriginal text: {text}")
        print(f"Caesar key: {key}")
        print(f"Encrypted text: {encrypted}")
    
    elif choice == '2':  # XOR Cipher
        while True:
            try:
                key = int(input("Enter the XOR key (number 1-255): "))
                if 1 <= key <= 255:
                    break
                else:
                    print("Please enter a number between 1 and 255.")
            except ValueError:
                print("Please enter a valid number.")
        
        encrypted = xor_cipher_encrypt(text, key)
        print(f"\nOriginal text: {text}")
        print(f"XOR key: {key}")
        print(f"Encrypted text: {encrypted}")
    
    elif choice == '3':  # Vigenere Cipher
        while True:
            key = input("Enter the Vigenère key (alphabetic characters only): ").strip()
            if key.isalpha():
                break
            else:
                print("Please enter only alphabetic characters.")
        
        encrypted = vigenere_cipher_encrypt(text, key)
        print(f"\nOriginal text: {text}")
        print(f"Vigenère key: {key}")
        print(f"Encrypted text: {encrypted}")

if __name__ == "__main__":
    main()