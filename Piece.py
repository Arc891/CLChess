from main import *
from abc import ABC, abstractmethod, abstractproperty

class Piece(ABC):
    def __init__(self, pos: Point, color: Color):
        self.pos   = pos
        self.color = color

    @abstractmethod
    def move(self):
        pass



class Pawn(Piece):
    def move(self):
        pass
    
class Bishop(Piece):
    def move(self):
        pass

class Knight(Piece):
    def move(self):
        pass

class Rook(Piece):
    def move(self):
        pass

class Queen(Piece):
    def move(self):
        pass

class King(Piece):
    def move(self):
        pass