# Write your solution here
def chessboard(size):
    x = 0
    while x < size:
        y = 0
        line = ""
        while y < size:
            if (x + y) % 2 == 0:
                line += "1"
            else:
                line += "0"
            y += 1
        print(line) 
        x += 1

# Testing the function
if __name__ == "__main__":
    chessboard(5)
