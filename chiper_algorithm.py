def caesar_cipher(message, shift, decrypt=False):
    result = ""

    # Adjust the shift value for decryption
    if decrypt:
        shift = -shift

    for char in message:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()

            # Shift the character
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))

            # Append the shifted character to the result
            result += shifted_char
        else:
            # If the character is not alphabetic, keep it unchanged
            result += char

    return result

# Get input from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message using the Caesar cipher
encrypted_message = caesar_cipher(message, shift)
print("Encrypted message:", encrypted_message)

# Decrypt the message using the Caesar cipher
decrypted_message = caesar_cipher(encrypted_message, shift, decrypt=True)
print("Decrypted message:", decrypted_message)
