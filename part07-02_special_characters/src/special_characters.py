# Write your solution here
import string

def separate_characters(my_string: str):
    
    return (
        "".join([x for x in list(my_string) if x in string.ascii_letters]),
        "".join([x for x in list(my_string) if x in string.punctuation]),
        "".join([x for x in list(my_string) if x not in string.ascii_letters and x not in string.punctuation])
    )



# parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(parts[0])
# print(parts[1])
# print(parts[2])