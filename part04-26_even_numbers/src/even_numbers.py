# Write your solution here

def even_numbers(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    return even_list