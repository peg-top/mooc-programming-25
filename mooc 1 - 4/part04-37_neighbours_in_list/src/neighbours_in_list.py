# Write your solution here

def longest_series_of_neighbours(lst):
    neighbours = []
    longest = []

    for i in lst:
        if len(neighbours) == 0:
            neighbours.append(i)
        elif abs(i - neighbours[-1]) == 1:
            neighbours.append(i)
        else:
            if len(neighbours) > len(longest):
                longest = neighbours
            neighbours = [i]
        
    
    if len(longest) > len(neighbours):
        return len(longest)
    return len(neighbours)

        


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    # my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))

    # print(longest_series_of_neighbours([1,2]))

    # print(longest_series_of_neighbours([1, 2, 3, 5, 6, 9, 10]))