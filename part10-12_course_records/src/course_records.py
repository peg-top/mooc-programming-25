class Course:
    def __init__(self, name, grade, credits):
        self.name = name
        self.grade = grade
        self.credits = credits

    def update_grade(self, grade):
        if grade > self.grade:
            self.grade = grade

    def __str__(self):
        return f"{self.name} ({self.credits} cr) grade {self.grade}"


class StudyTracker:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name, grade, credits):
        if name in self.__courses:
            self.__courses[name].update_grade(grade)
        else:
            self.__courses[name] = Course(name, grade, credits)

    def get_course(self, name):
        return self.__courses.get(name, None)

    def statistics(self):
        total_courses = len(self.__courses)
        total_credits = sum(course.credits for course in self.__courses.values())
        # Средний балл с учётом кредитов
        mean_grade = (
            sum(course.grade * course.credits for course in self.__courses.values()) / total_credits
            if total_credits > 0 else 0
        )

        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade:.1f}")
        print("grade distribution")

        # Распределение оценок
        grade_counts = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for course in self.__courses.values():
            grade_counts[course.grade] += 1

        for grade in range(5, 0, -1):
            print(f"{grade}: {'x' * grade_counts[grade]}")


class StudyTrackerApplication:
    def __init__(self):
        self.__tracker = StudyTracker()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__tracker.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        course = self.__tracker.get_course(name)
        if course:
            print(course)
        else:
            print("no entry for this course")

    def statistics(self):
        self.__tracker.statistics()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()


# if __name__ == "__main__":
app = StudyTrackerApplication()
app.execute()
