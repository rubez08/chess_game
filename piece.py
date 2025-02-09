from enum import IntFlag
class Piece(IntFlag):
    EMPTY = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6
    STRIP_COLOR = 7
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

    def is_white(self):
        return self & Piece.WHITE == Piece.WHITE
    
    def is_black(self):
        return self & Piece.BLACK == Piece.BLACK
    
    def is_same_color(self, other):
        if self == Piece.EMPTY or other == Piece.EMPTY:
            return False
        return self & Piece.WHITE == other & Piece.WHITE
    
    def is_opposite_color(self, other):
        if self == Piece.EMPTY or other == Piece.EMPTY:
            return False
        return self & Piece.WHITE != other & Piece.WHITE
    
    def is_king(self):
        return self & Piece.STRIP_COLOR == Piece.KING
    
    def is_rook(self):
        return self & Piece.STRIP_COLOR == Piece.ROOK
    
    def is_queen(self):
        return self & Piece.STRIP_COLOR == Piece.QUEEN
    
    def is_bishop(self):
        return self & Piece.STRIP_COLOR == Piece.BISHOP
    
    def is_knight(self):
        return self & Piece.STRIP_COLOR == Piece.KNIGHT
    
    def is_pawn(self):
        return self & Piece.STRIP_COLOR == Piece.PAWN
    
    