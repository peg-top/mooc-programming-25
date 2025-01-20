# Write your solution here

def longest(strings: list):
    long = ""
    for el in strings:
        if len(el) >= len(long):
            long = el
    return long