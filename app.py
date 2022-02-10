import os

TITLE = 'PYRDLE'.center(20)
EMPTY = '⬚'
WORDLE = 'elder'.upper()
board = [[EMPTY]*5 for i in range(6)]
keyboard = 'Q W E R T Y U I O P \n A S D F G H J K L \n  Z X C V B N M'


def print_board(board):
    for i in range(0, 5):
        print('   ', end='')
        for j in range(0, 5):
            print(board[i][j], end='  ')
        print('', end='\n')
    print()


def update_row_and_keyboard(word, row):
    global keyboard
    for i in range(0, 5):
        if WORDLE[i] == word[i]:
            green = '\033[1;32;1m' + word[i] + '\033[0;0m'
            board[row][i] = green
            keyboard = keyboard.replace(
                word[i], green)
        elif word[i] in WORDLE:
            yellow = '\033[1;33;1m' + word[i] + '\033[0;0m'
            board[row][i] = yellow
            keyboard = keyboard.replace(
                word[i], yellow)
        else:
            red = '\033[1;31;1m' + word[i] + '\033[0;0m'
            board[row][i] = word[i]
            keyboard = keyboard.replace(
                word[i], red)


guess_count = 0

# Game loop
while (True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[4m' + TITLE + '\033[0m' + '\n')
    print()
    print_board(board)
    print(keyboard)
    guess = input('\n').upper()
    update_row_and_keyboard(guess, guess_count)
    if guess == WORDLE:
        print('\n\033[1;32;1m' + 'You won!' + '\033[0;0m')
        break
    guess_count += 1
