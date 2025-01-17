from pieces.piece import Piece

class Bishop(Piece):
    name = "Bishop"
    def __init__(self, color, position):
        super().__init__(color, position)
