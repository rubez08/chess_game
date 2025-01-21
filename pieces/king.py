from pieces.piece import Piece
from colors import Color
import pygame
from files import files

class King(Piece):
    name = "King"
    def __init__(self, color, position):
        super().__init__(color, position)
        match color:
            case Color.WHITE:
                self.image = pygame.image.load("pieces/king_white.png")
            case Color.BLACK:
                self.image = pygame.image.load("pieces/king_black.png")
            case _:
                raise ValueError("Invalid color")
        self.hasMoved = False
        self.isInCheck = False

    def move(self, new_position, board):
        if not self.is_valid_move(new_position):
            raise ValueError("Invalid Move")
        self.position = new_position
        self.hasMoved = True


    def is_valid_move(self, new_position):
        if self.position.file == new_position.file and abs(self.position.rank - new_position.rank) == 1:
            return True
        elif self.position.rank == new_position.rank and abs(files.index(self.position.file) - files.index(new_position.file)) == 1:
            return True
        elif abs(files.index(self.position.file) - files.index(new_position.file)) == 1 and abs(self.position.rank - new_position.rank) == 1:
            return True
        else:
            return False
