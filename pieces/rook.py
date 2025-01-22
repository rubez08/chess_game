from pieces.piece import Piece
from colors import Color
import pygame
from position import Position
from files import files

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
    
    def move(self, new_position, board):
        if not self.is_valid_move(new_position):
            raise ValueError("Invalid Move")
        if self.is_obstructed(new_position, board):
            raise ValueError("There is a piece in the way")
        self.position = new_position
        self.hasMoved = True
    
    def is_valid_move(self, new_position):
        if self.position.rank == new_position.rank:
            return True
        elif self.position.file == new_position.file:
            return True
        else:
            return False
    
    def is_obstructed(self, newPosition, board):
        if self.position.rank == newPosition.rank:
            if files.index(self.position.file) < files.index(newPosition.file):
                for i in range(files.index(self.position.file) + 1, files.index(newPosition.file)):
                    position_to_check = Position(files[i], self.position.rank)
                    if board.get_piece_at_position(position_to_check) is not None:
                        return True
            elif (files.index(self.position.file) > files.index(newPosition.file)):
                for i in range(files.index(newPosition.file) + 1, files.index(self.position.file)):
                    position_to_check = Position(files[i], self.position.rank)
                    if board.get_piece_at_position(position_to_check) is not None:
                        return True
        elif self.position.file == newPosition.file:
            if self.position.rank < newPosition.rank:
                for i in range(self.position.rank + 1, newPosition.rank):
                    position_to_check = Position(self.position.file, i)
                    if board.get_piece_at_position(position_to_check) is not None:
                        return True
            elif self.position.rank > newPosition.rank:
                for i in range(newPosition.rank + 1, self.position.rank):
                    position_to_check = Position(self.position.file, i)
                    if board.get_piece_at_position(position_to_check) is not None:
                        return True
        return False