# Write your solution here

list = []

while True:

    print("The list is now", list)

    command = input("a(d)d, (r)emove or e(x)it: ").lower()

    if command == "d":
        list.append(len(list) + 1)
    elif command == "r":
        if len(list) != 0:
            list.pop()
    elif command == "x":
        break

print("Bye!")