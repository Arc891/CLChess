from abc import ABC, abstractmethod, abstractproperty

from Point import Point
from Piece import *
from Color import *

class Board:
    def __init__(self):
        self.board = [[Point(x, y) for x in range(1,9)] for y in range(8,0,-1)]
    
    def print(self):
        for x in self.board:
            for y in x:
                print(y, end=" ")
            print()


def main():
    board = Board()
    board.print()
    

main()

"""
Notes:
- Moving notation: Ne3 f5 (seperate selects)
- Figure out:
    - Colors
    - Bolding
    - Possible moves at any point

- Once selected: Make piece bold, perhaps different (background) color too
"""
