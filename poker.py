



class Card:
    """
    This is a class for creating a card object that has a suite and a rank 
    the cards are used to build a deck
    """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        This function sets the default value returned when print(card) is called
        """
        return f'{self.ranks[self.rank]} of {self.suits[self.suit]}'


    