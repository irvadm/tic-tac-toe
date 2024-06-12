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


def is_valid(board, move) -> bool:
    if board[move] == ' ':
        return True
    else:
        return False


def do_move(board, move, player):
    board[move] = player


def wins(board, player):
    # Check for horizontal win
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    
    # Check for vertical win
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[5] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    
    # Check for diagonal win
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


def main():
    # Get player and computer letter
    player, computer = ask_player_letter()
    turn = who_goes_first()
    if turn == computer:
        print('The computer will go first.')
    else:
        print('You will go first.')

    board = [' '] * 9
    # board = ['X', 'O', 'X', ' ', ' ', ' ', 'O', 'X', 'O']
    while True:
        if turn == player:
            print('Player turn')
            # Draw board
            draw_board(board)
            # Get and validate player move
            move = get_player_move()
            if move == 'quit':
                sys.exit(0)
            while not is_valid(board, move - 1):
                move = get_player_move()
            print(f'Valid Move: {move}')
            do_move(board, move - 1, player)
            # Check if player won
            if wins(board, player):
                print('You win!')
                break
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
