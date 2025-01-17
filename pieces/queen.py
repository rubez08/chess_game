from pieces.piece import Piece
class Queen(Piece):
    name = "Queen"
    def __init__(self, color, position):
        super().__init__(color, position)
