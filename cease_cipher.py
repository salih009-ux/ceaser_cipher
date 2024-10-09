def caesar_cipher(text, shift, direction):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65) if direction == "encrypt" else chr((ord(char) - shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97) if direction == "encrypt" else chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char

    return result

# Input from the user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
direction = input("Enter the direction (encrypt/decrypt): ")

# Perform the encryption/decryption
cipher_text = caesar_cipher(text, shift, direction)
print(f"Result: {cipher_text}")
