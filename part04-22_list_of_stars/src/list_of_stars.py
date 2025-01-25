# Write your solution here

def list_of_stars(lst):
    for x in lst:
        print("*" * x)

if __name__ == "__main__":

    print(list_of_stars([1, 3, 1, 4]))