def encode(old_pass):
    encoder_val = 3
    encoded_pass = ''
    for item in old_pass:
        new_val = str((int(item) + encoder_val) % 10)
        encoded_pass += new_val
    return encoded_pass


def decode(encoded_password: str) -> str:
    decode_val = 3
    decoded_password = ''
    for item in encoded_password:
        decoded_val = str((int(item) - decode_val) % 10)
        decoded_password += decoded_val
    return decoded_password


encode_decode = True

if __name__ == '__main__':
    while encode_decode:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        user_selection = int(input("Please enter an option: "))
        if user_selection == 1:
            old_pass = input("Please enter your password to encode: ")
            stored_pass = encode(old_pass)
            print("Your password has been encoded and stored!\n")
        elif user_selection == 2:
            pass
        elif user_selection == 3:
            break




