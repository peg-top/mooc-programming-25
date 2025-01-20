# Write your solution here

numbers = []

print("Please type in integer numbers. Type in 0 to finish.")

while True:

    number = int(input("Number: "))

    if len(numbers) != 0 and number == 0:
        break

    numbers.append(number)

if len(numbers) != 0:
    print(f'Numbers typed in {len(numbers)}')
    print(f'The sum of the numbers is {sum(numbers)}')
    print(f'The mean of the numbers is {sum(numbers) / len(numbers)}')
    print(f'Positive numbers {len([ x for x in numbers if x > 0])}')
    print(f'Negative numbers {len([ x for x in numbers if x < 0])}')


    