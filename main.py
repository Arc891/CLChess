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

    piece = Select(board, sideToMove)
    Move(board, piece)

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
