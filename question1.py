def main():
    text = 'Hello world'
    print(text)
    enc_text = encrypt(text, n=15, m=15)
    print(enc_text)

def encrypt(text, n, m):
    encrypted_text = ''
    for char in text:
        if 'a' <= char <= 'z':
            if char<='m':
                shift_value = n*m
                transformed_char = chr(ord(char)+shift_value)
                encrypted_text += transformed_char
            else:
                shift_value = n+m
                transformed_char = chr(ord(char)-shift_value)
                encrypted_text += transformed_char
        elif 'A' <= char <= 'Z':
            if char<='m':
                shift_value = n
                transformed_char = chr(ord(char)-shift_value)
                encrypted_text += transformed_char
            else:
                shift_value = m^2
                transformed_char = chr(ord(char)+shift_value)
                encrypted_text += transformed_char
        else:
            encrypted_text += char
    return encrypted_text

if __name__=="__main__":
    main()