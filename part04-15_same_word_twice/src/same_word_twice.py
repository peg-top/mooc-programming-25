# Write your solution here

list = []

while True:

    word = input("World: ")
    
    if word in list:
        print(f'You typed in {len(list)} different words')
        break
    
    list.append(word)