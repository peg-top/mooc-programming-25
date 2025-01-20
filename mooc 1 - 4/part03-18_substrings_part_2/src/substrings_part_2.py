# Write your solution here
s = input("Please write in a string: ")

i = len(s)

while i > 0 :
    print(s[i - 1:len(s)])
    i -= 1