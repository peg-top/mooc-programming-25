# tee ratkaisu tänne
# wwite your solution here

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
    
print(f'{"name":30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}')

for id, student in students.items():
    exec_nbr = sum([int(x) for x in exercises[id]])
    exec_pts = exec_nbr//4
    exm_pts = sum([int(x) for x in points[id]])
    tot_pts = exec_pts + exm_pts

    grade = 0
    if 0 <= tot_pts <= 14:
        grade = 0
    elif 15 <= tot_pts <= 17:
        grade = 1
    elif 18 <= tot_pts <= 20:
        grade = 2
    elif 21 <= tot_pts <= 23:
        grade = 3
    elif 24 <= tot_pts <= 27:
        grade = 4
    elif tot_pts >= 28:
        grade = 5

    
    print(f'{student['first'] + " " + student['last']:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}')