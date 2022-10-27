def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    """Takes input from user and performs simple checks """
    
    choose = 0
    while choose != 'X' or choose != 'O':
        choose = input("Do you want to be X or O?\n").upper()
    
        if choose == 'X':
            #print("Player 1 will go first.")
            return "X"
        elif choose == 'O':
            #print("Player 2 will go first.")
            return "O"
        else:
            print("Incorrect input. Please choose X or O.")

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark): 
    return ((board[1] == board [2] == board [3] == mark) or
    (board[4] == board [5] == board [6] == mark) or
    (board[7] == board [8] == board [9] == mark) or
    (board[1] == board [5] == board [9] == mark) or
    (board[3] == board [5] == board [7] == mark) or
    (board[1] == board [4] == board [7] == mark) or
    (board[2] == board [5] == board [8] == mark) or
    (board[3] == board [6] == board [9] == mark))

from curses.ascii import isdigit
import random

def choose_first():
    return random.randint(1, 2)

def space_check(board, position):
    """Check if position is available or not"""
    return board[position] == ' '

def full_board_check(board):
    if board.count("O") == 5 or board.count("X") == 5:
        return True # True if full
    return False

def player_choice(board):
    """This function checks user input and provide a number from 1 to 9.
    Also, it will check does position is occupied or not."""
    
    choose = "WRONG"
    acceptable_range = range(0,10)
    within_range = False
    
    while choose.isdigit() == False or within_range == False:
        choose = input("Please enter next postion from 1 to 9.\n")

        if choose.isdigit() == False:
            print("This is not a digit. Please enter value from 1 to 9.")

        if choose.isdigit():
            if int(choose) in acceptable_range:
                if space_check(board, int(choose)):
                    return int(choose)
                else:
                    print("Position is occupied. Please choose available position.")
            else:
                print("Incorrect input. Number should be from 1 to 9.")
                within_range == False

def replay():
    
    while True:
        choose = input("Do you want to play again? (Y/N)")
        if choose == "Y":
            return True
        elif choose == "N":
            return False
        else:
            print("Incorrect input. Please enter Y or N.")

def game():
    print('Welcome to Tic Tac Toe!')

    board=[' ']*10

    while True:
        # Set the game up here
        marker = player_input() #which marker(X or O) will be the first
        #first = choose_first() #randomly generating which player goes first
        #print ("Player {} goes first".format(str(first)))
        #pass
        display_board(board)

        while True:

            #Player 1 Turn
            position = player_choice(board) #return position if it's available
            place_marker(board, marker, position)
        
            display_board(board)

            if win_check(board, marker): # check which player is win
                print("Player 1 is win!")
                board=[' ']*10
                break
        
            if full_board_check(board):
                print("Dead heat")
                break #check if board is full
        
            if marker == 'X':
                marker = "O"
            else:
                marker = "X"

            # Player2's turn.
            position = player_choice(board) #return position if it's available
            place_marker(board, marker, position)
        
            display_board(board)

            if win_check(board, marker): # check which player is win
                print("Player 2 is win!")
                board=[' ']*10
                break        
        
            if full_board_check(board):
                print("Dead heat")
                break #check if board is full
        
            if marker == 'X':
                marker = "O"
            else:
                marker = "X"
            #pass

        if not replay():
            break

game()