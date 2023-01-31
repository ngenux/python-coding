import sys
import random
import subprocess
import time


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

# Color constants for players and markers
PLAYER1_COLOR = "rgb(242,105,109)"
PLAYER2_COLOR = "rgb(105,242,237)"
MARKER1_COLOR = "rgb(234,214,55)"
MARKER2_COLOR = "rgb(57,77,234)"

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


def animate_rolling(num_of_rolls=2):
    """
    The animate_rolling function is a simple animation that displays a rotating sequence of characters in the terminal.
    It runs for a specified number of times, displaying characters like "Rolling |", "Rolling /", and others. Finally,
    it displays "Done!" to indicate that the animation has completed.
    """
    # loop through the animation `num_of_rolls` times
    for i in range(num_of_rolls * 4):
        # check the current iteration number modulo 4
        # and write the corresponding character to stdout
        if i % 4 == 0:
            sys.stdout.write("\rRolling |")
        elif i % 4 == 1:
            sys.stdout.write("\rRolling /")
        elif i % 4 == 2:
            sys.stdout.write("\rRolling -")
        else:
            sys.stdout.write("\rRolling \\")

        # flush stdout to display the current character
        sys.stdout.flush()
        # wait for 0.5 seconds before moving on to the next iteration
        time.sleep(0.5)

    # after the animation is finished, write "Done!" on a new line
    sys.stdout.write("\rDone!    \n")
    sys.stdout.flush()


def greet_players(players, player_colors):
    """
    This function greets the players by printing out a welcome message on the console. The message
    includes the names of the players in all capital letters, and their names are styled with the
    color specified in the player_colors argument.
    """
    console.print(
        Text("WELCOME!", style=f"bold green"),
        Text(players[0].upper(), style=f"bold {player_colors[0]}"),
        Text("and", style="green"),
        Text(players[1].upper(), style=f"bold {player_colors[1]}"),
        Text("Let the game begin!", style="green"),
    )


def explain_game_rules():
    console.rule(
        Text(" RULES OF THE GAME ", style="bold bright_red on bright_yellow"),
        style="bright_yellow",
    )
    console.print(
        "  + The starting player is chosen randomly by rolling a die. The player with the highest roll goes first.",
        style="green",
    )
    console.print(
        "  + Starting player is also given the option to choose their mark, either 'X' or 'O'.",
        style="green",
    )
    console.print(
        "  + Each player will get a chance to mark his position on the board in turns.",
        style="green",
    )
    console.print(
        "  + The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.",
        style="green",
    )
    console.print(
        "  + When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n",
        style="green",
    )


def create_board():
    """
    This function creates a 3x3 board filled with empty spaces and the color green. It uses nested list
    comprehension to generate a nested list of 3x3. Each element of the board is a list containing a
    string " " and a string "green" representing an empty space on the board with green color.
    """
    return [[[" ", "green"] for _ in range(3)] for _ in range(3)]


def roll_dice(player_names, player_colors):
    """
    The function "roll_dice()" takes in two parameters, "players" and "colors". It uses an animation to simulate
    the rolling of dice and generate random numbers between 1 and 6 to determine which player goes first. It checks
    if both players roll the same number and if so, prints a message saying "Oops its a tie" and continues the loop.
    If one player rolls a higher number, it prints a message saying the starting player and returns a tuple of the
    starting player and their corresponding color.
    """
    while True:
        animate_rolling()  # display rolling animation
        player1_roll, player2_roll = random.randint(1, 6), random.randint(
            1, 6
        )  # generate random numbers between 1 and 6

        console.print(
            Text(player_names[0], style=f"{player_colors[0]}"),
            Text("has rolled", style="green"),
            player1_roll,
        )  # Printing player name and rolled value
        console.print(
            Text(player_names[1], style=f"{player_colors[1]}"),
            Text("has rolled", style="green"),
            player2_roll,
        )  # Printing player name and rolled value
        if player1_roll == player2_roll:
            console.print(
                "Oops its a tie. Lets roll again..", style="green"
            )  # If both players roll the same number
        elif player1_roll > player2_roll:
            console.print(
                Text(player_names[0], style=f"{player_colors[0]}"),
                Text("start's the game", style="green"),
            )
            return [player_names[0], player_names[1]], [
                player_colors[0],
                player_colors[1],
            ]  # return tuple of starting player and their color
        else:
            console.print(
                Text(player_names[1], style=f"{player_colors[1]}"),
                Text("start's the game.", style="green"),
            )
            return [player_names[1], player_names[0]], [
                player_colors[1],
                player_colors[0],
            ]  # return tuple of starting player and their color


