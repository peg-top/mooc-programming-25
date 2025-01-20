# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):

    num = []

    for x in range(row_no, row_no + 3):
        for y in range(column_no, column_no + 3):
            n = sudoku[x][y]
            if n != 0:
                if n in num:
                    return False
                num.append(n)
    return True

if __name__ == "__main__":

#     sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
    [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # row 3
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
    [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ], ]
  
    print(block_correct(sudoku, 0, 3))

    # print(block_correct(sudoku, 0, 0))
    # print(block_correct(sudoku, 1, 2))