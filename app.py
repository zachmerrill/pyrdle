import os
from text import Text
from wordle import Wordle

WORDLE = 'elder'.upper()

# Wordle requirements
MAX_LETTERS = 5
MAX_GUESSES = 6

# Initialize board
board = [['⬚']*5 for i in range(6)]
keyboard = 'Q W E R T Y U I O P \n A S D F G H J K L \n  Z X C V B N M'
keyboard_correct = []  # Stores the correct keys so we don't overwrite them


def print_board():
    global board
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Text.apply('PYRDLE'.center(20), Text.UNDERLINE))
    print()
    for i in range(0, MAX_GUESSES):
        print('   ', end='')
        for j in range(0, MAX_LETTERS):
            print(board[i][j], end='  ')
        print('', end='\n')
    print()
    print(keyboard)
    print()


def check_guess(word, row):
    global keyboard
    for i in range(0, 5):
        if WORDLE[i] == word[i]:
            # Letter is in correct location
            correct_letter = Text.apply(word[i], Text.GREEN)
            board[row][i] = correct_letter
            keyboard = keyboard.replace(
                word[i], correct_letter)
            # Add letter to keyboard list so we don't overwrite later
            keyboard_correct.append(word[i])
        elif word[i] in WORDLE:
            # Letter is present but in incorrect location
            present_letter = Text.apply(word[i], Text.YELLOW)
            board[row][i] = present_letter
            if word[i] not in keyboard_correct:
                keyboard = keyboard.replace(
                    word[i], present_letter)
        else:
            # Letter is not present
            absent_letter = Text.apply(word[i], Text.RED)
            board[row][i] = word[i]
            keyboard = keyboard.replace(
                word[i], absent_letter)


# Game loop
guess_count = 0
print_board()
while (True):
    if(guess_count == MAX_GUESSES):
        print(Text.apply('GAME OVER', Text.RED))
        break
    guess = input('\n').upper()
    check_guess(guess, guess_count)
    print_board()
    if guess == WORDLE:
        print(Text.apply('YOU WIN', Text.GREEN))
        break
    guess_count += 1
