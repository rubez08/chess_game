from piece import Piece
from translate_board_notations import array_pos_to_rank_file_numeric, rank_file_numeric_to_array_pos


def valid_moves(piece, idx, board, game_color):
    match piece:
        case Piece.WHITE_PAWN:
            if game_color == 'white':
                return valid_up_board_pawn_moves(piece, idx, board)
            else:
                return valid_down_board_pawn_moves(piece, idx, board)
        case Piece.BLACK_PAWN:
            if game_color == 'white':
                return valid_down_board_pawn_moves(piece, idx, board)
            else:
                return valid_up_board_pawn_moves(piece, idx, board)
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
    
def valid_down_board_pawn_moves(piece, idx, board):
    valid_moves = []
    for new_idx in range(64):
        # Move forward one square
        if new_idx - idx == 8:
            if board[new_idx] == piece.EMPTY:
                valid_moves.append(new_idx)
        # If on start square, move forward two squares
        if idx // 8 == 1:
            if new_idx - idx == 16:
                if board[new_idx] == Piece.EMPTY and board[new_idx - 8] == Piece.EMPTY:
                    valid_moves.append(new_idx)
        # Capture diagonally
        if idx % 8 == 0:
            if new_idx - idx == 9 and board[new_idx].is_black():
                valid_moves.append(new_idx)
        elif idx % 8 == 7:
            if new_idx - idx == 7 and board[new_idx].is_black():
                valid_moves.append(new_idx)
        else:
            if new_idx - idx == 9 and board[new_idx].is_black():
                valid_moves.append(new_idx)
            if new_idx - idx == 7 and board[new_idx].is_black():
                valid_moves.append(new_idx)
    return valid_moves

def valid_up_board_pawn_moves(piece, idx, board):
    valid_moves = []
    for new_idx in range(64):
        # Move forward one square
        if idx - new_idx == 8:
            if board[new_idx] == piece.EMPTY:
                valid_moves.append(new_idx)
        # If on start square, move forward two squares
        if idx // 8 == 6:
            if idx - new_idx == 16:
                if board[new_idx] == Piece.EMPTY and board[new_idx + 8] == Piece.EMPTY:
                    valid_moves.append(new_idx)
        # Capture diagonally
        if idx % 8 == 0:
            if idx - new_idx == 7 and board[new_idx].is_white():
                valid_moves.append(new_idx)
        elif idx % 8 == 7:
            if idx - new_idx == 9 and board[new_idx].is_white():
                valid_moves.append(new_idx)
        else:
            if idx - new_idx == 9 and board[new_idx].is_white():
                valid_moves.append(new_idx)
            if idx - new_idx == 7 and board[new_idx].is_white():
                valid_moves.append(new_idx)
    return valid_moves

def valid_rook_moves(piece, idx, board):
    valid_moves = []
    # Check horizontal moves
    rank = idx // 8
    idx_at_start_of_rank = rank * 8
    idx_at_end_of_rank = idx_at_start_of_rank + 7
    # Check left
    if idx != idx_at_start_of_rank:
        for new_idx in range(idx, idx_at_start_of_rank-1, -1):
            if new_idx == idx:
                continue
            elif board[new_idx] == Piece.EMPTY:
                valid_moves.append(new_idx)
                continue
            elif board[new_idx].is_opposite_color(piece):
                valid_moves.append(new_idx)
                break
            elif board[new_idx].is_same_color(piece):
                break
    # Check right
    if idx != idx_at_end_of_rank:
        for new_idx in range(idx, idx_at_end_of_rank+1):
            if new_idx == idx:
                continue
            elif board[new_idx] == Piece.EMPTY:
                valid_moves.append(new_idx)
                continue
            elif board[new_idx].is_opposite_color(piece):
                valid_moves.append(new_idx)
                break
            elif board[new_idx].is_same_color(piece):
                break
    # Check vertical moves
    file = idx % 8
    idx_at_start_of_file = file
    idx_at_end_of_file = 56 + file
    # Check up
    if idx != idx_at_start_of_file:
        for new_idx in range(idx, idx_at_start_of_file-8, -8):
            if new_idx == idx:
                continue
            elif board[new_idx] == Piece.EMPTY:
                valid_moves.append(new_idx)
                continue
            elif board[new_idx].is_opposite_color(piece):
                valid_moves.append(new_idx)
                break
            elif board[new_idx].is_same_color(piece):
                break
    # Check down
    if idx != idx_at_end_of_file:
        for new_idx in range(idx, idx_at_end_of_file+8, 8):
            if new_idx == idx:
                continue
            elif board[new_idx] == Piece.EMPTY:
                valid_moves.append(new_idx)
                continue
            elif board[new_idx].is_opposite_color(piece):
                valid_moves.append(new_idx)
                break
            elif board[new_idx].is_same_color(piece):
                break
    return valid_moves

def valid_knight_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []

    for new_idx in range(64):
        if board[new_idx].is_same_color(piece):
            continue
        new_rank, new_file = array_pos_to_rank_file_numeric(new_idx)
        if (abs(new_rank - curr_rank) == 2 and abs(new_file - curr_file) == 1) or (abs(new_rank - curr_rank) == 1 and abs(new_file - curr_file) == 2):
            valid_moves.append(new_idx)
    return valid_moves

def valid_bishop_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []

    increasing_diagonal = [] ## Diagonal defined by an increasing file and increasing rank
    decreasing_diagonal = [] ## Diagonal defined by an increasing file and decreasing rank

    for i in range(1, 8):
        if curr_rank + i < 8 and curr_file + i < 8:
            increasing_diagonal.append((curr_rank + i, curr_file + i))
        if curr_rank - i >= 0 and curr_file + i < 8:
            decreasing_diagonal.append((curr_rank - i, curr_file + i))
        if curr_rank + i < 8 and curr_file - i >= 0:
            decreasing_diagonal.append((curr_rank + i, curr_file - i))
        if curr_rank - i >= 0 and curr_file - i >= 0:
            increasing_diagonal.append((curr_rank - i, curr_file - i))
    
    for rank, file in increasing_diagonal:
        in_between_squares = [sq for sq in increasing_diagonal if sq[0] > min(rank, curr_rank) and sq[0] < max(rank, curr_rank)]
        if all([board[rank_file_numeric_to_array_pos(sq[0], sq[1])] == Piece.EMPTY for sq in in_between_squares]) and not board[rank_file_numeric_to_array_pos(rank,file)].is_same_color(piece):
            valid_moves.append(rank_file_numeric_to_array_pos(rank, file))

    for rank, file in decreasing_diagonal:
        in_between_squares = [sq for sq in increasing_diagonal if sq[0] > min(rank, curr_rank) and sq[0] < max(rank, curr_rank)]
        if all([board[rank_file_numeric_to_array_pos(sq[0], sq[1])] == Piece.EMPTY for sq in in_between_squares]) and not board[rank_file_numeric_to_array_pos(rank,file)].is_same_color(piece):
            valid_moves.append(rank_file_numeric_to_array_pos(rank, file))

    
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
            