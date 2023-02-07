import sys
import random
import subprocess
import time
import colorsys
from typing import List, Tuple, Union
from players import Players


# Check if the rich library is installed
while True:
    try:
        from rich.markdown import Markdown
        from rich.console import Console
        from rich.text import Text
        from rich.prompt import Prompt

        break
    except ModuleNotFoundError:
        # If the library is not found, ask user to confirm installation
        print("Rich library is needed to continue.")
        while True:
            installation = input("Do you want to install it? (yes/no): ")
            if installation == "yes":
                print("Installing Rich..")
                subprocess.call("pip install rich", shell=True)
                print("Done!")
                break
            elif installation == "no":
                print(
                    "Exiting.. Game cannot run properly without required dependencies!"
                )
                time.sleep(3)
                quit()
            else:
                print("Provide a valid response: yes or no")
                continue
        continue


console = Console()


def show_game_intro():
    # Print the banner message using the console.print() function
    # The message is in Markdown format and passed to the Markdown() function
    console.print(
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
        ),
        style="bold rgb(48,227,223) blink",
    )
    # Print new line
    console.print("\n")
    # Print the message
    console.print("Let the Fun begins. :alien:", style="green")


def explain_game_rules():
    console.rule(
        Text(" RULES OF THE GAME ", style="bold bright_red on bright_yellow"),
        style="bright_yellow",
    )
    console.print(
        Text(
            "  + The starting player is chosen randomly by rolling a die. The player with the highest roll goes first.",
            style="green",
        ),
        Text(
            "  + Starting player is also given the option to choose their mark, either 'X' or 'O'.",
            style="green",
        ),
        Text(
            "  + Each player will get a chance to mark his position on the board in turns.",
            style="green",
        ),
        Text(
            "  + The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.",
            style="green",
        ),
        Text(
            "  + When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n",
            style="green",
        ),
    )


def create_board():
    """
    This function creates a 3x3 board filled with empty spaces and the color green. It uses nested list
    comprehension to generate a nested list of 3x3. Each element of the board is a list containing a
    string " " and a string "green" representing an empty space on the board with green color.
    """
    return [[[" ", "green"] for _ in range(3)] for _ in range(3)]


class Prompt:
    @staticmethod
    def end_game() -> bool:
        console = Console()
        # Asks the player if they want to exit the game
        exit_game = str(
            Prompt.ask(
                Text("Do you want to exit?", style="green"), choices=["yes", "no"]
            )
        )
        # If the player chooses 'yes', the function prints a farewell message and returns True
        if exit_game == "yes":
            console.print(
                "Thanks for playing! We hope you had a blast. See you next time for more fun and excitement!",
                style="italic yellow",
            )
            return True
        # If the player chooses 'no', the function returns False
        else:
            return False

    @staticmethod
    def start_game() -> None:
        while True:
            game_start_response = Prompt.ask(
                Text("Ready to start the game?", style="green"),
                default="yes",
                choices=["yes", "no"],
                show_default=False,
            )
            if game_start_response == "yes":
                return
            elif game_start_response == "no" and Prompt.end_game():
                quit()


def display_board(board, round):
    """
    The code loops through the rows and elements in the board and uses the `console.print` function to
    display each element with the appropriate formatting. If the current element is the first in the row,
    it will add a leading space before it. If the current element is the last in the row, it will add a
    trailing space after it. It also adds a "|" separator between the element if it is not the last element
    in the row, and also add a '---+---+---' separator if the current row is not the last row.
    """
    # Clear the console
    subprocess.run(["cls" if sys.platform == "win32" else "clear"], shell=True)
    # Print the round number in bold yellow underline
    console.print(f"GAME ROUND {round}\n", style="bold dark_orange underline")
    # Loop through the rows of the board
    for i in range(3):
        # Loop through the columns of the board
        for j in range(3):
            if j == 0:
                # for the first element in the row, print a leading space
                console.print(
                    f" {board[i][j][0]}", style=f"bold {board[i][j][1]}", end=" "
                )
            elif j == 2:
                # for the last element in the row, print a trailing space
                console.print(f"{board[i][j][0]} ", style=f"bold {board[i][j][1]}")
            else:
                console.print(
                    f"{board[i][j][0]}", style=f"bold {board[i][j][1]}", end=" "
                )
            # If the current column is not the last, print the column seperator
            if j != 2:
                console.print("|", style="green", end=" ")
        # If the current row is not the last, print the row separator
        if i != 2:
            console.print("---+---+---", style="green")
    # Print a newline at the end
    console.print("\n")


def check_win(board, player_mark):
    """
    The function "check_win()" checks for a win condition by checking all rows, columns, and diagonals of the board
    for all instances of the player's mark passed as an argument, if all elements are equal, the function returns True,
    otherwise, it returns False.
    """
    # check rows
    for row in range(3):
        if all(board[row][col][0] == player_mark for col in range(3)):
            return True
    # check columns
    for col in range(3):
        if all(board[row][col][0] == player_mark for row in range(3)):
            return True
    # check diagonals
    if all(board[i][i][0] == player_mark for i in range(3)):
        return True
    if all(board[i][2 - i][0] == player_mark for i in range(3)):
        return True
    return False


