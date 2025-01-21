from pieces.piece import Piece
from colors import Color
import pygame
from files import files

class Knight(Piece):
    name = "Knight"
    def __init__(self, color, position):
        super().__init__(color, position)
        match color:
            case Color.WHITE:
                self.image = pygame.image.load("pieces/knight_white.png")
            case Color.BLACK:
                self.image = pygame.image.load("pieces/knight_black.png")
            case _:
                raise ValueError("Invalid color")
    
    def move(self, new_position, board):
        if not self.is_valid_move(new_position):
            raise ValueError("Invalid Move")
        self.position = new_position

    def is_valid_move(self, new_position):
        if (abs(self.position.rank - new_position.rank) == 2 and abs(files.index(self.position.file) - files.index(new_position.file))):
            return True
        elif (abs(self.position.rank - new_position.rank) == 1 and abs(files.index(self.position.file) - files.index(new_position.file))):
            return True
        else:
            return False