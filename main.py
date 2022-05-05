from abc import ABC, abstractmethod, abstractproperty
from itertools import chain, product

from Point import *
from Color import *
from BoardAndPieces import *
from Select import *


def main():
    board = Board()
    board.print()

    turn = 1
    sideToMove = White

    while turn < 2:
        piece = Select(board, sideToMove)
        board = Move(board, piece)
        if sideToMove == Black: turn += 1
        if sideToMove == White: sideToMove = Black
    
    
    # board.print()

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
