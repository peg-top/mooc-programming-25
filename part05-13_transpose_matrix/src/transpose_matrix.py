# Write your solution here

def transpose(matrix: list):

    size = len(matrix)

    transpose_matrix = []

    for y in range(size):

        transpose_row_matrix = []

        for x in range(size):
               
            transpose_row_matrix.append(matrix[x][y])
        
        transpose_matrix.append(transpose_row_matrix)

    matrix[:] = transpose_matrix


if __name__ == "__main__":

    a = [[1,2],[1,2]]
    transpose(a)
    print(a)