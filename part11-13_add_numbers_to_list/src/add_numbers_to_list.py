# WRITE YOUR SOLUTION HERE:

def add_numbers_to_list(lst):

    if len(lst) % 5 == 0:
        return
    else:
        lst.append(lst[-1] + 1)
        add_numbers_to_list(lst)

if __name__ == "__main__":
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)