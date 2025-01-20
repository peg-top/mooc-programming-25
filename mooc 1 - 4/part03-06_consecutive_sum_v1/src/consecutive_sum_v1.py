# Write your solution here

limit = int(input("Limit: "))

number = 0
sum_numbers = 0

while sum_numbers < limit:
    sum_numbers += number
    number += 1

print(sum_numbers)

