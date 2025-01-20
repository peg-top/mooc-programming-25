# Write your solution here
str = []

while True:
    new_word = input("Please type in a word: ")

    if len(str) != 0 and (new_word == "end" or new_word == str[-1]):
        break
    str.append(new_word)

print(" ".join(str))