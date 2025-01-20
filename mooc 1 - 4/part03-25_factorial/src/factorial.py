# Write your solution here
while True:

    n = int(input("Please type in a number: "))

    if n > 0:

        factorial = 1
        i = 1

        while i <= n:
            factorial *= i
            i += 1

        print(f'The factorial of the number {n} is {factorial}')
    else:
        print("Thanks and bye!")
        break
    