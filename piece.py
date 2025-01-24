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
    
    # def __init__(self, color, position=None):
    #     self.color = color
    #     self.position = position

    # def move(self, newPosition, board):
    #     self.position = newPosition
    
    # def is_valid_move(self, newPosition):
    #     return True
    
    # def is_obstructed(self, newPosition, board):
    #     return False
