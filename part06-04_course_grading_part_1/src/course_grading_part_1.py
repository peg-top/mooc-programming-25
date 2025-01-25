# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"


students = {}

with open(student_info) as students_file:

    for line in students_file:
        info = line.strip().split(";")
        if info[0] != "id":
            students[info[0]] = {"first": info[1], "last": info[2]}
        

exercises = {}

with open(exercise_data) as data_file:
    for line in data_file:
        info = line.strip().split(";")
        if info[0] != "id":
            exercises[info[0]] = info[1:]
    
    

for id, student in students.items():
    print(f'{student['first']} {student['last']} {sum([int(x) for x in exercises[id]])}')