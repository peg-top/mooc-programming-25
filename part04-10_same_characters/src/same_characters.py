# Write your solution here
def same_chars(s, a, b):
    return len(s) > a and len(s) > b and s[a] == s[b]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))