def board_available_cell(loc):
    if loc == 'e':
        return True 

def boardstate(loc,txto,start):
    if start != 1:
        if loc == 1 and txto == 'x':
            board[0][0]='X'
        elif loc == 2 and txto == 'x':
            board[0][1]='X'
        elif loc == 3 and txto == 'x':
            board[0][2]='X'
        elif loc == 4 and txto == 'x':
            board[1][0]='X'
        elif loc == 5 and txto == 'x':
            board[1][1]='X'
        elif loc == 6 and txto == 'x':
            board[1][2]='X'
        elif loc == 7 and txto == 'x':
            board[2][0]='X'
        elif loc == 8 and txto == 'x':
            board[2][1]='X'
        elif loc == 9 and txto == 'x':
            board[2][2]='X'
        if loc == 1 and txto == 'o':
            board[0][0]='O'
        elif loc == 2 and txto == 'o':
            board[0][1]='O'
        elif loc == 3 and txto == 'o':
            board[0][2]='O'
        elif loc == 4 and txto == 'o':
            board[1][0]='O'
        elif loc == 5 and txto == 'o':
            board[1][1]='O'
        elif loc == 6 and txto == 'o':
            board[1][2]='O'
        elif loc == 7 and txto == 'o':
            board[2][0]='O'
        elif loc == 8 and txto == 'o':
            board[2][1]='O'
        elif loc == 9 and txto == 'o':
            board[2][2]='O'
    return (board)

def win():
    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or \
       (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or \
       (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or \
       (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or \
       (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or \
       (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or \
       (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or \
       (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') or \
       (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or \
       (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or \
       (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or \
       (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or \
       (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or \
       (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or \
       (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or \
       (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return True
    else:
        return False

# Define initial state board
board = [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]

while 1:
    player_move = int(input("please enter move (P1)x:").strip())
    if board[2][2]!='e':
        boardstate(player_move,'x',0)
    else:
        print('Wrong move')
    print(boardstate(player_move,'x',0))
#     print(board)
    player_move = int(input("please enter move (P2)o:").strip())
    if board[2][2]!='e':
        print(boardstate(player_move,'o',0))
    else:
        print('Wrong move')
#     print(board)