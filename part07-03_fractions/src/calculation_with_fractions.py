# Write your solution here

from fractions import Fraction

def fractionate(amount: int):
    x = []
    for i in range(amount):
        x.append(Fraction(1, amount))
    return x


# for p in fractionate(3):
#     print(p)

# print()

# print(fractionate(5))