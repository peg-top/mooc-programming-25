# Write your solution here

def histogram(word):

    letters = {}

    for letter in word:
        if letter not in letters:
            letters[letter] = ""
        letters[letter] += "*"

    for key, value in letters.items():
        print(f'{key} {value}')


if __name__ == "__main__":

    histogram("statistically")