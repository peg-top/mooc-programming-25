# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(x, s):
    if len(s) == 0:
        s = "*"
    print(s[0] * x)

def shape(a, b, c, d):
    for i in range(a + 1):
        line(i, b)
    for i in range(c):
        line(a, d)


if __name__ == "__main__":
    shape(5, "x", 2, "o")