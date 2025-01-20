# Write your solution here
str1 = input("Please type in the 1st word: ")
str2 = input("Please type in the 1st word: ")

if str1 == str2:
    print("You gave the same word twice.")
else:
    print(f'{str1 if str1>str2 else str2} comes alpabetically last.')