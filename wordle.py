import requests
import ast
import datetime

# URL of the official wordle list in the game code
WORDLE_URL = 'https://www.powerlanguage.co.uk/wordle/main.c1506a22.js'
# The day of the first wordle, for use in getting today's wordle
WORDLE_START_DATE = datetime.datetime(2021, 6, 19)
# Strings used to identify the start and end of the wordle lists
ANSWERS_START_STRING = 'var La='
LIST_DIVIDER = ',Ta='
ACCEPTED_START_STRING = ',Ia='


class Wordle:
    wotd = []
    accepted = []

    # Gets the official lists, returns a tuple
    # [0] = list of answers (in order)
    # [1] = list of accepted words
    def __init__(self):
        # Get the official lists
        content = requests.get(WORDLE_URL).text
        answers_start = content.find(ANSWERS_START_STRING)
        accepted_start = content.find(LIST_DIVIDER)
        accepted_end = content.find(ACCEPTED_START_STRING)
        # Initialize the accepted words list
        self.accepted = ast.literal_eval(
            content[accepted_start+len(LIST_DIVIDER):accepted_end])
        # Initialize the word of the day based on todays date
        answers = ast.literal_eval(
            content[answers_start+len(ANSWERS_START_STRING):accepted_start])
        self.wotd = answers[(datetime.datetime.now() - WORDLE_START_DATE).days]
