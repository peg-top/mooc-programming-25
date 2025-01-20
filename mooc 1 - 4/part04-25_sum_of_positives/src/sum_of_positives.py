# Write your solution here

def sum_of_positives(lst):
    sum = 0
    for x in lst:
        if x > 0:
            sum += x
    return sum