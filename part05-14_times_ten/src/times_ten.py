# Write your solution here


def times_ten(start_index: int, end_index: int):
    
    ten = {}
    
    for key in range(start_index, end_index + 1):
        ten[key] = key * 10

    return ten
    