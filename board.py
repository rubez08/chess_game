from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from position import Position
from square import Square
from position import Position

from starting_positions import starting_piece_positions
class Board:
    files = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    rows = []
    index_to_squareName = {}
    def __init__(self):
        self.buildBoard()
        self.placePieces()

    def buildBoard(self):
        for i in range(8, 0, -1):
            row = []
            for file in self.files:
                position = Position(file, i)
                row.append(Square(position))
            self.rows.append(row)

    def placePieces(self):
        for position, piece in starting_piece_positions.items():
            file = position.file
            rank = position.rank
            square = self.rows[8 - rank][self.files.index(file)]
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

    def printBoard(self):
        for row in self.rows:
            for square in row:
                if (square.piece == None):
                    print('X', end=' ')
                else:
                    print(square.piece.name[0], end=' ')
            print()

    def movePiece(self, start, end):
        start_square = self.rows[8 - start.rank][self.files.index(start.file)]
        piece_to_move = start_square.piece
        if piece_to_move == None:
            raise ValueError("No piece at start position")
        end_square = self.rows[8 - end.rank][self.files.index(end.file)]
        if end_square.piece != None:
            raise ValueError("End position is occupied")
        end_square.piece = piece_to_move
        start_square.piece = None
        piece_to_move.move(end)
