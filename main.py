from abc import ABC, abstractmethod, abstractproperty
from itertools import chain, product

from Point import *
from Piece import *
from Color import *
from Board import *


def main():
    board = Board()
    board.print()

    print("--- Done ---")
    return
    
main()

"""
Notes:
- Moving notation: Ne3 f5 (seperate selects)
- Figure out:
    - Possible moves at any point

- Once selected: Make piece bold, perhaps different (background) color too
"""
