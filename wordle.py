import ast
import datetime

# The day of the first wordle, for use in getting today's wordle
WORDLE_START_DATE = datetime.datetime(2021, 6, 19)


class Wordle:
    wordle_number = 0
    wotd = ""
    accepted = []

    # Gets the official lists, returns a tuple
    # [0] = list of answers (in order)
    # [1] = list of accepted words
    def __init__(self):
        # Get the official list from our local file
        wordlistFile = open('wordlist.txt', 'r')
        self.accepted = wordlistFile.read().splitlines()
        # Initialize the word of the day based on todays date
        self.wordle_number = (datetime.datetime.now() -
                              WORDLE_START_DATE).days
        self.wotd = self.accepted[self.wordle_number]
