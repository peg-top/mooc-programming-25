# Write your solution here

def squared(s, size):
    t = 0
    line = ""
    while t < size * size:
        line += s[t]
        s += s[t]
        t += 1
        if t % size == 0:
            print(line)
            line = ""
            

if __name__ == "main":

    squared("aybabtu", 5)   