from random import shuffle
import operator


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


class Deck:
    """
    This class builds a deck of objects from Card 
    the deck will then be used to build a hand and to deal new cards
    """
    def __init__(self):
        self.cards = []
        self.buildDeck()
        self.shuffle()


    def build_deck(self):
        """
        This method iterates through the lists in Card to create 
        13 Card objects for each of the four suites and appends them 
        all in the list cards
        """
        for suit in range(0, 4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))


    def shuffle(self):
        """
        This method shuffles the list "cards" making 
        the order random
        """
        shuffle(self.cards)


    def deal(self):
        """
        This method is used to deal cards from the deck 
        by removing and returning the last card in the list
        """
        return self.cards.pop()


class Hand(Deck):
    """
    This class creates and object containing cards from 
    the Deck class and methods for drawing and replacing cards
    """
    def __init__(self, name=''):
        self.cards = []
        self.name = name
    

    def deal(self, deck, cards):
        """
        This method is used to deal a new hand 
        and sort it based on card rank
        """
        while len(self.cards) < cards:
            self.cards.append(deck.deal())
        self.cards.sort(key=operator.attrgetter('rank'))# sorts the hand based on the rank value of each object