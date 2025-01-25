# Write your solution here

phone_book = {}

while True:

    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1:
        name = input("name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")
    elif command == 2:
        name = input("name: ")
        phone = input("number: ")
        phone_book[name] = phone
        print("ok!")
    elif command ==3:
        print("quitting...")
        break

# if __name__ == "__main__":
#     print()
