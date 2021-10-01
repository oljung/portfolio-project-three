import random
class Mastermind:
    """
    This class contains the logic for the game mastermind, 
    all methods needed to run the game is contained in this class
    """
    def __init__(self, nrLow = 0, nrHigh = 9, length = 4):
        """
        The constructor is set up so you can alter the number range 
        and lenth of the secret code for a more varied game
        """
        self.nrLow = nrLow
        self.nrHigh = nrHigh
        self.length = length