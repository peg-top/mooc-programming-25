# Write your solution here

def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    numbers = {}

    for i in range(100):
        if i < 10:
            numbers[i] = ones[i]
        elif 10 <= i < 20:
            numbers[i] = teens[i - 10]
        else:
            tens_place = i // 10
            ones_place = i % 10
            if ones_place == 0:
                numbers[i] = tens[tens_place]
            else:
                numbers[i] = f"{tens[tens_place]}-{ones[ones_place]}"

    return numbers