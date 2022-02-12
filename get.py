import requests
import ast

# URL of the official wordle list in the game code
WORDLE_URL = 'https://www.powerlanguage.co.uk/wordle/main.c1506a22.js'

# Gets the official lists, returns a tuple
# [0] = list of answers (in order)
# [1] = list of accepted words
def get_official_wordle_lists():
    content = requests.get(WORDLE_URL).text
    answers_start = content.find('var La=')
    accepted_start = content.find(',Ta=')
    accepted_end = content.find(',Ia=')
    return [ast.literal_eval(content[answers_start+7:accepted_start]), ast.literal_eval(content[accepted_start+4:accepted_end])]

