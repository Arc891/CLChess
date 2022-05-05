from abc import ABC, abstractmethod, abstractproperty
from itertools import chain, product

from soupsieve import select

from Point import *
from Color import *
from BoardAndPieces import *

piece_names = ["p", "B", "N", "R", "Q", "K"]

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
        answer = input("Give the piece you want to select (f.e. Ng1): ")
        piece = answer[0]
        format_msg = "Enter: (p,B,N,R,Q,K)(a-g)(1-8), f.e. Qe3"
        
        if piece not in piece_names:
            print("That piece does not exist.", format_msg)
            continue

        try:
            pos = Point(colToInt[answer[1]], answer[2])
            assert(1 <= int(answer[2]) <= 8)
        except KeyError:
            print("That is not an existing column.", format_msg)
            continue
        except ValueError:
            print("That was not a existing row.", format_msg)
            continue

        selected_piece = board.board[pos.x-1][pos.y-1]
        
        if piece is not selected_piece.name:
            print("That piece does not exist there.")
            continue
        
        selected_piece = selected_piece.select(board)
        board.print()
        print("Selected: ", selected_piece, asSquare(pos))
        print()

        return selected_piece
    
def Move(board: Board, piece: Piece):
    print("Possible moves:")
    # sorted_moves = piece.possible_moves.sort(key=asSquare)
    # print(sorted_moves)
    moves_as_pos = []
    for x in piece.possible_moves:                   #TODO: If no possible moves, stop and give message
        print(x.pos, ":", asSquare(x.pos), end=" " ) #TODO: Add 'x' in front if taking piece
        moves_as_pos.append(x.pos)
    print()

    while True:
        answer = input("Give the location you want to move to (f.e. f3): ")
        pos = Point(colToInt[answer[0]], answer[1])
        print(pos)
        selected_piece = board.board[pos.x-1][pos.y-1]
        print(selected_piece)
        
        if pos not in moves_as_pos:
            print("That is not a possible move")
            continue
        
        selected_piece = selected_piece.select(board)
        board.print()
        print("Selected: ", selected_piece, asSquare(pos))
        print()

        return board
