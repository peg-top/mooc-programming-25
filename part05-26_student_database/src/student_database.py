# Write your solution here

def add_student(studentbase: dict, name: str):
    
    studentbase[name] = []
    

def cleaned_courses(courses: list):

    cleaned = {}

    for course, grade in courses:
        if grade != 0:
            if course not in cleaned:
                cleaned[course] = grade
            else:
                if cleaned[course] < grade:
                    cleaned[course] = grade
    
    cleaned_courses = []

    for key, value in cleaned.items():
        cleaned_courses.append([key, value])

    return cleaned_courses


def print_student(studenbase: dict, name: str):

    if name not in studenbase:
        print(f'{name}: no such person in the database')
    else:
        print(f'{name}:')

        completed_courses = cleaned_courses(studenbase[name])
    
        courses = len(completed_courses)

        if courses == 0:
            print(" no completed courses")
        else:
            grade = 0
            print(f' {courses} completed courses:')
            for course in completed_courses:
                print(f'  {course[0]} {course[1]}')
                grade += course[1]
            print(f' average grade {grade/courses}')


def add_course(studentbase: dict, name: str, course: tuple):
            
    studentbase[name].append(course)


def summary(studenbase):

    best_average_grade = (0, "")
    most_completed_courses = (0, "")

    print(f'students {len(studenbase)}')

    for name in studenbase:
        
        completed_courses =  cleaned_courses(studenbase[name])

        sum_of_grade = 0

        for course in completed_courses:
            sum_of_grade += course[1]

        average_grade = sum_of_grade / len(completed_courses)

        if  average_grade > best_average_grade[0]:
            best_average_grade = average_grade, name

        if len(completed_courses) > most_completed_courses[0]:
            most_completed_courses = len(completed_courses), name
    
    print(f'most courses completed {most_completed_courses[0]} {most_completed_courses[1]}')
    print(f'best average grade {best_average_grade[0]} {best_average_grade[1]}')



# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")