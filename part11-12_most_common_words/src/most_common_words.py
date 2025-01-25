# WRITE YOUR SOLUTION HERE:
from collections import Counter
import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as worfds_file:
        return {key: value for key, value in Counter(worfds_file.read().translate(str.maketrans("","", string.punctuation)).split()).items() if value >= lower_limit}

# text = '''
# List comprehension is an elegant way to define and create lists based on existing lists.
# List comprehension is generally more compact and faster than normal functions and loops for creating list.
# However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
# Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.'''

# print(text.strip().split())
if __name__ == "__main__":

    print(most_common_words("comprehensions.txt", 3))