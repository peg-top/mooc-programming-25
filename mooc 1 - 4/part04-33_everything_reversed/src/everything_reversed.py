# Write your solution here

def everything_reversed(lst: list):
    reversed = []
    for i in lst:
        reversed.append(i[::-1])
    return reversed[::-1]