# Write your solution here

def great(a, b):
    return a >= b

def greatest_number(a, b, c):
    if great(a, b) and great(a, c):
        return a
    elif great(b, a) and great(b, c):
        return b
    else:
        return c
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)