# WRITE YOUR SOLUTION HERE:

# Please write a function named filter_forbidden(string: str, forbidden: str)
# which takes two strings as its arguments. The function should return a new
# version of the first string. It should not contain any characters from
# the second string.

# The function should be implemented using list comprehensions. The maximum
# length of the function is three lines of code, including the header
# line beginning with the def keyword.

# Please have a look at the example below.

def filter_forbidden(string, forbidden):
    return "".join([ch for ch in string if ch not in forbidden])


if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)