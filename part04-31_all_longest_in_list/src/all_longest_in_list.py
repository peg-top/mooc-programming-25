# Write your solution here

def all_the_longest(lst):
    
    longest_word = 0

    for i in lst:
        if len(i) >= longest_word:
            longest_word = len(i)

    longest_list = []

    for i in lst:
        if longest_word == len(i):
            longest_list.append(i)

    return longest_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']