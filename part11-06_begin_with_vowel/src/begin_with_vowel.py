# WRITE YOUR SOLUTION HERE:

# Please write a function named begin_with_vowel(words: list) which takes 
# a list of strings as its argument.

# The function should use a list comprehension technique to create 
# and return a new list, containing only those words from the original 
# list which begin with a vowel (a, e, i, o, u). Both lowercase and uppercase 
# letters should be accepted.

# The maximum length of the function is two lines of code, including the header 
# line beginning with the def keyword.

# An example of the function in use:
# VOWELS = "aeiou""


def begin_with_vowel(words: list):
    return [w for w in words if w[0].lower() in "aeiou"]
   

# word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
# for vowelled in begin_with_vowel(word_list):
#     print(vowelled)