from pieces.piece import Piece
from colors import Color
import pygame

class Pawn(Piece):
    name = "Pawn"
    def __init__(self, color, position):
        super().__init__(color, position)
        self.has_moved = False
        match color:
            case Color.WHITE:
                self.image = pygame.image.load("pieces/pawn_white.png")
            case Color.BLACK:
                self.image = pygame.image.load("pieces/pawn_black.png")
            case _:
                raise ValueError("Invalid color")
    
    def move(self, new_position, board):
        if not self.is_valid_move(new_position):
            raise ValueError(f"Cannot move from {self.position} to {new_position}")
        self.position = new_position
    
    def is_valid_move(self, new_position):
        if self.color == Color.WHITE:
            if self.position.rank == 2:
                if (new_position.rank == 3 or new_position.rank == 4) and new_position.file == self.position.file:
                    return True
            elif new_position.rank - self.position.rank == 1 and new_position.file == self.position.file:
                return True
            else:
                return False
        else:
            if self.position.rank == 7:
                if (new_position.rank == 6 or new_position.rank == 5) and new_position.file == self.position.file:
                    return True
            elif self.position.rank - new_position.rank == 1 and new_position.file == self.position.file:
                return True
            else:
                return False
