from pieces.piece import Piece
from colors import Color
import pygame
from files import files
from position import Position

class Bishop(Piece):
    name = "Bishop"
    def __init__(self, color, position):
        super().__init__(color, position)
        match color:
            case Color.WHITE:
                self.image = pygame.image.load("pieces/bishop_white.png")
            case Color.BLACK:
                self.image = pygame.image.load("pieces/bishop_black.png")
            case _:
                raise ValueError("Invalid color")
    
    def move(self, new_position, board):
        if not self.is_valid_move(new_position):
            raise ValueError(f"Bishop cannot move from {self.position} to {new_position}")
        elif self.is_obstructed(new_position, board):
            raise ValueError(f"Path is obstructed from {self.position} to {new_position}")
        self.position = new_position
    
    def is_valid_move(self, new_position):
        if (abs(self.position.rank - new_position.rank) == abs(files.index(self.position.file) - files.index(new_position.file))):
            return True
        else:
            return False
    
    def is_obstructed(self, newPosition, board):
        # Determine the direction of the move
        rank_dir = 1 if newPosition.rank > self.position.rank else -1
        file_dir = 1 if files.index(newPosition.file) > files.index(self.position.file) else -1
        # Check if there is a piece in the path
        for i in range(1, abs(newPosition.rank - self.position.rank)):
            position_to_check = Position(files[files.index(self.position.file) + (i * file_dir)], self.position.rank + (i * rank_dir))
            if board.get_piece_at_position(position_to_check) is not None:
                return True
        return False