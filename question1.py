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
            # We reverse by applying the inverse of the transformation
            # Try reversing both rules, and pick the one that encrypts back to this char
            # First: try reverse of rule 1 (original a-m → was shifted forward by n*m)
            original_1 = (ord(char) - ord('a') - n * m) % 26
            forward_candidate = chr(ord('a') + original_1)

            if forward_candidate <= 'm':
                decrypted_text += forward_candidate
            else:
                # Must have been from n-z → reverse shift of (n + m)
                original_2 = (ord(char) - ord('a') + (n + m)) % 26
                decrypted_text += chr(ord('a') + original_2)

        elif 'A' <= char <= 'Z':
            # First: reverse rule 1 (A-M → was shifted backward by n)
            original_1 = (ord(char) - ord('A') + n) % 26
            forward_candidate = chr(ord('A') + original_1)

            if forward_candidate <= 'M':
                decrypted_text += forward_candidate
            else:
                # Must have been from N-Z → was shifted forward by m^2 → undo with -m^2
                original_2 = (ord(char) - ord('A') - m**2) % 26
                decrypted_text += chr(ord('A') + original_2)

        else:
            decrypted_text += char

    return decrypted_text

if __name__=="__main__":
    main()