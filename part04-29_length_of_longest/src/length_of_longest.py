# Write your solution here

def length_of_longest(lst):
    size = 0
    for i in lst:
        if len(i) > size:
            size = len(i)
    return size