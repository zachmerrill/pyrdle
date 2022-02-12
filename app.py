from game import Game

if __name__ == '__main__':
    # Initialize the game
    game = Game()
    # Game loop
    while True:
        # Get the user's guess
        guess = input('Guess a word: ').lower()
        # Check the guess
        game.check_guess(guess)
        # Print the board
        game.print_board()
        # Check if the game is won
        if game.is_won():
            print('You won!\n')
            game.print_share()
            break
        # Check if the game is lost
        if game.is_lost():
            print('You lost!\n')
            game.print_share()
            break
