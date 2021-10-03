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
        self.custom = False
        # call starting methods
        self.welcome_screen()
        self.select_game_type()


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
        'Your guess: 1234\n'+
        "The result: ['1', '-', 'C', '-']")
        print('This means the following:\n'+
        'The first number, 1, is in the correct position\n'+
        'The second number, 2, is not included in the secret code\n'+
        'The third number, 3, is in the code but is in the wrong position\n'+
        'The fourth number, 4, is not included in the code')
        print('When you have the correct numbers in the right place, you win!\n'+
        'Try to beat the game in as few guesses as possible.\n'+
        'The first thing you will do is decide if you want standard or custom game.\n'+
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
        if answer == 1:
            self.run_game()
        if answer == 2:
            self.run_game(True)


    def run_game(self, custom=False):
        """
        This method runs the game using the bool custom to 
        determing game type. It will create an object of Mastermind 
        based on value of custom. It will then update scores, ask 
        for another game and call itself using custom for same gametype 
        in loop
        """
        self.custom = custom # update instance variable, used for determining saving highscore or not
        game = None
        if not custom:
            game = Mastermind()
        else:# The user gets to set custom rules for the game
            correct_range = False
            while not correct_range:
                low = InputHandler.input_integer_range('Please select the lowest number: ',0, 8)
                high = InputHandler.input_integer_range('Please select the highest number: ', 1, 9)
                if high - low > 0:
                    correct_range = True
            length = InputHandler.input_integer('Please select a lenght: ')
            game = Mastermind(low, high, length)
        
        score = game.play()
        self.update_scores(score)
        play_again = InputHandler.input_bool('Would you like to play another round? Y(es) or N(no): ')
        if play_again:
            self.run_game(custom)


    def update_scores(self, score):
        """
        This method updates the values of the instance 
        variables handling scores from the game
        """
        self.result_list.append(score)
        
        if score < self.best_score:
            self.best_score = score
        
        if score > self.worst_score:
            self.worst_score = score


    def prepare_highscore_item(self):
        """
        This method returns a list of the values 
        stored in the instance variables for use when 
        updating a highscore table
        """
        average_score = round(sum(self.result_list)/len(self.result_list),2)# average score of rounds played, rounded to two decimals
        return [self.name, len(self.result_list), self.worst_score, self.best_score, average_score]
