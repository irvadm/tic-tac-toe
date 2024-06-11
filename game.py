def draw_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')


def main():
    board = [' '] * 9
    draw_board(board)


if __name__ == '__main__':
    main()
