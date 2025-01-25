# write your solution here

if False:
    text = "We use ptython to make a spell checker"
else:
    text = input("Write text: ")

wordlist = []

with open("wordlist.txt") as new_file:

    for line in new_file:
        wordlist.append(line.strip())
    
    words = text.split(' ')

    new_str_lst = []

    for word in words:
        if word.lower() in wordlist:
            new_str_lst.append(word)
        else: 
            new_str_lst.append("*" + word + "*")

    new_str = ' '.join(new_str_lst)

    print(new_str)
