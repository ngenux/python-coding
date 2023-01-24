def create_board():
    return [[" - " for x in range(3)] for y in range(3)]


def display_board(board):
    for i in range(3):
        print("---" * 4)
        print("|".join(board[i]))
    print("---" * 4)


def player_move(board, player_mark):
    row = int(input(f"Enter row for {player_mark}"))
    col = int(input(f"Enter col for {player_mark}"))
    if board[row][col] == " - ":
        board[row][col] == player_mark
        return True, row, col
    else:
        print("Wrong move, try again")
        return False, None, None


if __name__ == "__main__":
    board = create_board()
    display_board(board)
