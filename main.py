import time
import copy

from Point import *
from Color import *
from BoardAndPieces import *
from Select import *


def main():
    turn = 1
    sideToMove = White
    gameOver = False
    moves = []

    board = Board()
    board.print(turn, sideToMove, moves)

    while not gameOver:
        move_str = ""
        old_board = copy.deepcopy(board)

        # --- Player selects a piece --- #
        piece = Select(board, sideToMove)
        board.print(turn, sideToMove, moves)
        print("Selected: ", piece, asSquare(piece.pos))
        print()

        old_piece = copy.deepcopy(piece)

        # --- Player moves piece --- #
        outcome = Move(board, piece)

        if sideToMove == White: move_str += (str(turn) + ".")
        move_str += piece.def_name
        
        board = outcome[0]
        new_piece = outcome[1]

        if old_board.board[new_piece.pos.x-1][new_piece.pos.y-1].color.name != NoColor.name:
            if piece.def_name == "p":
                move_str = move_str.replace("p",asSquare(old_piece.pos)[0])
            move_str += "x"

        move_str = move_str.replace("p", "") 
        move_str += asSquare(new_piece.pos)

        moves.append(move_str)
        
        if sideToMove == Black: 
            turn += 1
            sideToMove = White

        elif sideToMove == White: 
            sideToMove = Black
    
        board.print(turn, sideToMove, moves)
        print("Moved:", piece, "to", asSquare(piece.pos))
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
