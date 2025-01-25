# Write your solution here

def find_words(search_term: str):

    words = []

    with open("words.txt") as words_file:
        for line in words_file:
            words.append(line.strip())

    search_words = []

    if "." in search_term:
        filtered_words = [word for word in words if len(word) == len(search_term)]

        for word in filtered_words:
            correct_letters = 0
            for i in range(len(word)):
                if search_term[i] == word[i] or search_term[i] == ".":
                    correct_letters += 1
            if correct_letters == len(word):
                search_words.append(word)
    
    elif search_term.startswith("*"):
        search_words = [word for word in words if word.endswith(search_term[1:])]

    elif search_term.endswith("*"):
        search_words = [word for word in words if word.startswith(search_term[:-1])]

    else:
        search_words = [word for word in words if word == search_term]

    return(search_words)


# read_file("words.txt")
# print(a[0])
# print(len(a))

# find_words("ca.")

# find_words(".ca.")
# find_words(".c.a.")

# print(find_words("*hed"))
# find_words("abu*")

# print(find_words("aah"))

