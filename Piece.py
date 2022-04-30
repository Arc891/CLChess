from abc import ABC, abstractmethod, abstractproperty
from Point import *
from Color import *

class Piece(ABC):
    def __init__(self, pos: Point, color: Color):
        self.pos   = pos
        self.color = color

    def __str__(self):
        return self.color.code + self.name + "\x1b[0m"

    @abstractmethod
    def move(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass


class Pawn(Piece):
    def move(self):
        pass

    name = "p"
    
class Bishop(Piece):
    def move(self):
        pass

    name = "B"

class Knight(Piece):
    def move(self):
        pass

    name = "N"

class Rook(Piece):
    def move(self):
        pass

    name = "R"

class Queen(Piece):
    def move(self):
        pass

    name = "Q"

class King(Piece):
    def move(self):
        pass
    
    name = "K"


class Empty(Piece):
    def move(self):
        pass

    name = "."
