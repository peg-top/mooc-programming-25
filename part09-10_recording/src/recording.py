# WRITE YOUR SOLUTION HERE:

# Please create a class named Recording which models a single recording. The class should have one private variable: __length of type integer.

# Please implement the following:

# a constructor which takes the length as an argument
# a getter method length which returns the length of the recording
# a setter method which sets the length of the recording
# It should be possible to make use of the class as follows:

class Recording:

    def __init__(self, length: int):
        if length < 0:
            raise ValueError("The length is below zero")
        else:
            self.__length = length

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError("The length is below zero")

        self.__length = length


# the_wall = Recording(43)
# print(the_wall.length)
# the_wall.length = -1
# print(the_wall.length)