from rich.text import Text
from rich.markdown import Markdown
from rich import print
import rich
import random
import sys
import time


def intro_message():

    print(
        Markdown(
            """
    ````
      ________________            _________   ______            __________  ______
     /_  __/  _/ ____/           /_  __/   | / ____/           /_  __/ __ \/ ____/
      / /  / // /      ______     / / / /| |/ /      ______     / / / / / / __/   
     / / _/ // /___   /_____/    / / / ___ / /___   /_____/    / / / /_/ / /___   
    /_/ /___/\____/             /_/ /_/  |_\____/             /_/  \____/_____/   
                                                                              
    ```
    Developed by Team ENIGMA
    """
        )
    )
    print("\n")
    print("Let the Fun begins.. \U0001f44d \n")


def welcome_players(players):
    print(
        # Text("\n"),
        Text("Welcome to the game ", style="blue"),
        Text(players[0].upper(), style="red"),
        Text(" and ", style="blue"),
        Text(players[1].upper(), style="green"),
        Text("!", style="blue"),
    )


def game_rules():
    print("\nRULES OF THE GAME:\n")
    print(
        "+ Person rolling the larger number on the die makes the first move and choose his mark 'X' or 'O'."
    )
    print("+ Each player will get a chance to mark his position on the board in turns.")
    print(
        "+ The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner."
    )
    print(
        "+ When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n"
    )


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
        board[row][col] == "player_mark"
        return True, row, col
    else:
        print("Wrong move, try again")
        return False, None, None


def animate_rolling():
    time.sleep(0.5)
    sys.stdout.write("\rrolling |")
    time.sleep(0.5)
    sys.stdout.write("\rrolling /")
    time.sleep(0.5)
    sys.stdout.write("\rrolling -")
    time.sleep(0.5)
    sys.stdout.write("\rrolling \\")
    time.sleep(0.5)
    sys.stdout.write("\rrolling |")
    time.sleep(0.5)
    sys.stdout.write("\rrolling /")
    time.sleep(0.5)
    sys.stdout.write("\rrolling -")
    time.sleep(0.5)
    sys.stdout.write("\rrolling \\")
    sys.stdout.write("\rDone!     \n")


def roll_dice(players):
    animate_rolling()
    player1_roll, player2_roll = random.randint(1, 6), random.randint(1, 6)
    print(f"{players[0]} has rolled {player1_roll}")
    print(f"{players[1]} has rolled {player2_roll}")

    if player1_roll == player2_roll:
        print("Oops its a tie.\n")
        roll_dice(players)
    elif player1_roll > player2_roll:
        print(f"{players[0]} can start the game")
        return players[0]
    else:
        print(f"{players[1]} can start the game")
        return players[1]


def start_rolling(players):
    game_start_response = input("Ready to start the game? (yes/no): ")
    if game_start_response.lower() == "yes":
        return roll_dice(players)
    elif game_start_response.lower() == "no":
        exit_question = input("Do you want to exit? (yes/no): ")
        if exit_question.lower() == "yes":
            print("Exiting Game.. Bye!")
            quit()
        elif exit_question.lower() == "no":
            game_start_response
            start_rolling(players[0], players[1])
    else:
        print("Type yes or no")


def choosing_mark(first_player):
    choice = str(input(f"Choose your mark {first_player} (X or O): ")).upper()
    print(choice)
    if choice != "X" or choice != "O":
        print("[red]Not a valid choice! Choose again[/red]")
        choosing_mark(first_player)
    else:
        print("[green]Great Choice![/green]")
        return choice


def get_player_names():
    player1 = str(input(("Enter name player 1: "))).upper()
    player2 = str(input(("Enter name player 2: "))).upper()
    if player1 == player2:
        print(
            "Both players cannot have same name. Please try again with different names."
        )
        get_player_names()
    else:
        return [player1, player2]


if __name__ == "__main__":
    intro_message()
    players_list = get_player_names()
    players_list
    print("\n")
    welcome_players(players_list)
    game_rules()
    board = create_board()
    display_board(board)
    first_player = start_rolling(players_list)
    second_player = [x for x in players_list if x != first_player][0]
    first_player_mark = choosing_mark(first_player)
    second_player_mark = [x for x in ["X", "O"] if x != first_player_mark][0]
    print(first_player, first_player_mark, second_player, second_player_mark)
