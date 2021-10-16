from random import shuffle
import operator
from inputhandler import InputHandler
import copy


class Card:
    """
    This is a class for creating a card object that has a suit and a rank
    the cards are used to build a deck
    """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [
        "narf",
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        This function sets the default value returned when print(card)
        is called
        """
        return f'{self.ranks[self.rank]} of {self.suits[self.suit]}'


class Deck:
    """
    This class builds a deck of objects from Card
    the deck will then be used to build a hand and to deal new cards
    """
    def __init__(self):
        self.cards = []
        self.build_deck()
        self.shuffle()

    def build_deck(self):
        """
        This method iterates through the lists in Card to create
        13 Card objects for each of the four suits and appends them
        all in the list cards
        """
        for suit in range(0, 4):
            for rank in range(1, 14):
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
        length = InputHandler.input_integer_range('How'\
             'many cards do you want to swap? 0-5: ', 0, 5)
        if length == 5:
            self.cards.clear()
            self.deal(deck, 5)
        elif length != 0:
            positions = InputHandler.input_integer_sequence('Please' \
                 ' select which cards to swap, seperated by a comma: ', length)
            correct_values = True
            for pos in positions:
                if pos < 1 or pos > 5:
                    correct_values = False
                    print('cards are numbered 1-5\n')
            if correct_values:
                for pos in positions:
                    # the values in position will be fron 1-5
                    self.cards.pop(pos-1)
                    self.cards.insert(pos-1, deck.deal())
        self.sort_hand()

    def __str__(self):
        """
        Changing the default return value for print(hand)
        """
        return f'Hand of {self.name} contains:\n {self.cards[0]}\n ' \
            f' {self.cards[1]}\n   {self.cards[2]}\n    ' \
                f'{self.cards[3]}\n     {self.cards[4]}\n'


class Ranking:
    """
    Class for handling the ranking of a hand for determining winning hand
    of the game
    """
    rankings = [
        'High Card',
        'Pair',
        'Two Pair',
        'Trips',
        'Straight',
        'Flush',
        'Full House',
        'Quads',
        # value used to properly align straigh flush index
        'narf',
        'Straight Flush'
    ]

    def rank_hand(self, hand):
        """
        Ranks the value of a hand and returns the ranking and
        value for use in comparing hands
        """
        value = 0
        value += self.flush(hand)
        value += self.straight(hand)
        # only needs to run if value is still zero.
        # You can't have a pair and straight/flush at the same time
        if value == 0:
            rank_value, second_card = self.two_three_four(hand)
            value += rank_value
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
                    if card.rank == previous_rank + 1 or card.rank == previous_rank + 9:
                        connected += 1
                else:
                    if card.rank == previous_rank + 1:
                        connected += 1
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
        # This card is used for determining rank of highest 2nd pair in a tie
        second_card = None
        same = 0
        first_same = 0
        if first_card is not None:
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
        if same == 1:
            value = 1
        return value, second_card

    def determine_first_card_in_set(self, hand):
        """
        used to determine first card in a set of cards
        of equal rank
        """
        return_card = None
        cards_to_copy = hand.get_cards()
        cards = copy.deepcopy(cards_to_copy)
        card_found = False
        for i in range(4):
            if not card_found:
                card = cards.pop(0)
                # compare the removed card to the remaining cards in list
                for c in cards:
                    if card.rank == c.rank:
                        return_card = card
                        card_found = True
                        break

        return return_card

    def get_highcard(self, hand):
        """
        Returns the card with the highest rank in hand
        """
        cards = hand.get_cards()
        if cards[0].rank == 1:
            return cards[0]
        else:
            return cards[4]

    def determine_winner(self, player_hand, AI_hand):
        """
        Compare rankings between two hands to determine which hand is the best
        """
        player_value, player_ranking = self.rank_hand(player_hand)
        AI_value, AI_ranking = self.rank_hand(AI_hand)
        result = ''
        AI_win = False
        if player_value > AI_value:
            result = f'{player_hand.name} wins the round' \
                f'with a {player_ranking}.'
        elif AI_value > player_value:
            AI_win = True
            result = f'{AI_hand.name} wins the round with a {AI_ranking}.'
        else:
            AI_win = self.tiebreak(player_hand, AI_hand, player_value)
            if not AI_win:
                result = f'{player_hand.name} wins the round with' \
                     f'a better {player_ranking}.'
            else:
                result = f'{AI_hand.name} wins the round' \
                    f'with a better {AI_ranking}.'
        return AI_win, result

    def tiebreak(self, player_hand, AI_hand, value):
        """
        Decides the best hand when two hands have the same value
        """
        AI_win = False
        if value == 9 or value == 5:
            if AI_hand.get_cards()[0].suit > player_hand.get_cards()[0].suit:
                AI_win = True

        if value == 7 or value == 3 or value == 1:
            player_set = self.determine_first_card_in_set(player_hand)
            AI_set = self.determine_first_card_in_set(AI_hand)
            if AI_set.rank == 1 and player_set.rank != 1:
                AI_win = True
            if player_set.rank != 1:
                if AI_set.rank > player_set.rank:
                    AI_win = True

        if value == 6 or value == 2:
            player_rank, player_trips = self.two_three_four(player_hand)
            AI_rank, AI_trips = self.two_three_four(AI_hand)
            player_set = self.determine_first_card_in_set(player_hand)
            AI_set = self.determine_first_card_in_set(AI_hand)
            if AI_set.rank == 1 and player_set.rank != 1:
                AI_win = True
            if player_set.rank != 1:
                if AI_trips.rank > player_trips.rank:
                    AI_win = True
                if AI_trips.rank == player_trips.rank:
                    player_highcard = self.get_highcard(player_hand)
                    AI_highcard = self.get_highcard(AI_hand)
                    if AI_highcard.rank > player_highcard.rank:
                        AI_win = True
                    if AI_highcard.rank == player_highcard.rank:
                        if AI_highcard.suit > player_highcard.suit:
                            AI_win = True

        if value == 4 or value == 0:
            player_highcard = self.get_highcard(player_hand)
            AI_highcard = self.get_highcard(AI_hand)
            if AI_highcard.rank == 1 and player_highcard.rank != 1:
                AI_win = True
            if player_highcard.rank != 1:
                if AI_highcard.rank > player_highcard.rank:
                    AI_win = True
            if AI_highcard.rank == player_highcard.rank:
                if AI_highcard.suit > player_highcard.suit:
                    AI_win = True
        return AI_win


class Poker:
    """
    This class plays a round of poker using the other classes to do so
    """
    def play_round(self, name):
        """
        Plays a round of poker and returns the winner
        """
        deck = Deck()
        player_hand = Hand(name)
        AI_hand = Hand('AI')
        player_hand.deal(deck, 5)
        AI_hand.deal(deck, 5)
        print()
        print(player_hand)
        print()
        player_hand.swap_cards(deck)
        print()
        ranking = Ranking()
        AI_win, result = ranking.determine_winner(player_hand, AI_hand)
        print(player_hand)
        print()
        print(AI_hand)
        print()
        print(result)
        return AI_win
