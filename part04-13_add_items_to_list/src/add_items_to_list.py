# Write your solution here

length = int(input("How many items: "))

list = []

for i in range(length):
    new_element = int(input(f'Item {i+1}: '))
    list.append(new_element)

print(list)
