# Write your solution here
def distinct_numbers(lst):
    new_lst = []
    for i in lst:
        if not i in new_lst:
            new_lst.append(i)
    return sorted(new_lst)

if __name__ == "__main__":
    print(distinct_numbers([1, 3, 3, 4, 19, 10]))