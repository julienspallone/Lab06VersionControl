# decodes a password shifiting each digit in the password by 3
def password_decoder(encoded_password: str) -> str:
    password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        password += decoded_digit
    return password

# Main function
if __name__ == "__main__":

    # Menu
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        #user input
        option = input("Enter option: ")

        # Encode
        if option == "1":
            password = input("Enter your password to encode: ")
            encoded_password = password_encoder(password) # call the function
            print("Your password has been encoded and stored!")
        # Decode
        elif option == "2":
            decoded_password = password_decoder(encoded_password) 
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        # Quit
        elif option == "3":
            break