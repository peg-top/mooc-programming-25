# Copy here code of line function from previous exercise

def line(x, s):
    if len(s) == 0:
        s = "*"
    print(s[0] * x)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    for i in range(size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
