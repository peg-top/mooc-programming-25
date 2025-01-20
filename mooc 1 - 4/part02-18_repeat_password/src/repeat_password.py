password = input("Password: ")

while True:
    repeat_pass = input("Repeat password: ")
    if password != repeat_pass:
        print("They do not match!")
    else:
        print("User account created!")
        break