# Write your solution here
s = input("Please type in a sentence: ")

i = 0
isWord = True

while i < len(s):
    if isWord:
        print(s[i])
        isWord = False
    if s[i] == " ":
        isWord = True
    i += 1
    
