class Board:

    def __init__(self):
        self.board = {
                "TL": " ", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "}

    def display_board(self):
        print(self.board["TL"] + "|" + self.board["TM"] \
            + "|" + self.board["TR"] + "|")
        print("-+" * 3)
        print(self.board["ML"] + "|" + self.board["MM"] \
            + "|" + self.board["MR"] + "|")
        print("-+" * 3)
        print(self.board["BL"] + "|" + self.board["BM"] \
            + "|" + self.board["BR"] + "|")

    def _is_valid_move(self, position):
        if self.board[position] is " ":
            return True
        return False

    def modify_board(self, position, type):
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None

    def is_winner(self, player):
        if self.board["TL"] == player.type and self.board["TM"] == player.type and self.board["TR"] == player.type or \
        self.board["ML"] == player.type and self.board["MM"] == player.type and self.board["MR"] == player.type or \
        self.board["BL"] == player.type and self.board["BM"] == player.type and self.board["BR"] == player.type or \
        self.board["TL"] == player.type and self.board["ML"] == player.type and self.board["BL"] == player.type or \
        self.board["TM"] == player.type and self.board["MM"] == player.type and self.board["BM"] == player.type or \
        self.board["TR"] == player.type and self.board["MR"] == player.type and self.board["BR"] == player.type or \
        self.board["TL"] == player.type and self.board["MM"] == player.type and self.board["BR"] == player.type or \
        self.board["BL"] == player.type and self.board["MM"] == player.type and self.board["TR"] == player.type:
            return True
        return False
