# Write your solution here
wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

salary = wage * hours

print(f'Daily wages: {salary if day != "Sunday" else salary * 2} euros')