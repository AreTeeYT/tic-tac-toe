

def create_board():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    return board


def build_board(board):
    board_for_display = ''

    for line in board:
        board_for_display += '\n' + line[0] + '|' + line[1] + '|' + line[2]
        if line is not board[2]:
            board_for_display += "\n------"
    
    return board_for_display

def check_win(board):
    
    #checking horizontal wins
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] != ' ':
            if board[i][0] == board[i][2]:
                return True
        else:
            continue
    
    #check vertical wins
    checker = [0,1,2]
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] != ' ':
            if board[0][i] == board[2][i]:
                return True
        else:
            continue
             
    #check diagonal wins
    if board[0][0] == board[1][1] and board[0][0] != ' ':
        if board[0][0] == board[2][2]:
            return True
    
    if board[0][2] == board[1][1] and board[0][2] != ' ':
        if board[0][2] == board[2][0]:
            return True
    
    return False

def check_draw(board):
    for i in board:
        for j in i:
            if j == ' ':
                return True
    print("It's a TIE")
    return False

def player_input(player, board):

    row = int(input(f'{player}: Please enter a row (0-2)'))
    column = int(input(f'{player}: Please enter a column (0-2)'))
    try :
        if board[column][row] == ' ':
            board[column][row] = player
        else:
            print('please enter a valid location')
            player_input(player, board)
    except:
        print('please enter a valid location')
        player_input(player, board)
    



def main():
    board = create_board()
    playing = True
    #filling player board
    
    player1 = 'X'
    player2 = 'O'

    print(build_board(board))
    while playing:
        player_input(player1, board)
        print(build_board(board))
        if check_win(board):
            print('Player 1 wins')
            playing = False
            break
        playing = check_draw(board)
        player_input(player2, board)
        print(build_board(board))
        if check_win(board):
            print('Player 2 wins')
            playing = False
            break

    replay = input('To play again enter Y: ')

    if replay.upper() == 'Y':
        main()
        




main()