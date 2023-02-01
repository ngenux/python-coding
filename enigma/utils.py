"""
The `GameTools` module provides static methods for generating random colors and animating the shuffling of players.

Methods:
    generate_colors(number=2) -> List[str]:
        Generates a list of `number` random color values in RGB format.
    
    animate_shuffle(num_of_rolls=2) -> None:
        Animate the shuffling of players.

"""


from typing import List, Tuple, Union
import random, sys, colorsys, time


class GameTools:
    @staticmethod
    def generate_colors(number=2) -> List[str]:
        """
        Generates a list of `number` random color values in RGB format.

        :param number: Number of colors to generate.
        :type number: int
        :return: List of random RGB color values.
        :rtype: list of str
        """
        colors = []
        # Loop through the range `number` times to generate colors
        for _ in range(number):
            # generate random values for h, s and l
            h, s, l = (
                random.random(),
                0.5 + random.random() / 2.0,
                0.4 + random.random() / 5.0,
            )
            # convert the generated hls values to rgb values
            r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
            # append the generated rgb color string to the `colors` list
            colors.append(str(f"rgb({r},{g},{b})"))

        # return the generated color strings
        return colors

    @staticmethod
    def animate_shuffle(num_of_rolls=2) -> None:
        """
        Animate the shuffling of players.

        :param num_of_rolls: Number of rolls for the animation.
        :type num_of_rolls: int
        :return: None
        :rtype: None
        """
        # Loop through the animation `num_of_rolls` times
        for i in range(num_of_rolls * 4):
            # Check the current iteration number modulo 4
            # and write the corresponding character to stdout
            if i % 4 == 0:
                sys.stdout.write("\rShuffling Players |")
            elif i % 4 == 1:
                sys.stdout.write("\rShuffling Players /")
            elif i % 4 == 2:
                sys.stdout.write("\rShuffling Players -")
            else:
                sys.stdout.write("\rShuffling Players \\")

            # Flush stdout to display the current character
            sys.stdout.flush()
            # Wait for 0.5 seconds before moving on to the next iteration
            time.sleep(0.5)

        # After the animation is finished, write "Done!" on a new line
        sys.stdout.write("\rDone!    \n")
        sys.stdout.flush()
