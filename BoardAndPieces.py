from abc import ABC, abstractmethod
from itertools import chain, product
import time

from Point import *
from Color import *

DEBUG = 1 
COLOR_RESET = "\x1b[0m"
EDGE_COLOR = "\x1b[7m"

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

    def print(self, turn: int, sideToMove: Color):
        def print_letters():
            print(EDGE_COLOR + "  ", end = "")
            for x in colToInt:
                print(x, end=" ")
            print("  " + COLOR_RESET)
        
        print("\033c") # Clears terminal
        print("  ---- Board ----")
        print("- Player 2 (161660)")
        
        # Top row / letters
        print_letters()

        for y in range(7,-1,-1):
            print(EDGE_COLOR + str(y+1), end=" " + COLOR_RESET) #Left side / numbers
            
            for x in range(8):
                print(self.board[x][y], end=" ") #The pieces
            
            print(EDGE_COLOR + str(y+1) + " " + COLOR_RESET) #Right side / numbers

        print_letters()
        print("- Player 1 (161660)")
        print("Turn:", turn)
        print("Side to move:", end=" ")
        print(sideToMove)




class Piece(ABC):
    def __init__(self, pos: Point, color: Color):
        self.pos   = pos
        self.color = color
        self.possible_moves = []

    def __str__(self):
        return self.color.code + self.name + COLOR_RESET


    @abstractmethod
    def select(self, board: Board, check: int=0):
        pass


    @abstractmethod
    def move(self, board: Board, pos: Point):
        pass


    @property
    @abstractmethod
    def name(self) -> str: 
        pass

    @property
    @abstractmethod
    def def_name(self) -> str: 
        pass
    



class Pawn(Piece):
    def select(self, board: Board, check: int=0):
        # dir = 1 if self.color == White else -1
        self.name = self.color.selected + self.name
        return self
        
    def move(self, board: Board, pos: Point):
        pass
    
    def_name = "p"
    name = def_name
    


class Bishop(Piece):
    def select(self, board: Board, check: int=0):
        self.name = self.color.selected + self.name
        return self

    def move(self, board: Board, pos: Point):
        pass

    def_name = "B"
    name = def_name



class Knight(Piece):
    def select(self, board: Board, check: int=0):
        possible_jumps =   [Point(1,2),  Point(1,-2), 
                            Point(2,1),  Point(2,-1), 
                            Point(-1,2), Point(-1,-2), 
                            Point(-2,1), Point(-2,-1)]
        
        self.possible_moves = []

        for x in possible_jumps:
            newpos = self.pos + x
            
            if not newpos.isLegal():
                continue

            cur_piece = board.board[newpos.x-1][newpos.y-1]
            if  cur_piece.color != self.color:
                self.possible_moves.append(cur_piece)

                if not check: cur_piece.name = cur_piece.color.selected + cur_piece.name
        
        if not check: self.name = self.color.selected + self.name
        return self

    def move(self, board: Board, newpos: Point):
        board.board[self.pos.x-1][self.pos.y-1] = Empty(self.pos, NoColor)
        
        for x in self.possible_moves:
            x.name = x.def_name

        self.possible_moves = []
        self.pos = newpos
        self.name = self.def_name
        board.board[newpos.x-1][newpos.y-1] = self
        return self
    

    def_name = "N"
    name = def_name




class Rook(Piece):
    def select(self, board: Board, check: int=0):
        self.name = self.color.selected + self.name
        return self

    def move(self, board: Board, pos: Point):
        pass

    def_name = "R"
    name = def_name



class Queen(Piece):
    def select(self, board: Board, check: int=0):
        self.name = self.color.selected + self.name
        return self
    
    def move(self, board: Board, pos: Point):
        pass

    def_name = "Q"
    name = def_name



class King(Piece):
    def select(self, board: Board, check: int=0):
        self.name = self.color.selected + self.name
        return self

    def move(self, board: Board, pos: Point):
        pass
    
    def_name = "K"
    name = def_name



class Empty(Piece):
    def select(self, board: Board, check: int=0):
        pass

    def move(self, board: Board, pos: Point):
        pass

    def_name = "."
    name = def_name
