from pieces.piece import Piece
from colors import Color
import pygame
from position import Position
from files import files

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
        if not self.is_valid_move(new_position, board):
            raise ValueError(f"Cannot move from {self.position} to {new_position}")
        is_double_move = False
        if abs(self.position.rank - new_position.rank) == 2:
            is_double_move = True
        if self.is_obstructed(new_position, board, is_double_move):
            raise ValueError(f"There is a piece in the way")
        self.position = new_position
    
    def is_valid_move(self, new_position, board):
        if self.color == Color.WHITE:
            if self.position.rank == 2:
                if (new_position.rank == 3 or new_position.rank == 4) and new_position.file == self.position.file:
                    return True
            elif new_position.rank - self.position.rank == 1 and new_position.file == self.position.file:
                return True
            elif new_position.rank - self.position.rank == 1 and abs(files.index(new_position.file) - files.index(self.position.file)) == 1 and board.get_piece_at_position(new_position) is not None:
                return True
            else:
                return False
        elif self.color == Color.BLACK:
            if self.position.rank == 7:
                if (new_position.rank == 6 or new_position.rank == 5) and new_position.file == self.position.file:
                    return True
            elif self.position.rank - new_position.rank == 1 and new_position.file == self.position.file:
                return True
            elif self.position.rank - new_position.rank == 1 and abs(files.index(new_position.file) - files.index(self.position.file)) == 1 and board.get_piece_at_position(new_position) is not None:
                return True
            else:
                return False
    
    def is_obstructed(self, new_position, board, is_double_move):
        if self.color == Color.WHITE:
            # If pawn is moving diagonally and it is a valid move, it is taking, so no obstruction
            if self.position.file != new_position.file:
                return False
            elif board.get_piece_at_position(Position(self.position.file, self.position.rank + 1)) is not None:
                return True
            elif is_double_move:
                if board.get_piece_at_position(Position(self.position.file, self.position.rank + 2)):
                    return True
        elif self.color == Color.BLACK:
            # If pawn is moving diagonally and it is a valid move, it is taking, so no obstruction
            if self.position.file != new_position.file:
                return False
            if board.get_piece_at_position(Position(self.position.file, self.position.rank - 1)) is not None:
                return True
            elif is_double_move:
                if board.get_piece_at_position(Position(self.position.file, self.position.rank - 2)):
                    return True

        return False
