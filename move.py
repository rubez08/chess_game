from piece import Piece
class Move:
    def __init__(self, board, start, end, piece_moved):
        self.board = board
        self.start = start
        self.end = end
        self.piece_moved = piece_moved
        self.piece_captured = None
    
    def move(self):
        # If start and end are the same, place piece back on original square
        if self.end == self.start:
            self.board[self.start] = self.piece_moved
        # Else move piece from start to end
        else:
            self.board[self.end] = self.piece_moved
            self.board[self.start] = Piece.EMPTY

            