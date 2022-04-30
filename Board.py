from abc import ABC, abstractmethod, abstractproperty
from itertools import chain, product

from Point import *
from Piece import *
from Color import *

DEBUG = 0

class Board:
    def __init__(self):
        self.board: list[list[Piece]] = [[Empty(Point(x,y), NoColor) for y in range(1,9)] for x in range(1,9)]
        for y, x in product(range(1,9), range(1,9)):
            if DEBUG: print("x{0}, y{1}".format(x,y), end=" - ")
            pos = Point(x, y)
            if 2 < y < 7:
                if DEBUG: print("empty", self.board[8-y][8-x])
                continue
            
            color = White if y < 3 else Black
            if y == 2 or y == 7:
                self.board[8-y][8-x] = Pawn(pos, color)
                if DEBUG: print("pawn", self.board[8-y][8-x])
            else:
                if x == 1 or x == 8:
                    self.board[8-y][8-x] = Rook(pos, color)
                    if DEBUG: print("rook", self.board[8-y][8-x])
                elif x == 2 or x == 7:
                    self.board[8-y][8-x] = Knight(pos, color)
                    if DEBUG: print("knight", self.board[8-y][8-x])
                elif x == 3 or x == 6:
                    self.board[8-y][8-x] = Bishop(pos, color)
                    if DEBUG: print("bishop", self.board[8-y][8-x])
                elif x == 4:
                    self.board[8-y][8-x] = Queen(pos, color)
                    if DEBUG: print("queen", self.board[8-y][8-x])
                elif x == 5:
                    self.board[8-y][8-x] = King(pos, color)
                    if DEBUG: print("king", self.board[8-y][8-x])

    def print(self):
        print("--- Board ---")
        for x in self.board:
            for y in x:
                print(y, end=" ")
            print()