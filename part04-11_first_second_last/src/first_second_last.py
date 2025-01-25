# Write your solution here

def first_word(s):
    i = s.find(" ")
    if i != -1:
        return s[:i]
    return s

def second_word(s):
    i = s.find(" ")
    if i != -1:
        return first_word(s[i+1:])


def last_word(s):
    last_space = 0
    for i in range(len(s)):
        if s[i] == " ":
            last_space = i
    return s[last_space+1:]

        


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"

    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))