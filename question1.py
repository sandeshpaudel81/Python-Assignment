def main():
    file = open("raw_text.txt", "r")
    text = file.read()
    enc_text = encrypt(text)
    print(enc_text)
    dec_text = decrypt(enc_text, n=2, m=2)
    print("Decrypted text:", dec_text)

def encrypt(text):
    encrypted_text = ''
    m = input('Enter the value of m:')
    n = input('Enter the value of n:')
    for char in text:
        # logic for lowercase letters
        if 'a' <= char <= 'z':
            # if the letter is in first half (a-m)
            if char<='m':
                shift = (n * m - (ord('z') - ord(char))) % 26
                transformed_char = chr(ord('a') + shift - 1)
                encrypted_text += transformed_char

            # if the letter is in second half (n-z)
            else:
                shift = (n + m - (ord(char) - ord('a'))) % 26
                transformed_char = chr(ord('z') + 1 - shift)
                encrypted_text += transformed_char

        # logic for uppercase letters
        elif 'A' <= char <= 'Z':
            # if the letter is in first half (A-M)
            if char<='M':
                shift = (n - (ord(char) - ord('A'))) % 26
                transformed_char = chr(ord('Z') + 1 - shift)
                encrypted_text += transformed_char

            # if the letter is in first half (N-Z)    
            else:
                shift = (m ** 2 - (ord('Z') - ord(char))) % 26
                transformed_char = chr(ord('A') + shift - 1)
                encrypted_text += transformed_char

        # logic for all other characters and numbers
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, n, m):
    decrypted_text = ''
    for char in encrypted_text:
        
        # logic for lowercase letters
        if 'a' <= char <= 'z':
            # Originally from a-m (shifted forward by n * m)
            if char <= 'm':
                shift_value = n * m
                remaining_shift = (ord(char) - ord('a') - shift_value) % 26
                transformed_char = chr(ord('a') + remaining_shift)
                decrypted_text += transformed_char

            # Originally from n-z (shifted backward by n + m)
            else:
                shift_value = n + m
                remaining_shift = (ord(char) - ord('a') + shift_value) % 26
                transformed_char = chr(ord('a') + remaining_shift)
                decrypted_text += transformed_char

        # logic for uppercase letters
        elif 'A' <= char <= 'Z':
            # Originally from A-M (shifted backward by n)
            if char <= 'M':
                shift_value = n
                remaining_shift = (ord(char) - ord('A') + shift_value) % 26
                transformed_char = chr(ord('A') + remaining_shift)
                decrypted_text += transformed_char

            # Originally from N-Z (shifted forward by m^2)
            else:
                shift_value = m ** 2
                remaining_shift = (ord(char) - ord('A') - shift_value) % 26
                transformed_char = chr(ord('A') + remaining_shift)
                decrypted_text += transformed_char

        # logic for non-alphabetic characters
        else:
            decrypted_text += char

    print("Decrypted message:", decrypted_text)
    return decrypted_text

if __name__=="__main__":
    main()