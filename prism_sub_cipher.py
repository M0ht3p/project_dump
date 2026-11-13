import unicodedata

def create_prism_alphabet(keyword):
    key_seen = set()
    clean_key = []
    for char in keyword.upper():
        if char.isalpha() and char not in key_seen:
            key_seen.add(char)
            clean_key.append(char)
    
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇÑÁÍÓÚÝÆŒØÅÆ"
    remaining = [c for c in base_alphabet if c not in key_seen]
    cipher_alphabet = "".join(clean_key + remaining)
    return cipher_alphabet

def encrypt(plaintext, keyword):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇÑÁÍÓÚÝÆŒØÅÆ"
    cipher_alphabet = create_prism_alphabet(keyword)
    
    lower_base = base_alphabet.lower()
    lower_cipher = cipher_alphabet.lower()
    
    trans_table = str.maketrans(
        base_alphabet + lower_base, 
        cipher_alphabet + lower_cipher
    )
    return plaintext.translate(trans_table)

def decrypt(ciphertext, keyword):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇÑÁÍÓÚÝÆŒØÅÆ"
    cipher_alphabet = create_prism_alphabet(keyword)
    
    lower_base = base_alphabet.lower()
    lower_cipher = cipher_alphabet.lower()
    
    trans_table = str.maketrans(
        cipher_alphabet + lower_cipher, 
        base_alphabet + lower_base
    )
    return ciphertext.translate(trans_table)

if __name__ == "__main__":
    while True:
        choice = input("\nDo you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()
        
        if choice == 'Q':
            print("Exiting. Goodbye!")
            break
            
        elif choice in ('E', 'D'):
            keyword = input("Enter your secret keyword: ").strip()
            if not keyword:
                print("Error: Keyword cannot be empty.")
                continue
                
            text = input("Enter the message: ")
            
            if choice == 'E':
                result = encrypt(text, keyword)
                print(f"\n[Encrypted Result]:\n{result}")
            else:
                result = decrypt(text, keyword)
                print(f"\n[Decrypted Result]:\n{result}")
                
        else:
            print("Invalid choice. Please type E, D, or Q.")
