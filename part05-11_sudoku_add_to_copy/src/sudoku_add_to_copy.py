# Write your solution here

def print_sudoku(sudoku: list):  

    size = len(sudoku)
    
    for x in range(size):
        row_str = ""
        
        for y in range(size):
            element = sudoku[x][y]
            row_str += str(element) if element != 0 else "_"            
            if y + 1 != size:
                row_str += " "
            if (y + 1) % 3 == 0:
                row_str += " "
        print(row_str)
        if (x + 1) % 3 == 0:
            print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):

    copy_sudoku = []
    size = len(sudoku)

    for x in range(size):
        copy_row_sudoku = []
        for y in range(size):
            if x == row_no and y == column_no:
                copy_row_sudoku.append(number)
            else:
                copy_row_sudoku.append(sudoku[x][y])
        copy_sudoku.append(copy_row_sudoku)
    
    return copy_sudoku

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)