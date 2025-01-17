from pieces.piece import Piece

class King(Piece):
    name = "King"
    def __init__(self, color, position):
        super().__init__(color, position)
        self.hasMoved = False
