# Write your solution here

def no_vowels(str):

    vowels = ['a', 'e', 'i', 'o', 'u']
    s = ""
    for i in str:
        if i not in vowels:
            s += i
    return s

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))