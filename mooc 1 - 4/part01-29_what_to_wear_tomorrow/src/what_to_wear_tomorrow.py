# Write your solution here
temp = int(input("What is the weather forecast for tomorrow? "))
print("Temperature:", temp)
isRain = input("Will it rain (yes/no) ")
print("Wear jeans and a T-shirt")
if temp <= 20:
    print("I recommend a jumper as well")
if temp <= 10:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if isRain == "yes":
    print("Don't forget your umbrella!")