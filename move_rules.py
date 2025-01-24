from piece import Piece
from translate_board_notations import array_pos_to_rank_file_numeric

def valid_moves(piece, idx, board):
    match piece:
        case Piece.WHITE_PAWN:
            return valid_white_pawn_moves(piece, idx, board)
        case Piece.BLACK_PAWN:
            return valid_black_pawn_moves(piece, idx, board)
        case Piece.WHITE_ROOK | Piece.BLACK_ROOK:
            return valid_rook_moves(piece, idx, board)
        case Piece.WHITE_KNIGHT | Piece.BLACK_KNIGHT:
            return valid_knight_moves(piece, idx, board)
        case Piece.WHITE_BISHOP | Piece.BLACK_BISHOP:
            return valid_bishop_moves(piece, idx, board)
        case Piece.WHITE_QUEEN | Piece.BLACK_QUEEN:
            return valid_queen_moves(piece, idx, board)
        case Piece.WHITE_KING | Piece.BLACK_KING:
            return valid_king_moves(piece, idx, board)
        case _:
            raise ValueError("Invalid piece")
    
def valid_white_pawn_moves(piece, idx, board):
    valid_moves = []
    for new_idx in range(64):
        if idx - new_idx == 8:
            valid_moves.append(new_idx)
        if idx // 8 == 6:
            if idx - new_idx == 16:
                valid_moves.append(new_idx)
    return valid_moves

def valid_black_pawn_moves(piece, idx, board):
    valid_moves = []
    for new_idx in range(64):
        if new_idx - idx == 8:
            valid_moves.append(new_idx)
        if idx // 8 == 1:
            if new_idx - idx == 16:
                valid_moves.append(new_idx)
    return valid_moves

def valid_rook_moves(piece, idx, board):
    valid_moves = []
    for new_idx in range(64):
        if new_idx // 8 == idx // 8:
            valid_moves.append(new_idx)
        elif new_idx % 8 == idx % 8:
            valid_moves.append(new_idx)
    return valid_moves

def valid_knight_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []
    for new_idx in range(64):
        new_rank, new_file = array_pos_to_rank_file_numeric(new_idx)
        if (abs(new_rank - curr_rank) == 2 and abs(new_file - curr_file) == 1) or (abs(new_rank - curr_rank) == 1 and abs(new_file - curr_file) == 2):
            valid_moves.append(new_idx)
    return valid_moves

def valid_bishop_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []
    for new_idx in range(64):
        new_rank, new_file = array_pos_to_rank_file_numeric(new_idx)
        if abs(new_rank - curr_rank) == abs(new_file - curr_file):
            valid_moves.append(new_idx)
    return valid_moves

def valid_queen_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []
    for new_idx in range(64):
        new_rank, new_file = array_pos_to_rank_file_numeric(new_idx)
        if new_idx // 8 == idx // 8:
            valid_moves.append(new_idx)
        elif new_idx % 8 == idx % 8:
            valid_moves.append(new_idx)
        if abs(new_rank - curr_rank) == abs(new_file - curr_file):
            valid_moves.append(new_idx)
    return valid_moves

def valid_king_moves(piece, idx, board):
    valid_moves = []
    for new_idx in range(64):
        if abs(new_idx - idx) == 1 or abs(new_idx - idx) == 7 or abs(new_idx - idx) == 8 or abs(new_idx - idx) == 9:
            valid_moves.append(new_idx)
    return valid_moves
            