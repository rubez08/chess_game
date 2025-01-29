from piece import Piece
from move_rules import array_pos_to_rank_file_numeric, rank_file_numeric_to_array_pos

class Move:
    def __init__(self, board, start, end, piece_moved, piece_captured=None, last_move=None):
        self.board = board
        self.start = start
        self.end = end
        self.piece_moved = piece_moved
        self.piece_captured = piece_captured
        self.is_en_passant = False
        self.captured_pawn_pos = None
        self.check_en_passant(last_move)
    
    def check_en_passant(self, last_move):
        # Check if last piece moved wasn't pawn or if there was no last move
        if not (self.piece_moved & Piece.PAWN) or not last_move:
            return
        last_move_start_rank, last_move_start_file = array_pos_to_rank_file_numeric(last_move.start)
        last_move_end_rank, last_move_end_file = array_pos_to_rank_file_numeric(last_move.end)
        self_start_rank, self_start_file = array_pos_to_rank_file_numeric(self.start)
        if last_move.piece_moved & Piece.PAWN:
            # If last move was a two-square pawn advance
            if abs(last_move_end_rank - last_move_start_rank) == 2:
                # And current pawn is adjacent to that pawn
                if abs(self_start_file - last_move_end_file) == 1 and abs(self_start_rank - last_move_end_rank) == 0:
                    # And moves to the square behind the pawn
                    direction = -8 if self.piece_moved & Piece.WHITE else 8
                    if self.end == last_move.end + direction:
                        self.is_en_passant = True
                        self.captured_pawn_pos = last_move.end
                        self.piece_captured = self.board[last_move.end]

    def move(self):
        if self.end == self.start:
            return
        else:
            # Check if this is a castling move - need to check BOTH king piece AND king movement
            start_rank, start_file = array_pos_to_rank_file_numeric(self.start)
            end_rank, end_file = array_pos_to_rank_file_numeric(self.end)
            
            is_castling = ((self.piece_moved & Piece.KING) == Piece.KING and  # Must be a king
                          abs(end_file - start_file) == 2 and  # Must move 2 squares horizontally
                          start_rank == end_rank)  # Must stay on same rank
            
            if is_castling:
                # Move the king
                self.board[self.end] = self.piece_moved
                self.board[self.start] = Piece.EMPTY
                
                # Move the rook
                if end_file > start_file:  # Kingside castle
                    rook_start = rank_file_numeric_to_array_pos(start_rank, 7)
                    rook_end = rank_file_numeric_to_array_pos(start_rank, 5)
                else:  # Queenside castle
                    rook_start = rank_file_numeric_to_array_pos(start_rank, 0)
                    rook_end = rank_file_numeric_to_array_pos(start_rank, 3)
                
                self.board[rook_end] = self.board[rook_start]
                self.board[rook_start] = Piece.EMPTY
            elif self.is_en_passant:
                # Move the attacking pawn
                self.board[self.end] = self.piece_moved
                self.board[self.start] = Piece.EMPTY
                # Remove the captured pawn
                self.board[self.captured_pawn_pos] = Piece.EMPTY
            else:
                # Normal move
                self.board[self.end] = self.piece_moved
                self.board[self.start] = Piece.EMPTY

            