# Write your solution here

a = input("Please type in string 1: ")
b = input("Please type in string 2: ")

if len(a) == len(b):
    print("The strings are equally long")
elif len(a) > len(b):
    print(f'{a} is longer')
else:
    print(f'{b} is longer')