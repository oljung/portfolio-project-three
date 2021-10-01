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


    def __str__(self):
        """
        Changing the default return value for print(hand)
        """
        return f'Hand of {self.name} contains:\n {self.cards[0]}\n  {self.cards[1]}\n   {self.cards[2]}\n    ' \
                f'{self.cards[3]}\n     {self.cards[4]}\n'


class Ranking:
    """
    Class for handling the ranking of a hand for determining winning hand 
    of the game
    """
    rankings = [
        'Straight Flush',
        'narf'# value used to properly align straigh flush index (straight + flush = 9)
        'Quads',
        'Full House',
        'Flush',
        'Straight',
        'Trips',
        'Two Pair',
        'Pair',
        'High Card'
    ]


    def rank_hand(self, hand):
        """
        Ranks the value of a hand and returns the ranking and 
        value for use in comparing hands
        """
        value = 0
        value += self.flush(hand)
        value += self.straight(hand)
        if value == 0: # only needs to run if value is still zero. You can't have a pair and straight/flush at the same time
            value += self.two_three_four(hand)
        return value, self.rankings[value]

    
    def flush(self, hand):
        """
        Determines if the hand ranking is flush
        """
        value = 0
        flush = True
        for card in hand.get_cards():
            if 'previous_suit' in locals():
                if card.suit != previous_suit:
                    flush = False
            previous_suit = card.suit
        if(flush):
            value = 5
        return value


    def straight(self, hand):
        """
        Determines if the hand ranking is straight
        """
        value = 0
        connected = 0
        for card in hand.get_cards():
            if 'previous_rank' in locals():
                if card.rank == 1:
                    if card.rank == previous_rank + 1 or card.rank == previous_rank +9:
                        connected += 1
                else:
                    if card.rank == previous_rank + 1:
                        connected +=1
            previous_rank = card.rank
        if connected == 4:
            value = 4
        return value


    def two_three_four(self, hand):
        """
        Method for determining of hand has a pair, two pair, trips, 
        quads of full house
        """
        value = 0
        first_card = self.determine_first_card_in_set(hand)
        first_card_rank = 0
        second_card = None # This card is used for determining rank of highest 2nd pair in a tie
        same = 0
        first_same = 0
        if first_card != None:
            first_card_rank = first_card.rank
        for card in hand.get_cards():
            if 'previous_rank' in locals():
                if card.rank == previous_rank:
                    same += 1
                if card.rank == first_card_rank:
                    first_same += 1
                else:
                    second_card = card
            previous_rank = card.rank
        if same == 3 and first_same == 3:
            value = 7
        if same == 3 and first_same != 3:
            value = 6
        if same == 2 and first_same == 2:
            value = 3
        if same == 2 and first_same != 2:
            value = 2
        if same != 1:
            value = 1
        return value, second_card
    

    def determine_first_card_in_set(self, hand):
        """
        used to determine first card in a set of cards 
        of equal rank
        """
        return_card = None
        cards = hand.get_cards()
        for i in range(4):
            card = cards.pop(0)
            if card in cards:
                return_card = card
                break
        return return_card
