from Board import *
from Player import *
from Play import *


def start():
    play = Play()
    play.print_valid_entries()
    player = play.player1
    num = 9
    while num > 0:
        num -= 1
        play.printing_board()
        position = input("{} turn, what's your move? ".format(player))
        play.change_board(position, player.type)
        if play.won_game(player):
            print("{} is the Winner!".format(player))
            break
        else:
            player = play.change_turn(player)
    if num == 0:
        print("Game over! It's a tie!")


if __name__ == "__main__":
    start()
