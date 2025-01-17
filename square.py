class Square:
    def __init__(self, position, piece=None):
        self.position = position
        self.piece = piece

    def isEmpty(self):
        return self.piece == None
