def password_encoder(password: str) -> str:
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def password_decoder(encoded_password: str) -> str:
    password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        password += decoded_digit
    return password

if __name__ == "__main__":


    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Enter option: ")

        if option == "1":
            password = input("Enter your password to encode: ")
            encoded_password = password_encoder(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            decoded_password = password_decoder(encoded_password)
            print(f"The encoded password is {password_encoder}, and the original password is {decoded_password}")
        elif option == "3":
            break