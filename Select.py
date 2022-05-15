import random

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

def randomLocation() -> str:
    result: str = ""
    piecenum = random.randint(0,len(piece_names)-1)
    piece = piece_names[piecenum] 
    col = getKey(colToInt, random.randint(1, 8))
    row = random.randint(1,8)
    result += piece + col + str(row)
    return result

# def updateMoves():


def Select(board: Board, sideToMove: Color) -> Piece:
    while True:
        format_msg = "Enter: (p,B,N,R,Q,K)(a-g)(1-8), f.e. " + randomLocation()

        answer = input("Give the piece you want to select: ")

        if answer == "qq":
            exit(0)

        if len(answer) < 3:
            print("Please enter a piece and location.", format_msg)
            continue

        piece = answer[0]
        
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

        selected_piece: Piece = board.board[pos.x-1][pos.y-1]
        
        if piece is not selected_piece.name:
            print("That piece does not exist there.")
            continue
        elif selected_piece.color != sideToMove:
            print("That is not your piece!")
            continue
        
        selected_piece = selected_piece.select(board)

        if len(selected_piece.possible_moves) == 0:
            selected_piece = selected_piece.move(board, selected_piece.pos)
            print("This piece has no possible moves, choose another")
            print()
            continue

        return selected_piece
    
def Move(board: Board, piece: Piece) -> tuple[Board, Piece]:
    print("Possible moves:")
    sorted_moves = []
    pieces_as_pos = []

    for x in piece.possible_moves:
        takes = ""
        if x.color is not NoColor: takes = "x" 
        pieces_as_pos.append(x.pos)
        sorted_moves.append(takes + asSquare(x.pos))
    
    sorted_moves = sorted(sorted_moves)

    for x in sorted_moves:
        print(x, end=" ")
    
    print()

    while True:
        answer = input("Give the location you want to move to: ")

        if answer == "qq":
            exit(0)

        if len(answer) < 2:
            print("Please enter a position.")
            continue
        
        answer = answer.replace("x", "")

        try:
            pos = Point(colToInt[answer[0]], answer[1])
            assert(1 <= int(answer[1]) <= 8)
        except KeyError:
            print("That is not an existing column.")
            continue
        except ValueError:
            print("That was not a existing row.")
            continue

        print(pos)
        selected_piece: Piece = board.board[pos.x-1][pos.y-1]
        print(selected_piece)
        
        if pos not in pieces_as_pos:
            print("That is not a possible move.")
            continue
        
        selected_piece = piece.move(board, pos)

        return (board, selected_piece)
