# Write your solution here

def remove_smallest(numbers: list):

    min_index = 0

    for i in range(len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
    
    numbers.pop(min_index)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)