import operator

class HighScoreManager:
    """
    Class for handling a list of Highscore instances
    """
    def __init__(self, data):
        self.heading = data.pop(0)
        self.highscore_list = self.create_list(data)
    

    def create_list(self, data):
        """
        Creates instances of Highscore for each row in data 
        and appends them to the highscore_list
        """
        list = []
        for d in data:
            list.append(Highscore(d[0], int(d[1]), int(d[2]), int(d[3]), float(d[4])))
        return list


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
        return f'{self.name}\t{self.item1}\t{self.item2}\t{self.item3}\t{self.item4}'
