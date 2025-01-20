# Write your solution here
limit = int(input("Limit: "))

number = 1
sum_numbers = 0
sequence = ""

while sum_numbers < limit:
    sequence += str(number)
    sum_numbers += number
    if sum_numbers < limit:
        sequence += " + "
    number += 1

print("The consecutive sum:", sequence, "=", sum_numbers)