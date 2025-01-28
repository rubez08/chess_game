from translate_board_notations import fen_notation_to_board
from move_rules import array_pos_to_rank_file_numeric
from piece import Piece
from move import Move

class Game:
    def __init__(self, color='white'):
        self.board = []
        self.set_up_game_start(color)
        self.color = color
        self.turn = 'white'
        self.move_history = []
        self.has_white_king_moved = False
        self.has_white_rook_moved = {
            'kingside': False,
            'queenside': False
        }
        self.has_black_king_moved = False
        self.has_black_rook_moved = {
            'kingside': False,
            'queenside': False
        }
    
    def set_up_game_start(self, color='white'):
        fen = '8/8/8/8/8/8/8/8'
        if color == 'white':
            fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        elif color == 'black':
            fen = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"
        self.board = fen_notation_to_board(fen)
    
    def print_board(self):
        for rank in range(8):
            for file in range(8):
                print(self.board[(rank * 8) + file], end = ' ')
            print()
    
    def add_move(self, move):
        last_move = self.move_history[-1] if self.move_history else None
        move = Move(self.board, move.start, move.end, move.piece_moved, last_move)
        self.move_history.append(move)
        self.turn = 'white' if self.turn == 'black' else 'black'
    
    def get_moves(self):
        return self.move_history
    
    def undo(self):
        if len(self.move_history) > 0:
            previous_move = self.move_history[-1]
            print(f"Previous capture: {previous_move.piece_captured}")
            self.board[previous_move.start] = previous_move.piece_moved
            self.board[previous_move.end] = previous_move.piece_captured
            self.move_history.pop()
            self.turn = 'white' if self.turn == 'black' else 'black'
    
    def get_last_move(self):
        if len(self.move_history) > 0:
            return self.move_history[-1]
