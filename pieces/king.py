from pieces.piece import Piece
from colors import Color
import pygame
from files import files
from position import Position

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
        self.has_moved = False
        self.is_in_check = False

    def move(self, new_position, board):
        rook = None
        if (abs(files.index(self.position.file) - files.index(new_position.file)) == 2) and self.position.rank == new_position.rank:
            try:
                rook, initial_position = self.castle(new_position, board)
            except ValueError as e:
                raise
            return rook, initial_position
        if not self.is_valid_move(new_position):
            raise ValueError("Invalid Move")
        self.position = new_position
        self.has_moved = True


    def is_valid_move(self, new_position):
        if self.is_in_check:
            return False
        if self.position.file == new_position.file and abs(self.position.rank - new_position.rank) == 1:
            return True
        elif self.position.rank == new_position.rank and abs(files.index(self.position.file) - files.index(new_position.file)) == 1:
            return True
        elif abs(files.index(self.position.file) - files.index(new_position.file)) == 1 and abs(self.position.rank - new_position.rank) == 1:
            return True
        else:
            return False
    
    def castle(self, new_position, board):
        if self.has_moved:
            raise ValueError("King has already moved")
        if self.is_in_check:
            raise ValueError("King is in check")
        if files.index(self.position.file) < files.index(new_position.file):
            rook = board.get_piece_at_position(Position(files[0], self.position.rank))
            if rook:
                if rook.has_moved:
                    raise ValueError("Rook has already moved")
                for i in range(1, 4):
                    if board.get_piece_at_position(Position(files[i], self.position.rank)):
                        raise ValueError("Path is obstructed")
                self.position = new_position
                rook.position = Position('d', self.position.rank)
                return rook, Position(files[0], self.position.rank)
            else:
                raise ValueError("Rook no longer in castling position")
        elif files.index(self.position.file) < files.index(new_position.file):
            rook = board.get_piece_at_position(Position(files[7], self.position.rank))
            if rook:
                if rook.has_moved:
                    raise ValueError("Rook has already moved")
                for i in range(5, 7):
                    if board.get_piece_at_position(Position(files[i], self.position.rank)):
                        raise ValueError("Path is obstructed")
                self.position = new_position
                rook.position = Position('f', self.position.rank)
                return rook, Position(files[7], self.position.rank)
            else:
                raise ValueError("Rook no longer in castling position")

        
