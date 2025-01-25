# Write your solution here
# You can test your function by calling it within the following block
def line(x, s):
    if len(s) == 0:
        s = "*"
    return(s[0] * x)

def spruce(size):
    print("a spruce!")
    for i in range(1, size + 1):
        print(line(size - i, " ") + line(2*i - 1, "*"))
    print(line(size - 1, " ") + line(1, "*"))

if __name__ == "__main__":
    spruce(5)