# Write your solution here

w = input("Word: ")

# Print the top border
print("*" * 30)

# Calculate padding for centering the word
before = (28 - len(w)) // 2
after = 28 - len(w) - before

# Print the word with padding
print(f'*{" " * before}{w}{" " * after}*')

# Print the bottom border
print("*" * 30)