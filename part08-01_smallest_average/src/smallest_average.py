# Write your solution here
# Please write a function named smallest_average(person1: dict, person2: dict, person3: dict), which takes three dictionary objects as its arguments.

# Each dictionary object contains values mapped to the following keys:

# "name": The name of the contestant
# "result1": the first result of the contestant (an integer between 1 and 10)
# "result2": the second result of the contestant (as above)
# "result3": the third result of the contestant (as above)
# The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. The return value should be the entire dictionary object containing the contestant's information.

# You may assume there will be no ties, i.e. a single contestant will have the smallest average result.

# An example of the function in action:

# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))
# Sample output
# {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}

def smallest_average(person1: dict, person2: dict, person3: dict):

    smallest_dict = {}
    smallest = 100

    for person in [person1, person2, person3]:
        if person["result1"] + person["result2"] +  person["result3"] / 3 < smallest:
            smallest = person["result1"] + person["result2"] +  person["result3"] / 3
            smallest_dict = person
    return smallest_dict

# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))