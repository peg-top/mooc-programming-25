# Write your solution here

if True:
    name = input("Whom should I sign this to: ")
    filename = input("Where shall I save it: ")
else:
    name = "Andrei"
    filename = "inscribed.txt"


with open(filename, "w") as w_file:
    w_file.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')