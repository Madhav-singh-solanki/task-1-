def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using Caesar cipher algorithm.
    
    Parameters:
    text (str): The input text to process
    shift (int): The number of positions to shift each character
    mode (str): 'encrypt' or 'decrypt'
    
    Returns:
    str: The processed text
    """
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be either 'encrypt' or 'decrypt'")
    
    if mode == 'decrypt':
        shift = -shift
    
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine the base for uppercase or lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around if needed
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)

def main():
    print("Caesar Cipher Tool")
    print("------------------")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            encrypted = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {encrypted}")
            
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            decrypted = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {decrypted}")
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

