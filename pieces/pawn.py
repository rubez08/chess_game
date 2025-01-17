from pieces.piece import Piece

class Pawn(Piece):
    name = "Pawn"
    def __init__(self, color, position):
        super().__init__(color, position)
        self.has_moved = False
