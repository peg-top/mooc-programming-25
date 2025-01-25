# WRITE YOUR SOLUTION HERE:


# Please create a class named ListHelper which contains the following two class methods.

# greatest_frequency(my_list: list) returns the most common item on the list
# doubles(my_list: list) returns the number of unique items which appear at least twice on the list
# It should be possible to use these methods without creating an instance of the class. An example of how the methods could be used:

from collections import Counter

class ListHelper:

    @classmethod
    def greatest_frequency(self, my_list: list):
        return max([(x, my_list.count(x)) for x in my_list], key=lambda x: x[1])[0]
        
    @classmethod
    def doubles(self, my_list):
        return len([key for key, value in Counter(my_list).items() if value >= 2])
        
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))