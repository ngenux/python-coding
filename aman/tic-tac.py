def create_board():
    return [[" - " for x in range(3)] for y in range(3)]


def display_board(board):
    for i in range(3):
        print("---" * 4)
        print("|".join(board[i]))
    print("---" * 4)

def player_move(board, player, choice):

if __name__ == "__main__":
    board = create_board()
    display_board(board)
