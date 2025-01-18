from pieces.piece import Piece
from colors import Color
import pygame

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

    def move(self, new_position):
        if self.is_valid_move(new_position):
            self.position = new_position
            self.hasMoved = True
        else:
            print("Invalid move")

    def is_valid_move(self, new_position):
        if self.position[0] == new_position[0] and abs(self.position[1] - new_position[1]) == 1:
            return True
        elif self.position[1] == new_position[1] and abs(self.position[0] - new_position[0]) == 1:
            return True
        elif abs(self.position[0] - new_position[0]) == 1 and abs(self.position[1] - new_position[1]) == 1:
            return True
        else:
            return False
