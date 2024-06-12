import random
import sys


def draw_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')


def ask_player_letter():
    """
    Ask player if they want to be X or O.
    Returns player letter and computer letter.
    """
    while True:
        print('Do you want to be X or O?')
        player = input().upper()
        if player in ('X', 'O'):
            if player == 'X':
                return player, 'O'
            else:
                return player, 'X'


def who_goes_first():
    """Randomly decide who goes first."""
    random_number = random.randint(0, 1)
    if random_number == 0:
        return 'X'
    else:
        return 'O'


def get_player_move():
    while True:
        print('What is your move? (1-9 or "q" to quit)')
        move = input()
        if move in ('QUIT', 'quit', 'Q', 'q'):
            return 'quit'
        if len(move) == 1 and move in '123456789':
            return int(move)


def main():
    # Get player and computer letter
    player, computer = ask_player_letter()
    turn = who_goes_first()
    if turn == computer:
        print('The computer will go first.')
    else:
        print('You will go first.')

    board = [' '] * 9
    while True:
        if turn == player:
            print('Player turn')
            # Draw board
            draw_board(board)
            # Get player move
            move = get_player_move()
            print(f'Move: {move}')
            if move == 'quit':
                sys.exit(0)
            # Check if player won
            # Check if tie
            # Switch turn
            turn = computer
        else:
            print('Computer turn')
            # Get computer move
            # Check if computer won
            # Check if tie
            # Switch turn
            turn = player


if __name__ == '__main__':
    main()
