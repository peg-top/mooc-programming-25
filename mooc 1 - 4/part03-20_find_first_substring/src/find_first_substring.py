# Write your solution here

s = input("Please type in a word: ")
c = input("Please type in a character: ")

i = s.find(c)

if i + 2 < len(s):
    print(s[i:i+3])
    
