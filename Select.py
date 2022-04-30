from abc import ABC, abstractmethod, abstractproperty
from itertools import chain, product

from Point import *
from Color import *
from BoardAndPieces import *

colToInt = {'a' : 1, 
            'b' : 2, 
            'c' : 3, 
            'd' : 4, 
            'e' : 5, 
            'f' : 6, 
            'g' : 7, 
            'h' : 8
}

def Select(board: Board, sideToMove: Color):
    while True:
        answer = input("Give the piece you want to move (f.e. Ne3):")
        piece = answer[0]
        pos = Point(colToInt[answer[1]], answer[2])
        
        if piece is not board.board[pos.x-1][pos.y-1].name:
            print("That piece does not exist there")
            continue
        
        board.board[pos.x-1][pos.y-1] = board.board[pos.x-1][pos.y-1].select(board)
        board.print()
        print("Selected: ", board.board[pos.x-1][pos.y-1], asSquare(pos))
        print()

        return board
    

