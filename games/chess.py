board = [[None for y in range(8)] for x in range(8)]

def pawn_init(color):

    location = 1 if color == "white" else 6
    pawn = "white" if color == "white" else "black"
    
    for x in range(8):
        board[x][location] = pawn + " pawn"

pawn_init("white")
pawn_init("black")


rook_init = [[1,0], [0, 7], [7, 0], [7, 7]]

def init_chess_piece(indices):
    for x in indices:
        board[x[0]][x[1]] = "rook"
        
init_chess_piece(rook_init)
print(board)
