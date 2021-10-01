from random import shuffle
import operator
from inputhandler import InputHandler


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
        self.sort_hand()
    

    def sort_hand(self):
        """
        Sorts the hand based on rank in ascending order
        """
        self.cards.sort(key=operator.attrgetter('rank'))


    def get_cards(self):
        """
        Returns the list of cards in the hand object
        """
        return self.cards


    def swap_cards(self, deck):
        """
        Method for swapping cards in list of cards 
        in the hand object by replacing with a new card from 
        the deck
        """
        length = InputHandler.input_integer_range('How many cards do you want to swap? 0-5: ', 0, 5)
        if length != 0:
            positions = InputHandler.input_integer_sequence('Please select with cards as a number, like: 14 or 125')
            for pos in positions:
                self.cards.pop(pos-1)# the values in position will be fron 1-5, index of cards is from 0-4
                self.cards.insert(pos-1, deck.deal())
            self.sort_hand()
