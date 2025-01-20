# Write your solution here

def formatted(lst):
    new_lst = []
    for i in lst:
        new_lst.append(f'{i:.2f}')
    return new_lst