from pieces.piece import Piece
from colors import Color
import pygame

class Rook(Piece):
    name = "Rook"
    def __init__(self, color, position):
        super().__init__(color, position)
        match color:
            case Color.WHITE:
                self.image = pygame.image.load("pieces/rook_white.png")
            case Color.BLACK:
                self.image = pygame.image.load("pieces/rook_black.png")
            case _:
                raise ValueError("Invalid color")
    
    def move(self, new_position):
        if not self.is_valid_move(new_position):
            raise ValueError("Invalid Move")
        self.position = new_position
        self.hasMoved = True
    
    def is_valid_move(self, new_position):
        return True