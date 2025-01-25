# write your solution here
def matrix_sum():
    with open("matrix.txt") as matrix_file:

        s = 0

        for line in matrix_file:
            line = line.replace("\n", "")
            row = line.split(',')
            s += sum([int(x) for x in row])
        
        return s

def matrix_max():
    with open("matrix.txt") as matrix_file:

        max = 0

        for line in matrix_file:
            line = line.replace("\n", "")
            row = line.split(',')

            for i in [int(x) for x in row]:
                if i > max:
                    max = i
        return max


def row_sums():
    with open("matrix.txt") as matrix_file:

        rows = []

        for line in matrix_file:
            line = line.replace("\n", "")
            row = line.split(',')
            rows.append(sum([int(x) for x in row]))
        return rows




# print(matrix_sum())
# print(matrix_max())