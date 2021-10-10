import operator


class HighScoreManager:
    """
    Class for handling a list of Highscore instances
    """
    def __init__(self, data, poker=False):
        self.heading = data.pop(0)
        self.highscore_list = self.create_list(data)
        self.poker = poker

    def create_list(self, data):
        """
        Creates instances of Highscore for each row in data
        and appends them to the highscore_list
        """
        list = []
        for d in data:
            list.append(Highscore(d[0], int(d[1]), int(d[2]), int(d[3]), float(d[4])))
        return list

    def sort_list(self, key_value):
        """
        Sorts the list of highscore instances using the
        key_value as key with operator.attrgetter
        """
        self.highscore_list.sort(key=operator.attrgetter(key_value))
        
        if not self.poker and key_value == 'item2':
            pass  # Mastmind score does not need to be reversed
        else:
            self.highscore_list.reverse()

    def print_heading(self):
        """
        Prints the heading formatted as a table
        """
        print(f'{self.heading[0]}\t{self.heading[1]}\t{self.heading[2]}\
            \t{self.heading[3]}\t{self.heading[4]}\t')

    def print_table(self):
        """
        Prints header and the items in highscore_list
        formatted as a table
        """
        print()
        self.print_heading()
        for item in self.highscore_list:
            print(item)

    def show_best_five(self, poker):
        """
        Shows the five best averages or win rates with
        at least five rounds played
        """
        best_five = []
        self.sort_list('item4')  # average/winrate is stored in item4
        for highscore in self.highscore_list:
            if highscore.item1 >= 5:
                best_five.append(highscore)

        if len(best_five) >= 5:
            if poker:
                # if its poker, the highest 5 values are the best
                best_five = best_five[-5:]
            else:
                # if mastermind, the lowest 5 values are the best
                best_five = best_five[:5]

        print()
        self.print_heading()
        for score in best_five:
            print(score)

    def show_results_by_player(self, name):
        """
        Method for displaying games made by a player
        with the given name
        """
        player_scores = []
        for item in self.highscore_list:
            if item.name == name:
                player_scores.append(item)

        print()
        if not player_scores:
            print('No player with that name has recorded a highscore')
        else:
            self.print_heading()
            for item in player_scores:
                print(item)


class Highscore:
    """
    This class holds information about a highscore
    converted from a worksheet table
    """
    def __init__(self, name, item1, item2, item3, item4):
        self.name = name
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4

    def __str__(self):
        """
        Sets the default return value when print(highscore) is called
        """
        return f'{self.name}\t{self.item1}\t\t{self.item2}\
            \t\t{self.item3}\t\t{self.item4}'
