from pieces.piece import Piece
from colors import Color
import pygame
from files import files
from position import Position

class Queen(Piece):
    name = "Queen"
    def __init__(self, color, position):
        super().__init__(color, position)
        match color:
            case Color.WHITE:
                self.image = pygame.image.load("pieces/queen_white.png")
            case Color.BLACK:
                self.image = pygame.image.load("pieces/queen_black.png")
            case _:
                raise ValueError("Invalid color")
    
    def move(self, new_position, board):
        if not self.is_valid_move(new_position):
            raise ValueError("Invalid Move")
        if self.is_obstructed(new_position, board):
            raise ValueError("There is a piece in the way")
        self.position = new_position
    
    def is_valid_move(self, new_position):
        if self.position.rank == new_position.rank:
            return True
        if self.position.file == new_position.file:
            return True
        if (abs(self.position.rank - new_position.rank) == abs(files.index(self.position.file) - files.index(new_position.file))):
            return True
        else:
            return False
    
    def is_obstructed(self, newPosition, board):
        # Rook-like movement
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
        else:
            # Bishop-like movement
            # Determine the direction of the move
            rank_dir = 1 if newPosition.rank > self.position.rank else -1
            file_dir = 1 if files.index(newPosition.file) > files.index(self.position.file) else -1
            # Check if there is a piece in the path
            for i in range(1, abs(newPosition.rank - self.position.rank)):
                position_to_check = Position(files[files.index(self.position.file) + (i * file_dir)], self.position.rank + (i * rank_dir))
                if board.get_piece_at_position(position_to_check) is not None:
                    return True
        return False