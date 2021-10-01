from mastermind import Mastermind
from inputhandler import InputHandler

class RunMastermind:
    """
    This class runs the game Mastermind and stores information 
    for use in a highscore format
    """
    def __init__(self, name='NoName'):
        self.name = name
        self.best_score = 0
        self.worst_score = 0
        self.result_list = []