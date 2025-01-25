# Write your solution here

def shortest(lst):
    word = lst[0]
    for i in lst:
        if len(word) >= len(i):
            word = i
    return word


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)

    print(shortest(['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']))