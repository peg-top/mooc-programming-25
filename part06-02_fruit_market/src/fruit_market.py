# write your solution here

def read_fruits():
    with open("fruits.csv") as new_file:

        fruits = {}

        for line in new_file:
            line =  line.replace("\n", "")
            lst = line.split(";")
            fruits[lst[0]] = float(lst[1])

        return fruits


# print(read_fruits())