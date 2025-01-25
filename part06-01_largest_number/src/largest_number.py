# write your solution here

def largest():

    with open("numbers.txt") as new_file:

        biggest = 0

        for line in new_file:
            num = int(line)
            if num > biggest:
                biggest = num
    return biggest

# print(largest())
    