# Write your solution here

def create_tuple(x: int, y: int, z: int):

    lst = sorted([x, y, z])
    return (lst[0], lst[-1], sum(lst))



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))