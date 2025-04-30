def main():
    text = 'BcOp'
    print(text)
    enc_text = encrypt(text, n=2, m=2)
    print(enc_text)

def encrypt(text, n, m):
    encrypted_text = ''
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

if __name__=="__main__":
    main()