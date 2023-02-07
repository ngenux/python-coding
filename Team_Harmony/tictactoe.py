#### Updating function for Draw
# Updating function for P1 and P2 inputs

# Define an empty cell
empty_cell = '| |'

# This function maps the location entered by the Players to the 2-D board. 
# 1 is represented as [0,0] till 9 represented as [2,2]
def loc_map(loc):
    board_loc = 0
    if loc == 1:
        board_loc = board[0][0]
    if loc == 2:
        board_loc = board[0][1]
    if loc == 3:
        board_loc = board[0][2]
    if loc == 4:
        board_loc = board[1][0]
    if loc == 5:
        board_loc = board[1][1]
    if loc == 6:
        board_loc = board[1][2]
    if loc == 7:
        board_loc = board[2][0]
    if loc == 8:
        board_loc = board[2][1]
    if loc == 9:
        board_loc = board[2][2]
    return (board_loc)

# Function for getting the list of all available cells after each Player move
def current_available_cells():
    str_available_cell = ''
    for i in range(9):
        if loc_map(i+1) == empty_cell:
            str_available_cell = str_available_cell + str(i+1) + ','
    return (str_available_cell)

# Defines the empty cells in the 2-D board
# def board_available_cell(loc):
#     if loc == '| |':
#         return True 

# Representing the location chosen by Players (for either 'x' or 'o')
# The empty cells are replaced with either 'X' or 'O'
def boardstate(loc,txto,start):
    if start != 1:
        if loc == 1 and txto == 'x':
            board[0][0]=' X '
        elif loc == 2 and txto == 'x':
            board[0][1]=' X '
        elif loc == 3 and txto == 'x':
            board[0][2]=' X '
        elif loc == 4 and txto == 'x':
            board[1][0]=' X '
        elif loc == 5 and txto == 'x':
            board[1][1]=' X '
        elif loc == 6 and txto == 'x':
            board[1][2]=' X '
        elif loc == 7 and txto == 'x':
            board[2][0]=' X '
        elif loc == 8 and txto == 'x':
            board[2][1]=' X '
        elif loc == 9 and txto == 'x':
            board[2][2]=' X '
        if loc == 1 and txto == 'o':
            board[0][0]=' O '
        elif loc == 2 and txto == 'o':
            board[0][1]=' O '
        elif loc == 3 and txto == 'o':
            board[0][2]=' O '
        elif loc == 4 and txto == 'o':
            board[1][0]=' O '
        elif loc == 5 and txto == 'o':
            board[1][1]=' O '
        elif loc == 6 and txto == 'o':
            board[1][2]=' O '
        elif loc == 7 and txto == 'o':
            board[2][0]=' O '
        elif loc == 8 and txto == 'o':
            board[2][1]=' O '
        elif loc == 9 and txto == 'o':
            board[2][2]=' O '
            
        board_set = '\n',board[0],'\n',board[1],'\n',board[2]
    return (board)

# Defining the Win state
# There are 8 states for each 'X' and 'O' where Win state is achieved
def win_check():
    if (board[0][0] == ' X ' and board[0][1] == ' X ' and board[0][2] == ' X ') or \
       (board[1][0] == ' X ' and board[1][1] == ' X ' and board[1][2] == ' X ') or \
       (board[2][0] == ' X ' and board[2][1] == ' X ' and board[2][2] == ' X ') or \
       (board[0][0] == ' X ' and board[1][0] == ' X ' and board[2][0] == ' X ') or \
       (board[0][1] == ' X ' and board[1][1] == ' X ' and board[2][1] == ' X ') or \
       (board[0][2] == ' X ' and board[1][2] == ' X ' and board[2][2] == ' X ') or \
       (board[0][0] == ' X ' and board[1][1] == ' X ' and board[2][2] == ' X ') or \
       (board[0][2] == ' X ' and board[1][1] == ' X ' and board[2][0] == ' X ') or \
       (board[0][0] == ' O ' and board[0][1] == ' O ' and board[0][2] == ' O ') or \
       (board[1][0] == ' O ' and board[1][1] == ' O ' and board[1][2] == ' O ') or \
       (board[2][0] == ' O ' and board[2][1] == ' O ' and board[2][2] == ' O ') or \
       (board[0][0] == ' O ' and board[1][0] == ' O ' and board[2][0] == ' O ') or \
       (board[0][1] == ' O ' and board[1][1] == ' O ' and board[2][1] == ' O ') or \
       (board[0][2] == ' O ' and board[1][2] == ' O ' and board[2][2] == ' O ') or \
       (board[0][0] == ' O ' and board[1][1] == ' O ' and board[2][2] == ' O ') or \
       (board[0][2] == ' O ' and board[1][1] == ' O ' and board[2][0] == ' O '):
        return True
    else:
        return False

