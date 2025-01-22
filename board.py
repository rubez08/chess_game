from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from position import Position
from square import Square
from position import Position
from files import files

from starting_positions import starting_piece_positions
class Board:
    rows = []
    index_to_squareName = {}
    def __init__(self):
        self.build_board()
        self.place_pieces()

    def build_board(self):
        for i in range(8, 0, -1):
            row = []
            for file in files:
                position = Position(file, i)
                row.append(Square(position))
            self.rows.append(row)

    def place_pieces(self):
        for position, piece in starting_piece_positions.items():
            file = position.file
            rank = position.rank
            square = self.rows[8 - rank][files.index(file)]
            if piece[0] == "Pawn":
                square.piece = Pawn(piece[1], position)
            elif piece[0] == "Rook":
                square.piece = Rook(piece[1], position)
            elif piece[0] == "Knight":
                square.piece = Knight(piece[1], position)
            elif piece[0] == "Bishop":
                square.piece = Bishop(piece[1], position)
            elif piece[0] == "Queen":
                square.piece = Queen(piece[1], position)
            elif piece[0] == "King":
                square.piece = King(piece[1], position)

    def print_board(self):
        for row in self.rows:
            for square in row:
                if (square.piece == None):
                    print('X', end=' ')
                else:
                    print(square.piece.name[0], end=' ')
            print()

    def move_piece(self, start, end, piece_to_move=None):
        start_square = self.rows[8 - start.rank][files.index(start.file)]
        if piece_to_move is None:
            raise ValueError("No piece at start position")
        end_square = self.rows[8 - end.rank][files.index(end.file)]
        if end_square.piece is not None:
            if end_square.piece.color == piece_to_move.color:
                raise ValueError("End position is occupied by a piece of the same color")
        try:
            result = piece_to_move.move(end, self)
            if result is None:
                second_piece, second_piece_start = None, None
            else:
                second_piece, second_piece_start = result
        except ValueError as e:
            raise ValueError(e)
        end_square.piece = piece_to_move
        start_square.piece = None
        if second_piece:
            second_start_square = self.rows[8 - second_piece_start.rank][files.index(second_piece_start.file)]
            second_end_square = self.rows[8 - second_piece.position.rank][files.index(second_piece.position.file)]
            second_end_square.piece = second_piece
            second_start_square.piece = None
    
    def get_piece_at_position(self, position):
        return self.rows[8 - position.rank][files.index(position.file)].piece