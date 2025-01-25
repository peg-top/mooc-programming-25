# Write your solution here

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

        


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

    


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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)