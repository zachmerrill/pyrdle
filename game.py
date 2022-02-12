import os
from text import Text
from wordle import Wordle

# Wordle requirements
MAX_LETTERS = 5
MAX_GUESSES = 6


class Game:
    guess = ''
    guess_count = 0
    board = [['⬚']*5 for i in range(6)]
    keyboard = 'Q W E R T Y U I O P \n A S D F G H J K L \n  Z X C V B N M'
    keyboard_correct = []  # Stores the correct keys so we don't overwrite them
    wordle = Wordle()

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Text.apply('PYRDLE'.center(20), Text.UNDERLINE))
        print()
        for i in range(0, MAX_GUESSES):
            print('   ', end='')
            for j in range(0, MAX_LETTERS):
                print(self.board[i][j], end='  ')
            print('', end='\n')
        print()
        print(self.keyboard)
        print()

    def check_guess(self, word):
        if word not in self.wordle.accepted:
            return
        self.guess = word
        for i in range(0, 5):
            letter_upper = word[i].upper()
            if self.wordle.wotd[i] == word[i]:
                # Letter is in correct location
                correct_letter = Text.apply(letter_upper, Text.GREEN)
                self.board[self.guess_count][i] = correct_letter
                self.keyboard = self.keyboard.replace(
                    letter_upper, correct_letter)
                # Add letter to keyboard list so we don't overwrite later
                self.keyboard_correct.append(letter_upper)
            elif word[i] in self.wordle.wotd:
                # Letter is present but in incorrect location
                present_letter = Text.apply(letter_upper, Text.YELLOW)
                self.board[self.guess_count][i] = present_letter
                if word[i] not in self.keyboard_correct:
                    self.keyboard = self.keyboard.replace(
                        letter_upper, present_letter)
            else:
                # Letter is not present
                absent_letter = Text.apply(letter_upper, Text.RED)
                self.board[self.guess_count][i] = letter_upper
                self.keyboard = self.keyboard.replace(
                    letter_upper, absent_letter)
        self.guess_count += 1

    def __init__(self):
        self.print_board()

    def is_won(self):
        return self.wordle.wotd == self.guess
