from Board import *
from Player import *

class Play:
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    def print_valid_entries(self):
        print("""
            TL - top left    | TM - top middle    | TR - top right
            ML - middle left | MM - center        | MR - middle right
            BL - bottom left | BM - bottom middle | BR - bottom right""")

    def printing_board(self):
        self.board.display_board()

    def change_turn(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player):
        return self.board.is_winner(player)

    def change_board(self, position, type):
        if self.board.modify_board(position, type) is not None:
            return self.board.modify_board(position, type)
        else:
            position = input("Not available position. Please, try again: ")
            return self.board.modify_board(position, type)
