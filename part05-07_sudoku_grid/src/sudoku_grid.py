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

def column_correct(sudoku: list, column_no: int):

    col = []

    for x in range(len(sudoku[0])):
        col.append(sudoku[x][column_no])


    for element in col:
        if col.count(element) > 1 and element != 0:
            return False
    return True

def row_correct(sudoku: list, row_no: int):

    for element in sudoku[row_no]:
        if sudoku[row_no].count(element) > 1 and element != 0:
            return False
    return True


def sudoku_grid_correct(sudoku: list):

    for x in range(len(sudoku)):
        if not (column_correct(sudoku, x) and row_correct(sudoku, x)):
            return False

    for x in range(0,len(sudoku),3):
        for y in range(0, len(sudoku), 3):
            if not(block_correct(sudoku, x, y)):
                return False
    
    return True
        
    




if __name__ == "__main__":

    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]]

    print(sudoku_grid_correct(sudoku2))