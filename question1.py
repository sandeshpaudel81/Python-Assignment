def main():
    user_m = input('Enter the value of m: ')
    try:
        m = int(user_m)
    except ValueError:
        try:
            float_m = float(user_m)
            m= int(round(float_m,0))
            print("Your input is rounded to ", m)
        except ValueError:
            ascii_values = [ord(char) for char in user_m]
            m = round(sum(ascii_values),0)
            print("Your input is converted to integer number: ", m)
            if type(m) != int:
                m = 0
                print("Your input is set as defalut value: ", m)

    user_n = input('Enter the value of n: ')
    try:
        n = int(user_n)
    except ValueError:
        try:
            float_n = float(user_n)
            n= int(round(float_n,0))
            print("Your input is rounded to ", m)
        except ValueError:
            ascii_values = [ord(char) for char in user_n]
            n = round(sum(ascii_values),0)
            print("Your input is converted to integer number: ", n)
            if type(n) != int:
                n = 0
                print("Your input is set as defalut value: ", n)

    file = open("raw_text.txt", "r")
    text = file.read()
    enc_text = encrypt(text, m, n)
    with open('encrypted_text.txt', 'w') as f:
        f.write("Encrypted text:\n")
        f.write(f"{enc_text}")
    dec_text = decrypt(enc_text, m, n)
    check_correctness(text, dec_text)

"""
Function for the Encryption
 This function encrypts the input text by applying custom shift logic to alphabetic characters.
Here lowercase and uppercase letters are processed differently.
Each half of the alphabet ('a'-'m', 'n'-'z', 'A'-'M', 'N'-'Z') shifted using formulas involving
the parameters m and n. Non-alphabetic characters remain unchanged.
"""
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

# Decryption Function
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

# Decryption Status Check
def check_correctness(original_text, dec_text):
    if original_text == dec_text:
        print("Correct decryption")
    else:
        print("Incorrect decryption")

if __name__=="__main__":
    main()