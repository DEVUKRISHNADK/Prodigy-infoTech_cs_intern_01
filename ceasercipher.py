def caesar_cipher(message, shift, mode='encrypt'):
    result = ""

    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in message:
        # Encrypt/decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave non-alphabetic characters as is
            result += char

    return result


# Get input from the user
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift, mode='encrypt')
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
print("Decrypted Message:", decrypted_message)
