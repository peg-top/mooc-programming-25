# Write your solution here
s = input("Please type in a string: ")
ss = input("Please type in a substring: ")

first = s.find(ss)

if first != -1:
    # print(s[first + len(ss):])
    second = s[first + len(ss):].find(ss)
    if second != -1:
        print(f'The second occurrence of the substring is at index {first + len(ss)+second}.')
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")