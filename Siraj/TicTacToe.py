import random

def print_board(board):
    print("The current Tic Tac Toe board looks like*************\n")
    for r in board:
        print("{}\t{}\t{}".format(r[0],r[1],r[2]))
        

def toss_markselection(players):
    print("There will be a toss as to decide who will start the game")
    toss = random.randint(0,99)%2
    
    print("{} will start the game first".format(players[toss]))
    print("{}:  Please select the mark of your choice from the following options.".format(players[toss]))
    playerMarks = {}
    playerMarks[players[toss]] = str(input())
    playerMarks[players[(toss+1)%2]] = input("{}: Please choose your mark ".format(players[(toss+1)%2]))
    
    while playerMarks[players[toss]] == playerMarks[players[(toss+1)%2]]:
        playerMarks[players[(toss+1)%2]] = input("{}: Please choose your mark which different than {} ".format(players[(toss+1)%2], players[(toss)]))
    
    return playerMarks

def main():
    print("Welcome to the game of tic tac toe")
    print("Please enter the two player names")
    players = ['_','_']
    players[0] = input('Player 1 Name:')
    players[1] = input('Player 2 Name:')

    board = [['_' for i in range(3)] for i in range(3)]

    print(toss_markselection(players))


main()
