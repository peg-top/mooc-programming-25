# Write your solution here
points = int(input("How many points [0-100]: "))

print("Grade: ", end = "")
if points <= 0 or points > 100:
    print("impossible!")
elif 90 <= points <= 100:
    print("5") 
elif 80 <= points < 90:
    print("4") 
elif 70 <= points < 80:
    print("3") 
elif 60 <= points < 70:
    print("2")
elif 50 <= points < 60:
    print("1")
else:
    print("fail")
