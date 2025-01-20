# Write your solution here

# Write your solution here

w = input("Please type in a word: ")
c = input("Please type in a character: ")

while len(w) > 0:
    
    i = w.find(c)
    
    if i == -1:
        break

    if i + 2 < len(w):
        print(w[i:i+3])
    
    w = w[i+1:]