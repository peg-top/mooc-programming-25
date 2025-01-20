# Write your solution here
students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))
full_groups = students//size
print(f'Number of groups formed: {full_groups if students%size == 0 else full_groups + 1}')