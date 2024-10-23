from random import randrange

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    #The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    y_axis = "+" + 7*"-" + "+" + 7*"-" + "+" + 7*"-" + "+"
    x_axis = "|" + 7*" " + "|" + 7*" " + "|" + 7*" " + "|"

    for z in range(len(board)):
        print(y_axis, x_axis, sep="\n")
        for w in board[z]:
            print("|" + " "*3 + str(w) + " "*2, end=" ")
        print("|", x_axis, end="\n", sep="\n")
    print(y_axis)
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    if board:
        try:
            user_play = int(input("Enter a number(0-9): "))
            if not user_play in range(1, 10):
                raise Exception("Only numbers between 1 and 9")
        except ValueError:
            print("Only enter integers")
        except:
            print("something else went wrong")
        
    print(user_play)

    
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []

    for x in range(len(board)):
        for y in range(len(board[x])):
            if type(board[x][y]) is int:
                free_fields.append((x, y))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    board_status = {"play": True, "winner": None}

    x_match = [[y for y in range(x, x + 3)] for x in range(0,8, 3)]
    y_match = [[y for y in range(x, 9, 3)] for x in range(0, 3, 1)]
    z_match = [[y for y in range(x, 9, 4)] for x in [0]]
    z_match.extend([[y for y in range(2, 8, 2)]])

    for x in [x_match, y_match, z_match]:       #ERR: this will still run after break
        for y in x:
            if y[0] == y[1] == y[2]:
                if y[0] == sign:
                    board_status["play"] = False
                    if sign == "O":
                        board_status["winner"] = sign
                    elif sign == "X":
                        board_status["winner"] = sign
                    break

    if len(make_list_of_free_fields(board)) == 0:
        board_status["play"] = False
        board_status["winner"] = None

    return board_status


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass


board[1][1] = "X" #computer play the first move
enter_move(victory_for(board, "X")["play"])
