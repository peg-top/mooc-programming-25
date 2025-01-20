# Write your solution here
number = int(input("Number: "))

# if number % 3 == 0:
#     print("Fizz", end="")
# if number % 5 == 0:
#     print("Buzz", end="\n")

print(f'{"Fizz" if number % 3 == 0 else ""}{"Buzz" if number % 5 == 0 else ""}')