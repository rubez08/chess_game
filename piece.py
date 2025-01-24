from enum import IntFlag
class Piece(IntFlag):
    EMPTY = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6
    WHITE = 8
    BLACK = 16

    BLACK_PAWN = BLACK | PAWN
    WHITE_PAWN = WHITE | PAWN
    BLACK_ROOK = BLACK | ROOK
    WHITE_ROOK = WHITE | ROOK
    BLACK_KNIGHT = BLACK | KNIGHT
    WHITE_KNIGHT = WHITE | KNIGHT
    BLACK_BISHOP = BLACK | BISHOP
    WHITE_BISHOP = WHITE | BISHOP
    BLACK_QUEEN = BLACK | QUEEN
    WHITE_QUEEN = WHITE | QUEEN
    BLACK_KING = BLACK | KING
    WHITE_KING = WHITE | KING
    
    # def __init__(self, color, position=None):
    #     self.color = color
    #     self.position = position

    # def move(self, newPosition, board):
    #     self.position = newPosition
    
    # def is_valid_move(self, newPosition):
    #     return True
    
    # def is_obstructed(self, newPosition, board):
    #     return False
