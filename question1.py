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
                shift_value = n*m
                remaining_shift = (shift_value-(ord('z')-ord(char))) % 26
                if remaining_shift < 0:
                    transformed_char = chr(ord('z')+remaining_shift)
                else:
                    transformed_char = chr(ord('a')-1+remaining_shift)
                encrypted_text += transformed_char

            # if the letter is in second half (n-z)
            else:
                shift_value = n+m
                remaining_shift = (shift_value-(ord(char)-ord('a'))) % 26
                if remaining_shift < 0:
                    transformed_char = chr(ord('a')+remaining_shift)
                else:
                    transformed_char = chr(ord('z')+1-remaining_shift)
                encrypted_text += transformed_char

        # logic for uppercase letters
        elif 'A' <= char <= 'Z':
            # if the letter is in first half (A-M)
            if char<='M':
                shift_value = n
                remaining_shift = (shift_value-(ord(char)-ord('A'))) % 26
                if remaining_shift < 0:
                    transformed_char = chr(ord('A')+remaining_shift)
                else:
                    transformed_char = chr(ord('Z')+1-remaining_shift)
                encrypted_text += transformed_char

            # if the letter is in first half (N-Z)    
            else:
                shift_value = m**2
                remaining_shift = (shift_value-(ord('Z')-ord(char))) % 26
                if remaining_shift < 0:
                    transformed_char = chr(ord('Z')+remaining_shift)
                else:
                    transformed_char = chr(ord('A')-1+remaining_shift)
                encrypted_text += transformed_char

        # logic for all other characters and numbers
        else:
            encrypted_text += char
    return encrypted_text

if __name__=="__main__":
    main()