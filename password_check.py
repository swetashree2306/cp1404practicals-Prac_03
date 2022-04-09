"""
CP1404 - Practical
Program to check password length should be at least 6 character and print asterisks
"""


def main():
    password = get_password()
    while len(password) < 6:
        print("Password should not be less then 6 characters")
        password = get_password()
    else:
        print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter your password:")
    return password


main()
