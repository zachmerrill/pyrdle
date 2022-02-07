import os

TITLE = 'PYRDLE'.center(20)
EMPTY = '⬚'


def print_board(board):
    for i in range(0, 5):
        print('   ', end='')
        for j in range(0, 5):
            print(board[i][j], end='  ')
        print('', end='\n')
    print()


def print_keyboard(keyboard):
    for i in range(0, 26):
        if i == 10:
            print('\n ', end='')
        if i == 19:
            print('\n   ', end='')
        print(keyboard[i], end=' ')
    print()


keyboard = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
            'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
board = [[EMPTY]*5 for i in range(6)]

# Game loop
while (True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[4m' + TITLE + '\033[0m' + '\n')
    print_board(board)
    print_keyboard(keyboard)
    guess = input('\n')
