# Write your solution here

def list_sum(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        lst.append(lst1[i] + lst2[i])
    return lst

if __name__ == "__main__":
    print(list_sum([1], [1]))
    print(list_sum([1,2], [1,3]))
