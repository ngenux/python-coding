def boardstate(loc,txto):
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    if loc == 1 and txto == 'x':
        board = [["X", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    elif loc == 2 and txto == 'x':
        board = [["-", "X", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    elif loc == 3 and txto == 'x':
        board = [["-", "-", "X"], ["-", "-", "-"], ["-", "-", "-"]]
    elif loc == 4 and txto == 'x':
        board = [["-", "X", "-"], ["X", "-", "-"], ["-", "-", "-"]]
    elif loc == 5 and txto == 'x':
        board = [["-", "X", "-"], ["-", "X", "-"], ["-", "-", "-"]]
    elif loc == 6 and txto == 'x':
        board = [["-", "X", "-"], ["-", "-", "X"], ["-", "-", "-"]]
    elif loc == 7 and txto == 'x':
        board = [["-", "X", "-"], ["-", "-", "-"], ["X", "-", "-"]]
    elif loc == 8 and txto == 'x':
        board = [["-", "-", "-"], ["-", "-", "-"], ["-", "X", "-"]]
    elif loc == 9 and txto == 'x':
        board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "X"]]
    if loc == 1 and txto == 'o':
        board = [["O", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    elif loc == 2 and txto == 'o':
        board = [["-", "O", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    elif loc == 3 and txto == 'o':
        board = [["-", "-", "O"], ["-", "-", "-"], ["-", "-", "-"]]
    elif loc == 4 and txto == 'o':
        board = [["-", "X", "-"], ["O", "-", "-"], ["-", "-", "-"]]
    elif loc == 5 and txto == 'o':
        board = [["-", "X", "-"], ["-", "O", "-"], ["-", "-", "-"]]
    elif loc == 6 and txto == 'o':
        board = [["-", "X", "-"], ["-", "-", "O"], ["-", "-", "-"]]
    elif loc == 7 and txto == 'o':
        board = [["-", "X", "-"], ["-", "-", "-"], ["O", "-", "-"]]
    elif loc == 8 and txto == 'o':
        board = [["-", "-", "-"], ["-", "-", "-"], ["-", "O", "-"]]
    elif loc == 9 and txto == 'o':
        board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "O"]]
    return board
