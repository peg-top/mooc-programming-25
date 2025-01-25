# Write your solution here



def is_integer(value):
    try:
        number = int(value)
        return True
    except ValueError:
        return False

def isStringValide(line):
    try:
        week_data, num_data = line.split(";")

        week_parts = week_data.split()
        if len(week_parts) != 2 or week_parts[0] != "week" or not is_integer(week_parts[1]):
            return False
        
        nums = [int(x) for x in num_data.split(",") if is_integer(x) and 1 <= int(x) <= 39]
        if len(set(nums)) != 7:
            return False
        # breakpoint()
        return True
    
    except (IndexError, ValueError):
        return False

def filter_incorrect():
    with open("lottery_numbers.csv") as lottery_filename, open("correct_numbers.csv", "w") as correct_file:
        for line in lottery_filename:
            if isStringValide(line):
                correct_file.write(line)

# filter_incorrect()