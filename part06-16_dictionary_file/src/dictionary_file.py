# Write your solution here


filename = "dictionary.txt"


while True:

    words = {}

    with open(filename) as words_file:

        for line in words_file:
            en_word, fi_word = line.strip().split(";")
            words[en_word] = fi_word

    
    print("1 - Add word, 2 - Search, 3 - Quit")
    command = int(input("Function: "))


    if command == 1:
        fi_word = input("The word in Finnish: ")
        en_word = input("The word in English: ")

        with open(filename, "a") as words_file:
            words_file.write(f'{en_word};{fi_word}\n')

        print("Dictionary entry added")

    elif command == 2:
        
        search_word =  input("Search term: ")

        for en_word, fi_word in words.items():
            if search_word in en_word:
                print(f'{fi_word} - {en_word}')
            else:
                if search_word in fi_word:
                    print(f'{fi_word} - {en_word}')
            

    elif command == 3:
        print("Bye!")
        break