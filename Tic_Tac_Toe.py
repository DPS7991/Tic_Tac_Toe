import random
from IPython.display import clear_output


def display_board(board):
    '''
        Function that prints out the board. The board is set up as a list where each index (1-9) corresponds with a number on a number pad. The result is a 3 x 3 board.
        '''
    clear_output()
    print('_____________')
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print('_____________')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print('_____________')
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print('_____________')


def player_input():
    '''
    Function takes in a player input and assigns their marker as 'X' or 'O'.
    '''
    player1_choice = ''
    player2_choice = ''

    while player1_choice not in ['X', 'O']:
        player1_choice = input("Player 1, Do you want to be X or O: ").upper()

        if player1_choice not in ['X', 'O']:
            clear_output()
            print('Please make sure to be X or O.')

    if player1_choice == 'X':
        player2_choice = 'O'
    else:
        player2_choice = 'X'

    return (player1_choice, player2_choice)


def place_marker(board, marker, position):
    '''
    Functions takes in the parameters: board, marker ('X' or 'O'), and a desired position (# 1-9).
    It then assigns the marker in the desired position on the board
    '''
    board[position] = marker


def win_check(board, mark):
    '''
    Function checks to see if the mark ('X' or 'O') has won
    '''
    win = list(mark * 3)
    return (win == board[1:4] or win == board[4:7] or win == board[7:10] or win == board[1:10:3] or
            win == board[2:10:3] or win == board[3:10:3] or win == board[1:10:4] or win == board[3:10:2])


def choose_first():
    '''
    Function that randomly decides which player goes first.
    '''
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    '''
    Function checks to see if there is an available space on the board.
    '''
    return board[position] == ' '


def full_board_check(board):
    '''
    Function checks to see if the board is full.
    '''
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    '''
    Function asks for player's next postion (# 1-9), and then uses the space_check function to check if the positon is free
    '''
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    '''
    Function that asks the player if they want to play again
    '''
    if input('Do you want to play again? Enter Yes or No: ').lower().startswith('y'):
        return True
    else:
        print('Thanks for playing!')
        return False

# The running of the game.


print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' '] * 10
    player1_choice, player2_choice = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_choice, position)

            if win_check(the_board, player1_choice):
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break

                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_choice, position)

            if win_check(the_board, player2_choice):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
