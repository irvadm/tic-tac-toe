import copy
import logging
import random
import sys


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s[%(lineno)d] - %(message)s')
logging.disable()


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


def get_computer_move(board, computer):
    """
    Determines the best move for the computer.
    It prioritizes moves, highest to lowest: winning move, blocking move,
    center move, corner move, side move.
    Returns None if no move is available.
    """

    if computer == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    empty_tiles = get_empty_tiles(board)
    # Return None if no moves are available
    if empty_tiles == []:
        return None

    # Check if a winning move is available
    logger.info('Check if a winning move is available:')
    for tile_pos in empty_tiles:
        board_copy = copy.copy(board)
        do_move(board_copy, tile_pos, computer)
        # Return winning move
        if wins(board_copy, computer):
            logger.info('Computer winning move: %s' % tile_pos)
            return tile_pos
    # Check if a blocking move is available
    logger.info('Check if a blocking move is available:')
    for tile_pos in empty_tiles:
        board_copy = copy.copy(board)
        do_move(board_copy, tile_pos, opponent)
        # Return blocking move
        if wins(board_copy, opponent):
            logger.info('Computer blocking move: %s' % tile_pos)
            return tile_pos

    # Check if center move is available
    if board[4] == ' ':
        return 4

    # Check if corner move is available
    for tile_pos in [0, 2, 6, 8]:
        if is_empty(board, tile_pos):
            return tile_pos
    
    # Check if side move is available
    for tile_pos in [1, 3, 5, 7]:
        if is_empty(board, tile_pos):
            return tile_pos

    # Return None if no moves are available
    return None


def get_empty_tiles(board) -> list[int]:
    empty_tiles = []
    for i, tile in enumerate(board):
        if board[i] == ' ':
            empty_tiles.append(i)
    return empty_tiles


def is_empty(board, move) -> bool:
    if board[move] == ' ':
        return True
    else:
        return False


def do_move(board, move, player):
    board[move] = player


def wins(board, player) -> bool:
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


def tie(board) -> bool:
    for tile in board:
        if tile == ' ':
            return False
    return True


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
            # Draw board
            draw_board(board)
            # Get and validate player move
            move = get_player_move()
            if move == 'quit':
                sys.exit(0)
            while not is_empty(board, move - 1):
                move = get_player_move()
            # print(f'Valid Move: {move}')
            do_move(board, move - 1, player)
            # Check if player won
            if wins(board, player):
                draw_board(board)
                print('You win!')
                break
            # Check if tie
            if tie(board):
                draw_board(board)
                print('It\'s a tie!')
                break
            # Switch turn
            turn = computer
        else:
            print('Computer\'s turn...')
            print()
            # Get computer move
            move = get_computer_move(board, computer)
            if move is None:
                if tie(board):
                    print('It\'s a tie!')
                    break
            do_move(board, move, computer)
            # Check if computer won
            if wins(board, computer):
                draw_board(board)
                print(f'Computer wins, you lose.')
                break
            # Switch turn
            turn = player


if __name__ == '__main__':
    main()
