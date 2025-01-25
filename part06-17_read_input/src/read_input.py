# Write your solution here

def read_input(message, min, max):
    while True:
        try:
            num = int(input(message))
            if min < num < max:
                return num
        except ValueError:
            pass

        print(f'You must type in an integer between {min} and {max}')


# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)