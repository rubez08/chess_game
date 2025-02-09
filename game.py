from translate_board_notations import fen_notation_to_board
from move_rules import is_king_in_check 
from piece import Piece
from move import Move
from move_rules import valid_moves

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
        self.is_white_in_check = False
        self.is_black_in_check = False
        self.white_king_idx = 60
        self.black_king_idx = 4

    def update_check_status(self):
        self.is_white_in_check = is_king_in_check('white', self.board, self)
        self.is_black_in_check = is_king_in_check('black', self.board, self)
    
    def is_checkmate(self):
        all_valid_moves = []
        for idx, piece in enumerate(self.board):
            if (self.turn == 'white' and piece.is_white()) or (self.turn == 'black' and piece.is_black()):
                print(f"Checking valid moves for {piece} at {idx}")
                all_valid_moves.extend(valid_moves(piece, idx, self.board, self.color, self.turn, self))
        print(f"All valid moves: {all_valid_moves}")
        if len(all_valid_moves) == 0:
            return True
        return False
    
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
        self.move_history.append(move)
        self.turn = 'white' if self.turn == 'black' else 'black'
        if move.piece_moved.is_king():
            if move.piece_moved.is_white():
                self.white_king_idx = move.end
            else:
                self.black_king_idx = move.end
    
    def get_moves(self):
        return self.move_history
    
    def undo(self):
        if len(self.move_history) > 0:
            previous_move = self.move_history[-1]
            self.board[previous_move.start] = previous_move.piece_moved
            if previous_move.is_castling:
                self.board[previous_move.rook_start] = previous_move.rook_piece
                self.board[previous_move.rook_end] = Piece.EMPTY
                self.board[previous_move.end] = Piece.EMPTY
            elif previous_move.is_en_passant:
                self.board[previous_move.captured_pawn_pos] = previous_move.piece_captured
                self.board[previous_move.end] = Piece.EMPTY
            else:
                self.board[previous_move.end] = previous_move.piece_captured
            self.move_history.pop()
            self.turn = 'white' if self.turn == 'black' else 'black'
    
    def get_last_move(self):
        if len(self.move_history) > 0:
            return self.move_history[-1]
    
    def copy(self):
        copy_game = Game(self.color)
        copy_game.board = self.board.copy()
        copy_game.turn = self.turn
        copy_game.move_history = self.move_history.copy()
        copy_game.has_white_king_moved = self.has_white_king_moved
        copy_game.has_white_rook_moved = self.has_white_rook_moved.copy()
        copy_game.has_black_king_moved = self.has_black_king_moved
        copy_game.has_black_rook_moved = self.has_black_rook_moved.copy()
        copy_game.is_white_in_check = self.is_white_in_check
        copy_game.is_black_in_check = self.is_black_in_check
        return copy_game
