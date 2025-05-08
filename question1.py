def main():
    m = int(input('Enter the value of m:'))
    n = int(input('Enter the value of n:'))
    file = open("raw_text.txt", "r")
    text = file.read()
    enc_text = encrypt(text, m, n)
    print(enc_text)
    dec_text = decrypt(enc_text, m, n)
    print("Decrypted text:", dec_text)

# Encryption function
def encrypt(text, m, n):
    encrypted_text = ''
    for char in text:
        if 'a' <= char <= 'z':
            if char <= 'm':  # first half
                shift = (ord(char) - ord('a') + n * m) % 13
                encrypted_text += chr(ord('a') + shift)
            else:  # second half
                shift = (ord(char) - ord('n') - (n + m)) % 13
                encrypted_text += chr(ord('n') + shift)

        elif 'A' <= char <= 'Z':
            if char <= 'M':  # first half
                shift = (ord(char) - ord('A') - n) % 13
                encrypted_text += chr(ord('A') + shift)
            else:  # second half
                shift = (ord(char) - ord('N') + m ** 2) % 13
                encrypted_text += chr(ord('N') + shift)

        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, m, n):
    decrypted_text = ''
    for char in text:
        if 'a' <= char <= 'z':
            if char <= 'm':  # first half
                shift = (ord(char) - ord('a') - n * m) % 13
                decrypted_text += chr(ord('a') + shift)
            else:  # second half
                shift = (ord(char) - ord('n') + (n + m)) % 13
                decrypted_text += chr(ord('n') + shift)

        elif 'A' <= char <= 'Z':
            if char <= 'M':  # first half
                shift = (ord(char) - ord('A') + n) % 13
                decrypted_text += chr(ord('A') + shift)
            else:  # second half
                shift = (ord(char) - ord('N') - m ** 2) % 13
                decrypted_text += chr(ord('N') + shift)
        else:
            decrypted_text += char
    return decrypted_text

if __name__=="__main__":
    main()