def check_tie(board):
    """
    The function check_tie(board) checks if the current state of the board is a tie. It iterates through each element
    of the board and checks if any element is empty (" "). If any empty element is found, it returns False indicating
    that the game is not tied yet. If all elements of the board are filled, it returns True, indicating the game is tied.
    """
    for row in range(3):
        for col in range(3):
            if board[row][col][0] == " ":
                return False
    return True


def game_over():
    """
    The function "game_over()" repeatedly prompts the user with a question asking if they want to play another round using
    the Prompt.ask method. If the user chooses "yes", it returns True, if the user chooses "no", it returns False.
    """
    choice = Prompt.ask(
        Text("Do you want to play another round?", style="green"),
        choices=["yes", "no"],
    )
    if choice == "yes":
        return True
    else:
        return False


def player_move(board, player_name, player_color, player_mark, mark_color):
    """
    The function player_move handles player's input, it prints current player's name and mark color and
    prompts player to input row and column. It then checks if the input position is already occupied, if
    so, prompts for new input. If not, updates the board and returns it.
    """
    # Prints the current player's name and their mark color in a bold and blinking
    console.print(
        Text(f"{player_name}'S MOVE -", style=f"bold {player_color} blink"),
        Text(player_mark, style=f"bold {mark_color}"),
    )
    while True:
        # Asks the player to enter the row number, with choices of 1, 2, or 3
        row = (
            int(
                Prompt.ask(
                    Text("Enter row number", style="green"), choices=["1", "2", "3"]
                )
            )
            - 1
        )
        # Asks the player to enter the column number, with choices of 1, 2, or 3
        col = (
            int(
                Prompt.ask(
                    Text("Enter column number", style="green"),
                    choices=["1", "2", "3"],
                )
            )
            - 1
        )
        # Check if the position is already occupied
        if board[row][col][0] != " ":
            console.print(
                "That position is already occupied. Please choose a different position.",
                style="red",
            )
            continue
        # update the board with the entered position
        board[row][col] = [player_mark, mark_color]
        return board


def game_loop(
    board,
    player_names_order,
    player_colors_order,
    markers_order,
    marker_colors_order,
    round,
    player_scores,
):
    """
    This function displays the current board. It calls the player_move function to let the current player make a move
    displays the updated board. It checks if the current player has won, if so, increase the current player's score.
    Checks if the game is a tie. if the game is a tie, returns the scores. Then changes the current player to the next
    player continues the loop until a win or tie is detected.
    """
    # displays the current board
    display_board(board, round)
    # current player variable is set to 0
    current_player = 0
    while True:
        # calls the player_move function to let the current player make a move
        board = player_move(
            board,
            player_names_order[current_player],
            player_colors_order[current_player],
            markers_order[current_player],
            marker_colors_order[current_player],
        )
        # displays the updated board after move
        display_board(board, round)
        # checks if the current player has won
        if check_win(board, markers_order[current_player]):
            console.print(
                Text("Congratulations", style="green"),
                Text(
                    player_names_order[current_player],
                    style=player_colors_order[current_player],
                ),
                Text("you have won the game!", style="green"),
            )
            # increase the current player's score
            player_scores[current_player] += 1
            return player_scores
        # checks if the game is a tie
        if check_tie(board):
            console.print("The game is a tie!", style="green")
            return player_scores
        # changes the current player to the next player
        current_player = (current_player + 1) % 2


if __name__ == "__main__":
    while True:
        round = 1
        show_game_intro()
        explain_game_rules()
        players = Players(num_players=2, player_marks=["X", "O"])
        players.get_valid_player_names()
        players.get_player_colors()
        players.greet_players()
        players.initialize_player_scores()
        Prompt.start_game()
        while True:
            board = create_board()
            player_names_order, player_colors_order = players.player_turns_and_colors()
            markers_order, marker_colors_order = players.player_markers_and_colors()
            players.show_player_marks()
            player_scores = players.initialize_player_scores()

            player_scores = game_loop(
                board,
                player_names_order,
                player_colors_order,
                markers_order,
                marker_colors_order,
                round,
                player_scores,
            )
            console.print(
                Text("SCORES:", style="green"),
                Text(
                    f"{player_names_order[0]}-{player_scores[0]}",
                    style=player_colors_order[0],
                ),
                Text("AND", style="green"),
                Text(
                    f"{player_names_order[1]}-{player_scores[1]}",
                    style=player_colors_order[1],
                ),
            )
            if game_over():
                console.print("Gear up for another round.", style="green")
                round += 1
                continue
            break
        if Prompt.end_game():
            quit()
        else:
            subprocess.run(["cls" if sys.platform == "win32" else "clear"], shell=True)
            console.print("Restarting Game..")
            time.sleep(3)
