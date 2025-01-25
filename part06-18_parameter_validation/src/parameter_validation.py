# Write your solution here


# Please write a function named new_person(name: str, age: int), which creates and returns a tuple containing the data in the arguments. The first element should be the name and the second the age.

# If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.

# Invalid parameters in this case include:

# name is an empty string
# name contains less than two words
# name is longer than 40 characters
# age is a negative number
# age is greater than 150

def new_person(name: str, age: int):

    isNameCorrect = len(name.split()) > 1 and name != "" and len(name) < 40

    if not isNameCorrect:
        raise ValueError("Incorrect  name ", name)

    isAgeCorrect = 0 <= age <= 150

    if not isAgeCorrect:
        raise ValueError("Incorrect age: ", age)

    if isNameCorrect and isAgeCorrect:
        return (name, age)
    