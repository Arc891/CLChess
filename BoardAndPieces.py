from abc import ABC, abstractmethod, abstractproperty
from itertools import chain, product

from Point import *
from Color import *

DEBUG = 1 

colToInt = {'a' : 1, 
            'b' : 2, 
            'c' : 3, 
            'd' : 4, 
            'e' : 5, 
            'f' : 6, 
            'g' : 7, 
            'h' : 8
}

class Board:
    def __init__(self):
        self.board: list[list[Piece]] = [[Empty(Point(x,y), NoColor) for y in range(1,9)] for x in range(1,9)]
        for y, x in product(range(1,9), range(1,9)):
            if DEBUG: print("x{0}, y{1}".format(x,y), end=" - ")
            pos = Point(x, y)
            if 2 < y < 7:
                if DEBUG: print("empty", self.board[x-1][y-1])
                continue
            
            color = White if y < 3 else Black
            if y == 2 or y == 7:
                self.board[x-1][y-1] = Pawn(pos, color)
                if DEBUG: print("pawn", self.board[x-1][y-1])
            else:
                if x == 1 or x == 8:
                    self.board[x-1][y-1] = Rook(pos, color)
                    if DEBUG: print("rook", self.board[x-1][y-1])

                elif x == 2 or x == 7:
                    self.board[x-1][y-1] = Knight(pos, color)
                    if DEBUG: print("knight", self.board[x-1][y-1])

                elif x == 3 or x == 6:
                    self.board[x-1][y-1] = Bishop(pos, color)
                    if DEBUG: print("bishop", self.board[x-1][y-1])

                elif x == 4:
                    self.board[x-1][y-1] = Queen(pos, color)
                    if DEBUG: print("queen", self.board[x-1][y-1])

                elif x == 5:
                    self.board[x-1][y-1] = King(pos, color)
                    if DEBUG: print("king", self.board[x-1][y-1])

    def print(self):
        print("\033c---- Board ----")
        print("- Player 2 (161660)")
        row = 8
        for y in range(7,-1,-1):
            for x in range(8):
                print(self.board[x][y], end=" ")
            print("\x1b[7m" + str(row) + " \x1b[0m")
            row -= 1
        for x in colToInt:
            print("\x1b[7m" + x, end=" \x1b[0m")
        print("\x1b[7m  \x1b[0m")
        print("- Player 1 (161660)")




class Piece(ABC):
    def __init__(self, pos: Point, color: Color):
        self.pos   = pos
        self.color = color

    def __str__(self):
        return self.color.code + self.name + "\x1b[0m"

    @abstractmethod
    def select(self, board: Board):
        pass

    @abstractmethod
    def move(self, board: Board):
        pass

    @property
    @abstractmethod
    def name(self):
        pass


class Pawn(Piece):
    def select(self, board: Board):
        # dir = 1 if self.color == White else -1
        self.name = self.color.selected + self.name
        return self
        
    def move(self, board: Board):
        pass

    name = "p"
    


class Bishop(Piece):
    def select(self, board: Board):
        pass

    def move(self, board: Board):
        pass

    name = "B"



class Knight(Piece):
    def select(self, board: Board):
        pass

    def move(self, board: Board):
        pass

    name = "N"



class Rook(Piece):
    def select(self, board: Board):
        pass

    def move(self, board: Board):
        pass

    name = "R"



class Queen(Piece):
    def select(self, board: Board):
        pass
    
    def move(self, board: Board):
        pass

    name = "Q"



class King(Piece):
    def select(self, board: Board):
        pass

    def move(self, board: Board):
        pass
    
    name = "K"



class Empty(Piece):
    def select(self, board: Board):
        pass

    def move(self, board: Board):
        pass

    name = "."
