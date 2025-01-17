from pieces.piece import Piece
class Rook(Piece):
    name = "Rook"
    def __init__(self, color, position):
        super().__init__(color, position)
