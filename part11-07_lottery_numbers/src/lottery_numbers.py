# WRITE YOUR SOLUTION HERE:
# Please write a class named LotteryNumbers which takes the week number
# (an integer value) and a list of seven integers as its constructor arguments.
# The list should contain the correct lottery numbers for the given week.

# Please also write a method named number_of_hits(numbers: list) which takes
# a list of integers as its argument. The method returns the number of correct
#  entries in the parameter list.

# The method should use a list comprehension to achieve this. The maximum
# length of the function is two lines of code, including the header line
# beginning with the def keyword.

# An example of how the class and function are used:

class LotteryNumbers:

    def __init__(self, week, numbers):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, lst):
        return sum([1 for x in lst if x in self.numbers])

    def hits_in_place(self, numbers):
        return [x if x in self.numbers else -1 for x in numbers]

if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))