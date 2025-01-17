class Piece:
    def __init__(self, color, position=None):
        self.color = color
        self.position = position

    def move(self, newPosition):
        self.position = newPosition
