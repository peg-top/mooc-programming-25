# Write your solution here

def invert(dictionary: dict):

    lst = []

    for key, value in dictionary.items():
        lst.append([key, value])

    
    for el in lst:
        del dictionary[el[0]]
        dictionary[el[1]] = el[0]
    

# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# invert(s)
# print(s)