def start_game(player_names, player_colors):
    """
    The function "start_game()" takes in two parameters, "players" and "colors", which are lists of player
    names and colors respectively. It uses a loop to repeatedly prompt the user if they want to start the
    game and if the user selects "yes" it calls the roll_dice function, passing in the players and colors
    as arguments, if the user selects "no" it calls the exit_game function, that handles exiting the game.
    If the user does not select "yes" or "no", the loop continues and the prompt is displayed again.
    """
    while True:
        game_start_response = Prompt.ask(
            Text("Ready to start the game?", style="green"),
            default="yes",
            choices=["yes", "no"],
            show_default=False,
        )
        if game_start_response == "yes":
            return roll_dice(player_names, player_colors)
        elif game_start_response == "no":
            if exit_game():
                quit()
            else:
                continue


def choosing_mark(player_names_order, player_colors_order, marker_colors):
    """
    The function "choosing_mark()" takes in three parameters: player_names_order, player_colors_order, and
    marker_colors. It prompts the first player in the player_names_order list to choose a mark, either "x" or "o"
    using the Prompt.ask function. It then creates a list of marks in the order in which the players will use them,
    prints player's names along with the marks they will use and then wait for 3 seconds before returning the tuple
    of markers_order and marker_colors.
    """
    # prompt the first player to choose a mark "x" or "o"
    console.print("\nChoose your mark", style="bold green underline")
    # ask the first player in the player_names_order list to choose a mark,
    # either "x" or "o" and store it in the choice variable
    choice = Prompt.ask(
        Text(player_names_order[0], style=player_colors_order[0]),
        choices=["x", "o"],
        default="x",
        show_default=False,
    ).upper()
    # print "Great Choice!" in green color
    console.print("Great Choice!", style="green")
    # create a list of markers in the order in which the players will use them, where the first player's
    # chosen mark is the first element and the remaining mark as the second element
    markers_order = [choice] + [x for x in ["X", "O"] if x != choice]
    console.print(
        Text(player_names_order[0], style=player_colors_order[0]),
        Text(f"- {markers_order[0]}", style=f"{marker_colors[0]}"),
        Text(player_names_order[1], style=player_colors_order[1]),
        Text(f"- {markers_order[1]}", style=f"{marker_colors[1]}"),
    )
    # print "Starting game.." in green color
    console.print("Starting game..", style="green")
    # wait for 3 seconds before returning the tuple of markers_order and marker_colors
    time.sleep(3)
    return markers_order, marker_colors


def get_valid_player_names():
    """
    This function prompts the user to enter two player names, converts them to uppercase, and checks
    if the names are alphanumeric and not the same. If the names are not alphanumeric or the same,
    the user is prompted to enter new names. If the names are valid, the function returns a list
    containing the two player names.
    """
    while True:
        # Prompt user to enter first player name and convert to uppercase
        player1_name = Prompt.ask(
            Text("Enter first player name", style="green"), default="Player1"
        ).upper()
        # Prompt user to enter second player name and convert to uppercase
        player2_name = Prompt.ask(
            Text("Enter second player name", style="green"), default="Player2"
        ).upper()
        # Check if player names contain only alphanumeric characters
        if not player1_name.isalnum() or not player2_name.isalnum():
            console.print(
                "Player names can only contain alphanumeric characters.", style="red"
            )
            continue
        # Check if player names are not the same
        if player1_name == player2_name:
            console.print(
                "Both players cannot have the same name. Please try again.", style="red"
            )
        else:
            # If names are valid, return a list of player names
            return [player1_name, player2_name]


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


def exit_game():
    """
    The function "exit_game()" is used to ask the player if they want to exit the game. It uses the "Prompt.ask()"
    function to display a message "Do you want to exit?" with two options "yes" and "no" in green color. Based on the
    player's selection, it either prints a farewell message and returns true or return false.
    """
    # Asks the player if they want to exit the game
    exit_game = str(
        Prompt.ask(Text("Do you want to exit?", style="green"), choices=["yes", "no"])
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


if __name__ == "__main__":
    while True:
        round = 1
        show_game_intro()
        explain_game_rules()
        player_colors = [PLAYER1_COLOR, PLAYER2_COLOR]
        marker_colors = [MARKER1_COLOR, MARKER2_COLOR]
        player_names = get_valid_player_names()
        greet_players(player_names, player_colors)
        player_scores = [0, 0]
        while True:
            board = create_board()
            player_names_order, player_colors_order = start_game(
                player_names, player_colors
            )
            markers_order, marker_colors_order = choosing_mark(
                player_names_order, player_colors_order, marker_colors
            )
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
        if exit_game():
            quit()
        else:
            subprocess.run(["cls" if sys.platform == "win32" else "clear"], shell=True)
            console.print("Restarting Game..")
            time.sleep(3)
