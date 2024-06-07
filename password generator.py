import string
import random

def generate_password(length):
    if length<= 0:
        return "Error: Password length must be greater than zero."
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print(" WELCOME to the Password Generator using Python. ")
    try:
        length = int(input(" Please enter the desired length of the password: "))
        password = generate_password(length)
        print(f" Generated password: {password}")
        print(" Thank You for using Password Generator. ")
        print(" Designed by ADARSHA JASH. ")
    except ValueError:
        print(" Invalid input! Please enter a valid number. ")
if __name__ == "__main__":
    main()