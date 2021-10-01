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


    def welcome_screen(self):
        """
        This method runs a welcome screen informing the user of what 
        this is and how to play it
        """
        print('*M*A*S*T*E*R*M*I*N*D*')
        print('Welcome to Mastermind!')
        print('The goal of this game is to guess the secret code.\n' + 
        'You have as many guesses as you need.\n' +
        'After every guess you will see a result of that guess.\n'+
        'A result may look like this:\n'+
        'Your guess: 1234'+
        '[1, -, C, -]')
        print('This means the following:\n'+
        'The first number, 1, is in the correct position\n'+
        'The second number, 2, is not included in the secret code\n'+
        'The third number, 3, is in the code but is in the wrong position\n'+
        'The fourth number, 4, is not included in the code')
        print('When you have the correct numbers in the right place, you win!\n'+
        'Try to beat the game in as few guesses as possible.\n'+
        'The first thing you will do is decide if you want standard or cusom game.\n'+
        'Only the standard game can save you highscore')


    def select_game_type(self):
        """
        This method selects the game type, the standard game 
        or a default version where the user can select lenght of code 
        and what numbers to include
        """
        print('Please secect game type.\n'+
        'NOTE! only standard game saves highscore')
        print('1. Standard game')
        print('2. Custom game, set your rules')
        print('0. Back to main menu')
        answer = InputHandler.input_integer_range('Please make a choice: ', 0, 2)
        if answer == '1':
            run_game()
        if answer == '2':
            run_game(True)
