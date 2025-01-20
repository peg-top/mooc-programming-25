# Write your solution here

def palindromes(str):
    for i in range(len(str)):
        if str[i] != str[-(i + 1)]:
            return False
    return True

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":

while True:
    word = input("Please type in a palindrome: ")

    if palindromes(word):
        print(f'{word} is a palindrome!')
        break
    
    print("that wasn't a palindrome")
        
# block!
