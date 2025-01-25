# Write your solution here

def most_common_character(s):

    most = 0
    c = ""

    for ch in s:
        if s.count(ch) > most:
            most = s.count(ch)
            c = ch
    
    return c


# first_string = "abcdbde"
# print(most_common_character(first_string))

# second_string = "exemplaryelementary"
# print(most_common_character(second_string))