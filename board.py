# from pieces.pawn import Pawn
# from pieces.rook import Rook
# from pieces.knight import Knight
# from pieces.bishop import Bishop
# from pieces.queen import Queen
# from pieces.king import King
# from position import Position
# from square import Square
# from position import Position
# from files import files
# from starting_positions import starting_piece_positions



from piece import Piece
from translate_board_notations import fen_notation_to_board

class Board:

    def __init__(self):
        self.board = []

    def set_up_game_start(self, color='white'):
        fen = '8/8/8/8/8/8/8/8'
        if color == 'white':
            fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        elif color == 'black':
            fen = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"
        self.board = fen_notation_to_board(fen)
    
    def flip_board(self):
        flipped_board = []
        for rank in range(7, -1, -1):
            for file in range(8):
                flipped_board.append(self.board[(rank * 8) + file])
        self.board = flipped_board
    
    def print_board(self):
        for rank in range(8):
            for file in range(8):
                print(self.board[(rank * 8) + file], end = ' ')
            print()