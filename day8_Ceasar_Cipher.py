def caesar_cipher(text, shift, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    shift = shift % 26  # normalize shift

    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)

            if mode == "encode":
                new_index = (index + shift) % 26
            else:  # decode
                new_index = (index - shift) % 26

            result += alphabet[new_index]
        else:
            result += char  # keep spaces/punctuation

    return result


# --- Program starts here ---
print("Welcome to the Caesar Cipher!")

mode = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

output = caesar_cipher(message, shift, mode)
print(f"Your {mode}d message is: {output}")
