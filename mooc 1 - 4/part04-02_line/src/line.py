# Write your solution here
# You can test your function by calling it within the following block

def line(x, s):
    if len(s) == 0:
        s = "*"
    print(s[0] * x)

if __name__ == "__main__":
    line(5, "x")