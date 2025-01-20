# Write your solution here

def most_common_character(str):
    
    common = " "
    
    for i in str:
        if str.count(i) > str.count(common):
            common = i

    return common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))