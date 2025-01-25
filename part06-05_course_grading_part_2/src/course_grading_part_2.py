# wwite your solution here
# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"


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

points = {}

with open(exam_points) as points_file:

    for line in points_file:
        info = line.strip().split(";")
        if info[0] != "id":
            points[info[0]] = info[1:]
    
    

for id, student in students.items():
    student_point = sum([int(x) for x in exercises[id]])//4 + sum([int(x) for x in points[id]])
    grade = 0
    if 0 <= student_point <= 14:
        grade = 0
    elif 15 <= student_point <= 17:
        grade = 1
    elif 18 <= student_point <= 20:
        grade = 2
    elif 21 <= student_point <= 23:
        grade = 3
    elif 24 <= student_point <= 27:
        grade = 4
    elif student_point >= 28:
        grade = 5

    print(f'{student['first']} {student['last']} {grade}')