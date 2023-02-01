"""
Module for defining the `Players` class, which manages player data for a game.
"""
import time, random
from typing import List, Tuple, Union
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from utils import GameTools


class Players:
    """
    This class is used to initialize players and their properties.

    :param num_players: Number of players in the game.
    :type num_players: int
    :param player_marks: List of all available player marks.
    :type player_marks: list of str
    """

    def __init__(self, num_players: int, player_marks: List[str]):
        """
        Initialize the player properties.

        :raises ValueError: If number of players and player marks don't match.
        """
        if len(player_marks) != num_players:
            raise ValueError("Number of players and marks don't match.")
        self.num_players = num_players
        self.player_marks = player_marks
        self.player_names = []
        self.player_colors = []
        self.player_scores = []
        self.mark_colors = []
        self.players_order = []
        self.console = Console()

    def get_valid_player_names(self) -> List[str]:
        """
        Prompt the user to enter player names and validate the input.

        :return: List of player names.
        :rtype: list of str
        """
        while len(self.player_names) < self.num_players:
            # Prompt the user to enter a player name and convert it to uppercase
            player_name = Prompt.ask(
                Text(f"Enter player-{len(self.player_names) + 1} name", style="green"),
                default=f"Player{len(self.player_names) + 1}",
            ).upper()

            # Check if the player name contains only alphanumeric characters
            if not player_name.isalnum():
                self.console.print(
                    "Player names can only contain alphanumeric characters.",
                    style="red",
                )
                continue

            # Check if the player name already exists
            if player_name in self.player_names:
                continue

            self.player_names.append(player_name)

        return self.player_names

    def get_player_colors(self) -> List[str]:
        """
        Generate and return colors for each player.

        :return: List of player colors.
        :rtype: list of str
        """
        # Generate player colors
        self.player_colors = GameTools.generate_colors(self.num_players)

        # Return the generated player colors
        return self.player_colors

    def greet_players(self) -> None:
        """
        Display a welcome message to the players.
        """
        # Create a text object to store the welcome message
        text = Text()

        # Append the word "WELCOME!" to the text object in bold green text
        text.append("WELCOME!", style="bold green")

        # If there is only one player, display the player's name in their designated color
        if self.num_players < 2:
            text.append(self.player_names[0], style=f"bold {self.player_colors[0]}")
            self.console.print(text)
        else:
            # For multiple players, iterate through the list of player names and colors
            for idx in range(self.num_players):
                if idx == (self.num_players - 2):
                    text.append(
                        self.player_names[idx], style=f"bold {self.player_colors[idx]}"
                    )
                    text.append(" AND ", style="green")
                elif idx == (self.num_players - 1):
                    text.append(
                        self.player_names[idx], style=f"bold {self.player_colors[idx]}"
                    )
                else:
                    text.append(
                        self.player_names[idx], style=f"bold {self.player_colors[idx]}"
                    )
                    text.append(", ", style="green")

            # Display the completed welcome message
            self.console.print(text)

    def initialize_player_scores(self) -> List[int]:
        """
        Initialize the player scores to 0.

        :return: List of player scores.
        :rtype: list of int
        """
        # Create a list of player scores initialized to 0
        self.player_scores = [0] * self.num_players

        # Return the list of player scores
        return self.player_scores

    def player_turns_and_colors(self) -> Tuple[List[str], List[str]]:
        """
        Determine the order of players' turns and colors.

        :return: Tuple of players' names and colors.
        :rtype: tuple of two lists
        """
        # Shuffle the player names
        GameTools.animate_shuffle()
        random.shuffle(self.player_names)

        # Store the players order
        self.players_order = self.player_names

        # Create a Text object to display the order
        text = Text()
        text.append("Players order: ", style="green")

        # Display the order
        print(self.players_order)
        for idx, player in enumerate(self.players_order):
            text.append(f"{player} ", style=f"bold {self.player_colors[idx]}")
        self.console.print(text)

        # Return the players order and player colors
        return self.players_order, self.player_colors

    def player_markers_and_colors(self) -> Tuple[List[str], List[str]]:
        """
        Determine the markers for each player and their corresponding colors.

        :return: Tuple of players' markers and colors.
        :rtype: tuple of two lists
        """
        player_marks = []  # list to store player markers
        for idx, player in enumerate(
            self.players_order
        ):  # loop through each player in order
            text = Text()
            text.append(
                "Please Choose your mark ", style="green"
            )  # add text to display prompt
            text.append(
                player, style=f"bold {self.player_colors[idx]}"
            )  # add player name to prompt
            self.console.print(text)  # print prompt to console
            player_mark = Prompt.ask(
                text, choices=self.player_marks
            )  # ask player to choose a marker from available options
            self.player_marks.remove(player_mark)  # remove chosen marker from options
            player_marks.append(player_mark)  # add chosen marker to player_marks list
        print(player_marks)
        self.player_marks = player_marks  # store player_marks as class variable
        del player_marks  # delete local player_marks variable
        self.mark_colors = GameTools.generate_colors(
            self.num_players
        )  # generate colors for player markers
        return (
            self.player_marks,
            self.mark_colors,
        )  # return tuple of player_marks and colors

    def show_player_marks(self) -> None:
        """
        Display the markers for each player.
        """
        # Print "PLAYER MARKS" in bold yellow color with underline
        self.console.print("PLAYER MARKS", style="bold yellow underline")

        # Loop through each player
        for i in range(self.num_players):
            text = Text()

            # Display the player name in bold with corresponding player color
            text.append(self.player_names[i], style=f"bold {self.player_colors[i]}")

            # Display the player marker in bold with corresponding marker color
            text.append(
                f" - {self.player_marks[i]}", style=f"bold {self.mark_colors[i]}"
            )

            # Print the formatted text
            self.console.print(text)

            # Sleep for 3 seconds
            time.sleep(3)
