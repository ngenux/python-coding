# importing libraries
import dict

def game_timing(self, player_time):
    """
    This function return True when player time crosses 30 secs else False.
    Input:
    player_time: Int
    """
    if player_time > 30:
        return True
    else:
        return False