# Write your solution here

def calculate_grade(total_points, exam_points):
    if exam_points < 10:
        return 0
    elif total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

def main():
    results = []
    
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        exam_points, exercises = map(int, user_input.split())
        exercise_points = exercises // 10  # Convert exercises to points
        total_points = exam_points + exercise_points
        results.append((exam_points, exercise_points, total_points))

    print("Statistics:")

    if results:
        total_points_sum = sum(result[2] for result in results)
        average = total_points_sum / len(results)
        print(f"Points average: {average:.1f}")

        passes = [result for result in results if calculate_grade(result[2], result[0]) > 0]
        pass_percentage = (len(passes) / len(results)) * 100
        print(f"Pass percentage: {pass_percentage:.1f}")

        print("Grade distribution:")
        grade_counts = [0] * 6
        for result in results:
            grade = calculate_grade(result[2], result[0])
            grade_counts[grade] += 1

        for grade in range(5, -1, -1):
            print(f"  {grade}: {'*' * grade_counts[grade]}")

main()

# if __name__ == "__main__":
    # main()