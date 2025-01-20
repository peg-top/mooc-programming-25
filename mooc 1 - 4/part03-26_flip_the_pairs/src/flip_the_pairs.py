# Write your solution here

n = int(input("Please type in a number: "))

i = 1

while i <= n:
    if i % 2 == 0:
        print(i - 1)
    else:
        if i+1 <= n:
            print(i + 1)
        else:
            print(i)
    i += 1
