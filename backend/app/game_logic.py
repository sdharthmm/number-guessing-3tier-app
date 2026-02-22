# game_logic.py

import random
print("LOADING GAME LOGIC")


# This class will manage one game session
class NumberGuessingGame:

    def __init__(self):
        # Generate a random number between 1 and 100
        self.secret_number = random.randint(1, 100)

        # Track number of attempts
        self.attempts = 0

        # Game state
        self.is_over = False


    def guess(self, number: int):
        """
        Accepts a guessed number and returns result message.
        """

        if self.is_over:
            return "Game already finished"

        # Increment attempt count
        self.attempts += 1

        if number < self.secret_number:
            return "Too low"

        elif number > self.secret_number:
            return "Too high"

        else:
            self.is_over = True
            return "Correct"