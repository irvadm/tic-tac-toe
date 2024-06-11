import random


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


def main():
    # Get player and computer letter
    player, computer = ask_player_letter()
    turn = who_goes_first()
    if turn == computer:
        print('The computer will go first.')
    else:
        print('You will go first.')
    board = [' '] * 9
    draw_board(board)


if __name__ == '__main__':
    main()
