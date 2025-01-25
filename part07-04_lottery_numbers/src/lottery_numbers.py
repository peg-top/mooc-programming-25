# Write your solution here

from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    return sorted(set([randint(lower, upper) for x in range(amount)]))



# for number in lottery_numbers(7, 1, 40):
#     print(number)