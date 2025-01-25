# Write your solution here

phone_book = {}

while True:

    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1:
        name = input("name: ")
        if name in phone_book:
            for phone in phone_book[name]:
                print(phone)
        else:
            print("no number")
    elif command == 2:
        name = input("name: ")
        phone = input("number: ")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(phone)
        print("ok!")
    elif command ==3:
        print("quitting...")
        break