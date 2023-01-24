import numpy as np
import sys

class Board(object):
    def __init__(self,size,default_char):
        self.size = size
        self.tile = default_char
        
    def get_board(self):
        board = [[self.tile]*self.size]*self.size
        return board
        
    def print_board(self):
        board = self.get_board()
        for row in board:
            sys.stdout.write("|")
            for tile in row:
                sys.stdout.write(str(tile) + "|")
            sys.stdout.write("\n")

if __name__ == "__main__":
    bo = Board(5,"*")
    print(bo.print_board())