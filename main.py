from Point import *
from Color import *
from BoardAndPieces import *
from Select import *


def main():
    turn = 1
    sideToMove = White

    board = Board()
    board.print(turn, sideToMove)

    while turn < 4:
        piece = Select(board, sideToMove)
        board.print(turn, sideToMove)
        print("Selected: ", piece, asSquare(piece.pos))
        print()

        outcome = Move(board, piece)
        board = outcome[0]

        if not outcome[1]:
            board.print(turn, sideToMove)
            print("This piece has no possible moves, select another piece.")
            print()
            continue
        
        if sideToMove == Black: 
            turn += 1
            sideToMove = White

        elif sideToMove == White: 
            sideToMove = Black
    
        board.print(turn, sideToMove)
        print("Moved: ", piece, "to", asSquare(piece.pos))
        print()
    
    # board.print(turn, sideToMove)

    print("  ---- Done  ----")
    return
    
main()

"""
Notes:
- Moving notation: Ne3 f5 (seperate selects)
- Figure out:
    - Possible moves at any point

- Once selected: Make piece bold, perhaps different (background) color too
"""
