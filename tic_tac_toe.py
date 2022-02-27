
import time


def display_board(board):

    print("\n")
    print("       |      |      ")
    print("    {0}  |   {1}  |   {2}" .format(board[1], board[2], board[3]))
    print("       |      |      ")
    print("----------------------")
    print("       |      |      ")
    print("    {0}  |   {1}  |   {2}" .format(board[4], board[5], board[6]))
    print("       |      |      ")
    print("----------------------")
    print("       |      |      ")
    print("    {0}  |   {1}  |   {2}".format(board[7], board[8], board[9]))
    print("       |      |      ")


def display_possible_positions():

    print("\n")
    print("       |      |      ")
    print("    1  |   2  |   3")
    print("       |      |      ")
    print("----------------------")
    print("       |      |      ")
    print("    4  |   5  |   6")
    print("       |      |      ")
    print("----------------------")
    print("       |      |      ")
    print("    7  |   8  |   9")
    print("       |      |      ")
    print("This is how the board is laid out. Whenever the game asks you to input a position, this is what you refer "
          "to. Player One will always go first.")
    print("\n")


def player_selection():

    selection = "placeholder"
    acceptable_selections = ["X", "O"]

    while selection not in acceptable_selections:
        selection = input("Player One, select X or O: ")
        if selection in acceptable_selections:
            if selection == "X":
                return 'X', 'O'
            else:
                return 'O', 'X'
        else:
            print("Please input either X or O. Try Again.")


def insert_marker(board, marker, position):

    board[position] = marker
    return board


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board, position):

    return board[int(position)] == ' '


def full_board_check(board):

    for num in range(1, 10):
        if space_check(board, num):
            return False
    return True


def player_mark(board):

    acceptable_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    position = "placeholder"

    while position not in acceptable_positions:
        position = input("Select the position of your next mark (1 to 9): ")
        if position in acceptable_positions:
            if space_check(board, position):
                return int(position)
            else:
                print("Position is already filled. Try Again.")
                position = "placeholder"
        else:
            print("Please input a integer corresponding to a valid position (1 to 9). Try Again.")


def replay():

    acceptable_responses = ["Y", "N"]
    response = "placeholder"

    while response not in acceptable_responses:
        response = input("Would you like to play again? (Y for yes, N for no): ")
        if response in acceptable_responses:
            return response == "Y"
        else:
            print("Please use Y for yes, N for no. Try Again.")


print("Hello. Welcome to my rendition of Tic Tac Toe.")
time.sleep(2)
display_possible_positions()
time.sleep(2)
player1_mark, player2_mark = player_selection()

while True:

    game_on = True
    current_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    while game_on:
        turn = "Player One's"
        display_board(current_board)
        print(f"It is {turn} turn")
        insert_marker(current_board, player1_mark, player_mark(current_board))
        display_board(current_board)
        if win_check(current_board, player1_mark):
            print("Player One has won the game. Congratulations. ")
            game_on = False
            break
        else:
            if full_board_check(current_board):
                print("The game is a draw.")
                game_on = False
                break
            else:
                turn = "Player Two's"
        print(f"It is {turn} turn.")
        insert_marker(current_board, player2_mark, player_mark(current_board))
        if win_check(current_board, player2_mark):
            print("Player Two has won the game. Congratulations.")
            game_on = False
            break
        else:
            if full_board_check(current_board):
                print("The game is a draw.")
                game_on = False
                break
            else:
                turn = "Player One's"

    if not replay():
        break
