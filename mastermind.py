import random
from inputhandler import InputHandler


class Mastermind:
    """
    This class contains the logic for the game mastermind,
    all methods needed to run the game is contained in this class
    """
    def __init__(self, nr_low=0, nr_high=9, length=4):
        """
        The constructor is set up so you can alter the number range
        and lenth of the secret code for a more varied game
        """
        self.nr_low = nr_low
        self.nr_high = nr_high
        self.length = length

    def secret_number(self, nr_low, nr_high, length):
        """
        This method will generate a random sequence of numbers
        with nrLow being hte lowest and nrHigh being the highest
        using length. If the difference between highest and lowest
        is larger than or equal to length, the numbers will be unique.
        If not uniqueness is not possible, and is therefore not required
        """
        code = []
        while len(code) < length:
            random_number = random.randint(nr_low, nr_high)
            if nr_high - nr_low >= length:
                if random_number not in code:
                    code.append(random_number)
            else:
                code.append(random_number)
        return code

    def make_guess(self):
        """
        Method for getting a guess of the same lenght
        as the secret number, this method will run until
        a valid number sequence is entered
        """
        correct_number_values = False
        message = f'Enter a number of {self.length}' \
            f' numbers between {self.nr_low} and {self.nr_high}: '
        while not correct_number_values:
            guess = InputHandler.input_integer_sequence(message, self.length)
            for num in guess:
                if num >= self.nr_low and num <= self.nr_high:
                    correct_number_values = True
                else:
                    print(f'{num} is not within desired range,'\
                        f' {self.nr_low} and {self.nr_high}\n')
        return guess

    def check_code(self, secret_code, guessed_code):
        """
        This method compares the guessed number against the
        secret number generated. Will return feedback based on
        evaluated result
        """
        right_place = 0
        evaluate_code = []
        for guess, secret in zip(guessed_code, secret_code):
            if guess == secret:
                evaluate_code.append(str(guess))
                right_place += 1
            elif guess in secret_code:
                evaluate_code.append("C")
            else:
                evaluate_code.append("-")
        return right_place, evaluate_code

    def play(self):
        right_place = 0
        rounds = 0
        secret_code = self.secret_number(self.nr_low, self.nr_high, self.length)
        while right_place < len(secret_code):
            guessed_code = self.make_guess()
            right_place, evaluate_code = self.check_code(secret_code, guessed_code)
            print(f'Number of digits in the right place: {right_place}')
            print(f'Result of your last guess: {evaluate_code}')
            print()
            rounds += 1
        print(f'Mastermind was solved in {rounds} rounds.\nWell done!\n')
        return rounds
