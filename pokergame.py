from poker import Poker
from inputhandler import InputHandler

class RunPoker:
    """
    This class runs the game Poker and stores information 
    for use in highscore table
    """
    def __init__(self, name='NoName'):
        self.name = name
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.welcome_screen()
    

    def welcome_screen(self):
        """
        Method for showing a welcome screen to player with 
        information about the game and how to play
        """
        print()
        print('P*O*K*E*R')
        print('Welcome to a 5-card poker game,\n'+
        'The goal is the get a better hand than the AI.')
        print('To do this you get one chance to swap cards that are in your hand')
        print('You swap like this:\n'+
        '1. Choose how many cards you want to swap\n'+
        '2. Write the number of the card(s) you want to swap, like this:\n'+
        'If you want to swap card 2, type in 2.\n'+
        'If you want to swap card 1 and 4, type 14')
        print('When you have swapped your cards both your and AI hand is shown,\n'+
        'and the winner is declared.')
        print('Hand are ranked using standard poker rules:\n'+
        'In ascending order:\n'+
        'Highcard\n'+
        'Pair\n'+
        'Two Pair\n'+
        'Trips (three of a kind)\n'+
        'Straight (all cards are connected)\n'+
        'Flush (all card have the same suite)\n'+
        'Full House (Pair and Trips)\n'+
        'Quads (four of a kind)\n'+
        'Straight Flush (all cards connected and in suite)')
        print('In the unlikely event of a tie, the higher pair or similar wins.\n'+
        'If that value is the same, high card will win.\n'+
        'If highcard is the same rank, suite will win.Suites are ranked as follows:\n'+
        'In ascending order:\n'+
        'Clubs\n'+
        'Diamonds\n'+
        'Hearts\n'+
        'Spades')
        print('There are some slight deviations to tiebreakers, \n'+
        'you can read more about them here:\n'+
        '"link to repo"\n'+
        'NOTE! Ctrl + c will terminate the app, use right click to copy')
        answer = InputHandler.input_bool('Would you like to play a round? Y(es) or N(o): ')
        if answer:
            self.run_game()


    def run_game(self):
        """
        Method that runs a round of poker and returns winner. 
        After it updates the scores and ask for another round, calling itself if yes
        """
        game = Poker()
        AI_win = game.play_round(self.name)
        self.update_scores(AI_win)
        answer = InputHandler.input_bool('Would you like to play another round? Y(es) or N(o): ')
        if answer:
            self.run_game()


    def update_scores(self, AI_win):
        """
        Updates the scores stored in instance of object 
        for use in highscore table
        """
        self.games_played += 1
        if not AI_win:
            self.games_won += 1
        else:
            self.games_lost += 1


    def prepare_highscore_item(self):
        """
        Prepares an item for use in highscore table
        """
        if self.games_played == 0:
            return False
        else:
            win_rate = round(self.games_won/self.games_played, 2) * 100
            return [self.name, self.games_played, self.games_won, self.games_lost, win_rate]
