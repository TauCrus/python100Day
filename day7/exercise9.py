import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('---+---+---')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('---+---+---')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def check_win(board):
    if board['TL'] == board['TM'] == board['TR'] != '   ':
        return True
    elif board['ML'] == board['MM'] == board['MR'] != '   ':
        return True
    elif board['BL'] == board['BM'] == board['BR'] != '   ':
        return True
    elif board['TL'] == board['ML'] == board['BL'] != '   ':
        return True
    elif board['TM'] == board['MM'] == board['BM'] != '   ':
        return True
    elif board['TR'] == board['MR'] == board['BR'] != '   ':
        return True
    elif board['TL'] == board['MM'] == board['BR'] != '   ':
        return True
    elif board['TR'] == board['MM'] == board['BL'] != '   ':
        return True
    else:
        return False


def main():
    init_board = {
        'TL': '   ', 'TM': '   ', 'TR': '   ',
        'ML': '   ', 'MM': '   ', 'MR': '   ',
        'BL': '   ', 'BM': '   ', 'BR': '   ',
    }
    '''
    init_board = {
        'TL': 'T L', 'TM': 'T M', 'TR': 'T R',
        'ML': 'M L', 'MM': 'M M', 'MR': 'M R',
        'BL': 'B L', 'BM': 'B M', 'BR': 'B R',
    }
    '''

    begin = True

    while begin:
        current_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        # os.system('clear')
        os.system('cls')

        print_board(current_board)
        while counter < 9:
            move = input('轮到%s走棋，请输入位置：' % turn)
            cur_turn = ' ' + turn + ' '
            if current_board[move] != ' o ' and current_board[move] != ' x ':
                counter += 1
                current_board[move] = cur_turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            # os.system('clear')
            os.system('cls')
            print_board(current_board)
            if check_win(current_board):
                print("%s is winner" % cur_turn)
                break
        choice = input('再玩一局？（yes|no）')
        begin = choice == 'yes'


if __name__ == "__main__":
    main()
