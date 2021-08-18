MINIMUM_LENGTH = 10
password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print("Invalid Password")
    password = input("Password: ")
for char in password:
    print("*", end="")