# Defining state for Draw
# No cells are empty
def draw_check():
    if (board[0][0] != empty_cell and board[0][1] != empty_cell and board[0][2] != empty_cell and \
        board[1][0] != empty_cell and board[1][1] != empty_cell and board[1][2] != empty_cell and \
        board[2][0] != empty_cell and board[2][1] != empty_cell and board[2][2] != empty_cell):
        return True
    else:
        return False
    
# Define initial state board
def init_state_board():
    board = [[empty_cell, empty_cell, empty_cell], [empty_cell, empty_cell, empty_cell], [empty_cell, empty_cell, empty_cell]]
    turn = 0
    return board,turn

# Format board
def format_board(player_move,boardstate,xo):
    form = '\n'+str(boardstate(player_move,xo,0)[0])+'\n'+str(boardstate(player_move,xo,0)[1])+'\n'+str(boardstate(player_move,xo,0)[2])
    return (form)

# Validate location number input
def validate_loc_num_input(player_move):
    if player_move == [1,9]:
        return True
    
def input_board():
    ipboard = [[' 1 ', ' 2 ', ' 3 '], [' 4 ', ' 5 ', ' 6 '], [' 7 ', ' 8 ', ' 9 ']]
    ipboard_set = '\n'+str(ipboard[0])+'\n'+str(ipboard[1])+'\n'+str(ipboard[2])
    return (ipboard_set)



def P1_inputs(turn,board):
    try:
        # Checking if turn is for Player 1 (X)
        while (turn % 2 == 0):
#             print('Please enter number from 1 to 9')
            cellno = current_available_cells()
            print('Available cells: ' + cellno)
            player_move = int(input("please enter move (P-1)X:").strip())

            validate_loc_num_input(player_move)
            if player_move == 1:
                board_loc = board[0][0]
            if player_move == 2:
                board_loc = board[0][1]
            if player_move == 3:
                board_loc = board[0][2]
            if player_move == 4:
                board_loc = board[1][0]
            if player_move == 5:
                board_loc = board[1][1]
            if player_move == 6:
                board_loc = board[1][2]
            if player_move == 7:
                board_loc = board[2][0]
            if player_move == 8:
                board_loc = board[2][1]
            if player_move == 9:
                board_loc = board[2][2]
#                 if player_move != [1-9]:
#                     print('Wrong location')

            if board_loc == empty_cell:
    #             boardstate(player_move,'x',0)
                
                print(format_board(player_move,boardstate,'x'))
#                 cellno = current_available_cells()
#                 print('Available cells: ' + cellno)
                if win_check():
                    print('P-1 WINS')
                    board,turn = init_state_board()
                    break
                    
                turn = turn + 1
        
                if draw_check():
                    print('GAME DRAWN')
                    board,turn = init_state_board()
                    break
        
            else:
                print('Place already taken. Try again..')
                cellno = current_available_cells()
                print('Available cells: ' + cellno)
    except:
        cellno = current_available_cells()
        print('Available cells: ' + cellno)
    return (board, turn)

def P2_inputs(turn,board):
    try:
        while (turn % 2 == 1):
            cellno = current_available_cells()
            print('Available cells: ' + cellno)
            player_move = int(input("Please enter move (P-2)O:").strip())
            validate_loc_num_input(player_move)

            if player_move == 1:
                board_loc = board[0][0]
            if player_move == 2:
                board_loc = board[0][1]
            if player_move == 3:
                board_loc = board[0][2]
            if player_move == 4:
                board_loc = board[1][0]
            if player_move == 5:
                board_loc = board[1][1]
            if player_move == 6:
                board_loc = board[1][2]
            if player_move == 7:
                board_loc = board[2][0]
            if player_move == 8:
                board_loc = board[2][1]
            if player_move == 9:
                board_loc = board[2][2]

            if board_loc == empty_cell:
                print(format_board(player_move,boardstate,'o'))

                if win_check():
                    print('P-2 WINS')
                    board,turn = init_state_board()
                    break

                turn = turn + 1
        
                if draw_check():
                    print('GAME DRAWN')
                    board,turn = init_state_board()
                    break
            else:
                print('Place already taken. Try again..')
                cellno = current_available_cells()
                print('Available cells: ' + cellno)
    except:
        cellno = current_available_cells()
        print('Available cells: ' + cellno)
    return (board, turn)
    
# ------------------------------------------------------------------------
# Start main
new_game ='y'
while new_game == 'y' or new_game == 'Y':
    new_game = str(input("Do you want to start a new game (y to play. press any other key to exit)?: ").strip())
    if new_game == 'y' or new_game == 'Y':
        print('Welcome to Tic-Tac-Toe')
        print('The inputs used are represented in the board as below')
        # New game starts here
        ipboard = input_board()
        print(ipboard)
        
        board,turn = init_state_board()
        while turn >= 0: 
            board, turn = P1_inputs(turn,board)
            if turn == 0:
                break
#             print(turn)
            
            # Checking if turn is for Player 2 (O)
            board, turn = P2_inputs(turn,board)
            if turn == 0:
                break
#             print(turn)
        else:
            break
    else:
        print('Thanks for playing')