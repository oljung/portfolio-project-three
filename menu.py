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
        self.name = InputHandler.input_name('Please enter your name: ')
        self.select_option()

    def welcome_screen(self):
        """
        Welcomes the user to the application
        """
        print('***********WELCOME TO***********')
        print('*M*A*S*T*E*R*M*I*N*D**P*O*K*E*R*')
        print('Please select which game you want to play,\n' +
              'or which highscore you want to see')
        print('Mastermind is a game of logic, trying to figure out a secret code.')
        print('Poker is a standard 5-card poker, where you are allowed on swap')
        print('Further instructions are provided when you start each game')
        print()

    def select_option(self):
        """
        Shows the options of the main menu and handles selection
        """
        CHOICE_PLAY_MASTERMIND = 1
        CHOICE_PLAY_POKER = 2
        CHOICE_SHOW_MASTERMIND = 3
        CHOICE_SHOW_POKER = 4
        print()
        print('What would you like to do?')
        print('1. Play Mastermind')
        print('2. Play Poker')
        print('3. Show Mastermind highscore')
        print('4. Show Poker highscore')
        print('0. Exit application')
        answer = InputHandler.input_integer_range('Your choice: ', 0, 4)

        if answer == CHOICE_PLAY_MASTERMIND:
            mastermind = RunMastermind(self.name)
            data = mastermind.prepare_highscore_item()
            if data:
                update = InputHandler.input_bool('Would you like to update highscore? Y(es) N(o): ')
                if update:
                    WorksheetHandler.update_worksheet('mastermind', data)

        if answer == CHOICE_PLAY_POKER:
            poker = RunPoker(self.name)
            data = poker.prepare_highscore_item()
            if data:
                update = InputHandler.input_bool('Would you like to update highscore? Y(es) N(o): ')
                if update:
                    WorksheetHandler.update_worksheet('poker', data)

        if answer == CHOICE_SHOW_MASTERMIND:
            self.show_highscore_menu()

        if answer == CHOICE_SHOW_POKER:
            self.show_highscore_menu(True)

        if answer != 0:
            self.select_option()

    def show_highscore_menu(self, poker=False):
        """
        Shows a menu on what to do with the highscore
        information
        """
        worksheet = ''
        if poker:
            worksheet = 'poker'
        else:
            worksheet = 'mastermind'

        data = WorksheetHandler.get_worksheet_data(worksheet)
        highscore = HighScoreManager(data, poker)
        line1 = '1. Show results sorted by rounds played'
        line2 = '2. '
        line3 = '3. '
        line4 = '4. Show results by player'
        if poker:
            line2 += 'Show results sorted by games won'
            line3 += 'Show best five scores sorted by winrate'
        else:
            line2 += 'Show results sorted by best score'
            line3 += 'Show best five scores sorted by average score'

        CHOICE_SHOW_ROUNDS = 1
        CHOICE_SHOW_WIN_BEST = 2
        CHOICE_SHOW_BEST_5 = 3
        CHOICE_SHOW_PLAYER = 4
        print()
        print('Please select an option:')
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print('0. Back to main menu')
        print()

        answer = InputHandler.input_integer_range('Your choice: ', 0, 4)

        if answer == CHOICE_SHOW_ROUNDS:
            highscore.sort_list('item1')
            highscore.print_table()

        if answer == CHOICE_SHOW_WIN_BEST:
            highscore.sort_list('item2')

        if answer == CHOICE_SHOW_BEST_5:
            highscore.show_best_five(poker)

        if answer == CHOICE_SHOW_PLAYER:
            name = InputHandler.input_name('Please enter the name to display results for: ')
            highscore.show_results_by_player(name)

        if answer != 0:
            self.show_highscore_menu(poker)
