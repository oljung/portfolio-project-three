from mastermindgame import RunMastermind
from pokergame import RunPoker
from inputhandler import InputHandler
from worksheethandler import WorksheetHandler
from highscore import HighScoreManager


class Menu:
    """
    Class for running the application menu and handling 
    user choices
    """
    def __init__(self):
        self.welcome_screen()
        self.select_option()
    

    def welcome_screen(self):
        """
        Welcomes the user to the application
        """
        print('***********WELCOME TO***********')
        print('*M*A*S*T*E*R*M*I*N*D**P*O*K*E*R*')
        print('Please select which game you want to play,\n'+
        'or which highscore you want to see')
        print('Mastermind is a game of logic, trying to figure out a secret code.')
        print('Poker is a standard 5-card poker, where you are allowed on swap')
        print('Further instructions are provided when you start each game')
    

    def select_option(self):
        """
        Shows the options of the main menu and handles selection
        """
        print()
        print('What would you like to do?')
        print('1. Play Mastermind')
        print('2. Play Poker')
        print('3. Show Mastermind highscore')
        print('4. Show Poker highscore')
        print('0. Exit application')
        answer = InputHandler.input_integer_range('Your choice: ', 0, 4)

        if answer == 1:
            mastermind = RunMastermind()
            update = InputHandler.input_bool('Would you like to update highscore? Y(es) N(o): ')
            if update:
                data = mastermind.prepare_highscore_item()
                WorksheetHandler.update_worksheet('mastermind', data)
        
        if answer == 2:
            poker = RunPoker()
            update = InputHandler.input_bool('Would you like to update highscore? Y(es) N(o): ')
            if update:
                data = poker.prepare_highscore_item()
                WorksheetHandler.update_worksheet('poker', data)
        
        if answer == 3:
            self.show_highscore_menu()
        
        if answer == 4:
            self.show_highscore_menu(True)
        
        if answer != 0:
            self.select_option()
