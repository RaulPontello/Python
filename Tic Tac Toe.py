## Tic Tac Toe game ##
# How to play: type the position (1, 2,..., 9) where you want to place the marker

# 1) Importing

import random
import time

# 2) Functions

def board(game_list):
    """
    Function to create the board and print it
    :param: string of the movements done
    :return: none
    """
    print('   {:^5} | {:^5} | {:^5}' .format(game_list[7], game_list[8], game_list[9]))
    print('   {:^5} | {:^5} | {:^5}' .format('-' * 5, '-' * 5, '-' * 5))
    print('   {:^5} | {:^5} | {:^5}'.format(game_list[4], game_list[5], game_list[6]))
    print('   {:^5} | {:^5} | {:^5}' .format('-' * 5, '-' * 5, '-' * 5))
    print('   {:^5} | {:^5} | {:^5}'.format(game_list[1], game_list[2], game_list[3]))

def player_marker():
    """
    Function do define the marker of the two players
    :param: none
    :return: tuple (Player 1, Player 2)
    """
    marker = input('Player 1, choose your marker (X/0): ').strip().upper()

    # Validation
    while marker != 'X' and marker != '0':
        marker = input('Typing error, choose again (X/0): ').strip().upper()

    if marker == 'X':
        return ('X', '0')

    elif marker == '0':
        return ('0', 'X')

def start_game():
    """
    Function to decide who begins playing
    :param: none
    :return: start
    """
    start = str(input('Do you want to begin (Y/N) ? ')).strip().upper()  # Definition of who begins playing

    # Validation
    while start != 'Y' and start != 'N':
        start = str(input('Typing error, choose again (Y/N) ? ')).strip().upper()

    return start

def place_marker(start, move, move_option):
    """
    Function to place the player marker in the correct place of the board
    :param: start: Defines who starts playing, move: 9 turns
    :return: none
    """
    if (start == 'Y' and move % 2 != 0) or (start == 'N' and move % 2 == 0):
        print('Your turn')

        while True:
            try:
                placement = int(input('Where do you want to play: '))
                move_option.remove(placement)
                game_list[placement] = player1

            except (TypeError, ValueError):
                print('Typing error, choose again ')
                continue

            else:
                break

    elif (start == 'Y' and move % 2 == 0) or (start == 'N' and move % 2 != 0):
        print('Computer turn')
        placement = random.choice(move_option)
        move_option.remove(placement)
        game_list[placement] = player2

def win_check(game_list, player1, player2):
    """
    Function to check if the game is over
    :param: game_list: List of the ordered moves done, markers(player1, player2)
    :return: none
    """
    global game_over

    if game_list[1] == game_list[2] == game_list[3] == player1 or \
        game_list[4] == game_list[5] == game_list[6] == player1 or \
        game_list[7] == game_list[8] == game_list[9] == player1 or \
        game_list[1] == game_list[4] == game_list[7] == player1 or \
        game_list[2] == game_list[5] == game_list[8] == player1 or \
        game_list[3] == game_list[6] == game_list[9] == player1 or \
        game_list[1] == game_list[5] == game_list[9] == player1 or \
        game_list[3] == game_list[5] == game_list[7] == player1:
            time.sleep(1)
            print('')
            print('-=' * 30)
            print('You win, game over !')
            print('-=' * 30)
            game_over = True

    elif game_list[1] == game_list[2] == game_list[3] == player2 or \
        game_list[4] == game_list[5] == game_list[6] == player2 or \
        game_list[7] == game_list[8] == game_list[9] == player2 or \
        game_list[1] == game_list[4] == game_list[7] == player2 or \
        game_list[2] == game_list[5] == game_list[8] == player2 or \
        game_list[3] == game_list[6] == game_list[9] == player2 or \
        game_list[1] == game_list[5] == game_list[9] == player2 or \
        game_list[3] == game_list[5] == game_list[7] == player2:
            time.sleep(1)
            print('')
            print('-=' * 30)
            print('Computer wins, game over !')
            print('-=' * 30)
            game_over = True

def draw_ckeck():
    """
    Function to check if there is a draw
    :return: none
    """
    global game_over

    if '' not in game_list and game_over == False:
        time.sleep(1)
        print('')
        print('No winner !')
        game_over = True


# 3) Main code

game_list = ['#', '', '', '', '', '', '', '', '', '']   # List of the ordered moves done
move_option = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # Possible placement of the markers
player1, player2 = player_marker()   # Runs player_input() to define the markers
game_over = False   # Verification if the game is over or not
start = start_game()
print('Loading game...')

for move in range(1, 10):   # game starts: 10 turns
    time.sleep(2)
    print('')
    print('-' * 30)
    place_marker(start, move, move_option)
    time.sleep(2)
    print('')
    board(game_list)
    win_check(game_list, player1, player2)
    draw_ckeck()

    if game_over == True:
        break



