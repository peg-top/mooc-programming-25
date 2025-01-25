# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):


    if 0 <= x < len(game_board) and 0 <= y < len(game_board):

        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
    
    return False



if __name__ == "__main__":

    # game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    # print(play_turn(game_board, 2, 0, "X"))

    # game_board = [['', '', 'X'], ['O', 'X', ''], ['', 'X', '']]
    # print(play_turn(game_board, 2, 2, "X"))

    game_board = [['O', '', 'X'], ['', '', ''], ['', '', '']]
    print(play_turn(game_board, 3, 0, "X"))
    
    print(game_board)