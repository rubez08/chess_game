from pieces.piece import Piece

class Knight(Piece):
    name = "Knight"
    def __init__(self, color, position):
        super().__init__(color, position)
