def main():
    m = int(input('Enter the value of m:'))
    n = int(input('Enter the value of n:'))
    # file = open("raw_text.txt", "r")
    # text = file.read()
    text = 'SandeshPaudel'
    enc_text = encrypt(text, m, n)
    print(enc_text)
    dec_text = decrypt(enc_text, m, n)
    print("Decrypted text:", dec_text)

def encrypt(text, m, n):
    encrypted_text = ''
    for char in text:
        if 'a' <= char <= 'z':
            if char <= 'm':  # first half
                shift = (ord(char) - ord('a') + n * m) % 26
                encrypted_text += chr(ord('a') + shift)
            else:  # second half
                shift = (ord(char) - ord('a') - (n + m)) % 26
                encrypted_text += chr(ord('a') + shift)

        elif 'A' <= char <= 'Z':
            if char <= 'M':  # first half
                shift = (ord(char) - ord('A') - n) % 26
                encrypted_text += chr(ord('A') + shift)
            else:  # second half
                shift = (ord(char) - ord('A') + m ** 2) % 26
                encrypted_text += chr(ord('A') + shift)

        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, m, n):
    decrypted_text = ''

    for char in text:
        if 'a' <= char <= 'z':
            # Try both decryption paths — only one will land back in a valid 'a-m' or 'n-z' range
            forward_shift = (ord(char) - ord('a') - n * m) % 26
            backward_shift = (ord(char) - ord('a') + (n + m)) % 26
            if chr(ord('a') + backward_shift) <= 'm':
                decrypted_text += chr(ord('a') + forward_shift)
            else:
                decrypted_text += chr(ord('a') + backward_shift)

        elif 'A' <= char <= 'Z':
            backward_shift = (ord(char) - ord('A') + n) % 26
            forward_shift = (ord(char) - ord('A') - m ** 2) % 26
            if chr(ord('A') + backward_shift) <= 'M':
                decrypted_text += chr(ord('A') + backward_shift)
            else:
                decrypted_text += chr(ord('A') + forward_shift)

        else:
            decrypted_text += char

    return decrypted_text
# def decrypt(encrypted_text, m, n):
#     decrypted_text = ''
#     for char in encrypted_text:
        
#         # logic for lowercase letters
#         if 'a' <= char <= 'z':
#             # Originally from a-m (shifted forward by n * m)
#             if char <= 'm':
#                 shift_value = n * m
#                 remaining_shift = (ord(char) - ord('a') - shift_value) % 26
#                 transformed_char = chr(ord('a') + remaining_shift)
#                 decrypted_text += transformed_char

#             # Originally from n-z (shifted backward by n + m)
#             else:
#                 shift_value = n + m
#                 remaining_shift = (ord(char) - ord('a') + shift_value) % 26
#                 transformed_char = chr(ord('a') + remaining_shift)
#                 decrypted_text += transformed_char

#         # logic for uppercase letters
#         elif 'A' <= char <= 'Z':
#             # Originally from A-M (shifted backward by n)
#             if char <= 'M':
#                 shift_value = n
#                 remaining_shift = (ord(char) - ord('A') + shift_value) % 26
#                 transformed_char = chr(ord('A') + remaining_shift)
#                 decrypted_text += transformed_char

#             # Originally from N-Z (shifted forward by m^2)
#             else:
#                 shift_value = m ** 2
#                 remaining_shift = (ord(char) - ord('A') - shift_value) % 26
#                 transformed_char = chr(ord('A') + remaining_shift)
#                 decrypted_text += transformed_char

#         # logic for non-alphabetic characters
#         else:
#             decrypted_text += char
#     return decrypted_text

if __name__=="__main__":
    main()