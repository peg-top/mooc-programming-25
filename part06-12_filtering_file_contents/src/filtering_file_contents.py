# Write your solution here

def parse_solution(solution: str) -> tuple:

    operand_index = solution.find("+")

    if operand_index == -1:
        operand_index = solution.find("-")
  
    return (int(solution[:operand_index]), int(solution[operand_index + 1:]), solution[operand_index])    


def filter_solutions():
    with open("solutions.csv") as solution_file:

        solutions = []

        for line in solution_file:
            name, solution, answer = line.split(";")
            solutions.append([name, parse_solution(solution), int(answer)])

        correct = []
        incorrect = []

        for solution in solutions:

            name, sol, answer = solution[0], solution[1], solution[2]
            
            if sol[2] == "+":
                if sol[0] + sol[1] == answer:
                    correct.append(f'{name};{sol[0]}+{sol[1]};{answer}\n')
                else:
                    incorrect.append(f'{name};{sol[0]}+{sol[1]};{answer}\n')
            elif sol[2] == "-":
                if sol[0] - sol[1] == answer:
                    correct.append(f'{name};{sol[0]}-{sol[1]};{answer}\n')
                else:
                    incorrect.append(f'{name};{sol[0]}-{sol[1]};{answer}\n')

        with open("correct.csv", "w") as correct_file:

            for c in correct:
                correct_file.write(c)

        with open("incorrect.csv", "w") as incorrect_file:

            for c in incorrect:
                incorrect_file.write(c)
        

    




if __name__ == "__main__":
    filter_solutions()
