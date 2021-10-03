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