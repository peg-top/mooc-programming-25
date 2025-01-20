# Write your solution here

def length(lst):
    counter = 0
    for _ in lst:  # Iterate through the list
        counter += 1
    return counter

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    print(length([]))
    result = length(my_list)
    print(result)