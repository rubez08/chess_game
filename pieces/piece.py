class Piece:
    def __init__(self, color, position=None):
        self.color = color
        self.position = position

    def move(self, newPosition, board):
        self.position = newPosition
    
    def is_valid_move(self, newPosition):
        return True
    
    def is_obstructed(self, newPosition):
        return False
