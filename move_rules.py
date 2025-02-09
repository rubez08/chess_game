from piece import Piece
from translate_board_notations import array_pos_to_rank_file_numeric, rank_file_numeric_to_array_pos
from move import Move

def pseudo_valid_moves(piece, idx, board, game_color, game):
    """Private function to get psuedo-valid moves for any piece"""

    if piece.is_pawn():
        moving_up = (game_color == 'white' and piece == Piece.WHITE_PAWN) or \
                    (game_color == 'black' and piece == Piece.BLACK_PAWN)
        last_move = game.move_history[-1] if game and game.move_history else None
        return __valid_pawn_moves(piece, idx, board, moving_up, last_move)
    elif piece.is_rook():
        return __valid_rook_moves(piece, idx, board)
    elif piece.is_knight():
        return __valid_knight_moves(piece, idx, board)
    elif piece.is_bishop():
        return __valid_bishop_moves(piece, idx, board)
    elif piece.is_queen():
        return __valid_queen_moves(piece, idx, board)
    elif piece == Piece.WHITE_KING:
        return __valid_king_moves(piece, idx, board, game.has_white_king_moved, game.has_white_rook_moved)
    elif piece == Piece.BLACK_KING:
        return __valid_king_moves(piece, idx, board, game.has_black_king_moved, game.has_black_rook_moved)
    else:
        raise ValueError("Invalid piece")

def valid_moves(piece, idx, board, game_color, game_turn, game):
    """Public function to get valid moves for any piece"""
    if piece.is_pawn():
        moving_up = (game_color == 'white' and piece == Piece.WHITE_PAWN) or \
                    (game_color == 'black' and piece == Piece.BLACK_PAWN)
        last_move = game.move_history[-1] if game and game.move_history else None
        return [end_idx for end_idx in __valid_pawn_moves(piece, idx, board, moving_up, last_move) if not __would_move_cause_check(piece, idx, end_idx, game_turn, game)]
    elif piece.is_rook():
        return [end_idx for end_idx in __valid_rook_moves(piece, idx, board) if not __would_move_cause_check(piece, idx, end_idx, game_turn, game)]
    elif piece.is_knight():
        return [end_idx for end_idx in __valid_knight_moves(piece, idx, board) if not __would_move_cause_check(piece, idx, end_idx, game_turn, game)]
    elif piece.is_bishop():
        return [end_idx for end_idx in __valid_bishop_moves(piece, idx, board) if not __would_move_cause_check(piece, idx, end_idx, game_turn, game)]
    elif piece.is_queen():
        return [end_idx for end_idx in __valid_queen_moves(piece, idx, board) if not __would_move_cause_check(piece, idx, end_idx, game_turn, game)]
    elif piece == Piece.WHITE_KING:
        return [end_idx for end_idx in __valid_king_moves(piece, idx, board, game.has_white_king_moved, game.has_white_rook_moved) if not __would_move_cause_check(piece, idx, end_idx, game_turn, game)]
    elif piece == Piece.BLACK_KING:
        return [end_idx for end_idx in __valid_king_moves(piece, idx, board, game.has_black_king_moved, game.has_black_rook_moved) if not __would_move_cause_check(piece, idx, end_idx, game_turn, game)]
    else:
        raise ValueError("Invalid piece")

def __is_square_under_attack(square_idx, attacking_color, board, game):
    # Check if a square is under attack by any enemy piece
    for idx, piece in enumerate(board):
        if piece != Piece.EMPTY and piece.is_opposite_color(attacking_color):
            # Get all possible moves for this piece
            moves = pseudo_valid_moves(piece, idx, game.board, "white" if attacking_color == "black" else "black", game)
            if square_idx in moves:
                return True
    return False

def is_king_in_check(color, board, game):
    # Check if the King of the given color is in check
    # Find King
    king_idx = game.white_king_idx if color == 'white' else game.black_king_idx

    # Check if king's square is under attack by opposite color
    return __is_square_under_attack(king_idx, Piece.WHITE if color =='white' else Piece.BLACK, board, game)

def __would_move_cause_check(piece, start_idx, end_idx, color, game):
    """Test if a move would put or leave own king in check"""
        # Add bounds checking
    if not (0 <= start_idx < 64 and 0 <= end_idx < 64):
        raise ValueError("Invalid move")  # Invalid move if out of bounds
    # Make a copy of the game
    temp_game = game.copy()
    # Make potential move in game copy
    move = Move(temp_game.board, start_idx, end_idx, piece, temp_game.board[end_idx], game.get_last_move())
    move.move()
    temp_game.add_move(move)
    
    return is_king_in_check(color, temp_game.board, temp_game)
    
def __valid_pawn_moves(piece, idx, board, moving_up, last_move=None):
    """Calculate valid pawn moves based on direction
    Args:
        piece: The pawn piece
        idx: Current position
        board: Game board
        moving_up: True if pawn moves up the board, False if down
        last_move: The last move made in the game (for en passant)
    """
    valid_moves = []
    direction = -8 if moving_up else 8
    start_rank = 6 if moving_up else 1
    current_rank = idx // 8
    
    # Forward moves
    forward_idx = idx + direction
    if 0 <= forward_idx < 64 and board[forward_idx] == Piece.EMPTY:
        valid_moves.append(forward_idx)
        
        # Two square advance from starting position
        if current_rank == start_rank:
            double_forward_idx = idx + (direction * 2)
            if board[double_forward_idx] == Piece.EMPTY:
                valid_moves.append(double_forward_idx)
    
    # Regular captures
    file = idx % 8
    captures = []
    if file > 0:  # Can capture left
        captures.append(idx + direction - 1)
    if file < 7:  # Can capture right
        captures.append(idx + direction + 1)
    
    # Check capture squares for enemy pieces
    for capture_idx in captures:
        if 0 <= capture_idx < 64:
            target = board[capture_idx]
            if target != Piece.EMPTY and target.is_opposite_color(piece):
                valid_moves.append(capture_idx)
    
    # En passant
    if last_move and (last_move.piece_moved & Piece.PAWN):
        last_start_rank = last_move.start // 8
        last_end_rank = last_move.end // 8
        last_file = last_move.end % 8
        
        # Check if last move was a two-square pawn advance
        if abs(last_end_rank - last_start_rank) == 2:
            # Check if our pawn is adjacent to the moved pawn
            if current_rank == last_end_rank and abs(file - last_file) == 1:
                # Add en passant capture square
                en_passant_idx = last_move.end + direction
                valid_moves.append(en_passant_idx)
                
    return valid_moves

def __valid_rook_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []

    # Check horizontal moves
    horizontal_moves = []
    for i in range(8):
        if i == curr_file:
            continue
        horizontal_moves.append((curr_rank, i))
    for square in horizontal_moves:
        in_between_squares = [sq for sq in horizontal_moves if sq[1] > min(square[1], curr_file) and sq[1] < max(square[1], curr_file)]
        if all([board[rank_file_numeric_to_array_pos(sq[0], sq[1])] == Piece.EMPTY for sq in in_between_squares]) and not board[rank_file_numeric_to_array_pos(curr_rank, square[1])].is_same_color(piece):
            valid_moves.append(rank_file_numeric_to_array_pos(curr_rank, square[1]))
    
    # Check vertical moves
    vertical_moves = []
    for i in range(8):
        if i == curr_rank:
            continue
        vertical_moves.append((i, curr_file))
    for square in vertical_moves:
        in_between_squares = [sq for sq in vertical_moves if sq[0] > min(curr_rank, square[0]) and sq[0] < max(curr_rank, square[0])]
        if all([board[rank_file_numeric_to_array_pos(sq[0], sq[1])] == Piece.EMPTY for sq in in_between_squares]) and not board[rank_file_numeric_to_array_pos(square[0], curr_file)].is_same_color(piece):
            valid_moves.append(rank_file_numeric_to_array_pos(square[0], curr_file))
    
    return valid_moves

def __valid_knight_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) == 3 and curr_rank + i >= 0 and curr_rank + i < 8 and curr_file + j >= 0 and curr_file + j < 8:
                if not board[rank_file_numeric_to_array_pos(curr_rank + i, curr_file + j)].is_same_color(piece):
                    valid_moves.append(rank_file_numeric_to_array_pos(curr_rank + i, curr_file + j))
    
    return valid_moves

def __valid_bishop_moves(piece, idx, board):
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []

    # Check all four diagonal directions
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for rank_dir, file_dir in directions:
        rank, file = curr_rank + rank_dir, curr_file + file_dir
        while 0 <= rank < 8 and 0 <= file < 8:
            target_idx = rank_file_numeric_to_array_pos(rank, file)
            target_piece = board[target_idx]
            
            # If square is empty, add it and continue in this direction
            if target_piece == Piece.EMPTY:
                valid_moves.append(target_idx)
            # If square has enemy piece, add it and stop this direction
            elif not target_piece.is_same_color(piece):
                valid_moves.append(target_idx)
                break
            # If square has friendly piece, stop this direction
            else:
                break
                
            rank += rank_dir
            file += file_dir
    
    return valid_moves

def __valid_queen_moves(piece, idx, board):
    return __valid_rook_moves(piece, idx, board) + __valid_bishop_moves(piece, idx, board)

def valid_castling_moves(piece, idx, board, has_king_moved, has_rook_moved):
    """Check for valid castling moves for a king"""
    valid_moves = []
    
    # Only process if it's a king and hasn't moved
    if not (piece & Piece.KING) or has_king_moved:
        return valid_moves
        
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    
    # Check kingside castle
    if not has_rook_moved.get('kingside', True):
        # Check if squares between king and rook are empty
        if all(board[rank_file_numeric_to_array_pos(curr_rank, f)] == Piece.EMPTY 
               for f in range(curr_file + 1, 7)):
            valid_moves.append(rank_file_numeric_to_array_pos(curr_rank, curr_file + 2))
    
    # Check queenside castle
    if not has_rook_moved.get('queenside', True):
        # Check if squares between king and rook are empty
        if all(board[rank_file_numeric_to_array_pos(curr_rank, f)] == Piece.EMPTY 
               for f in range(1, curr_file)):
            valid_moves.append(rank_file_numeric_to_array_pos(curr_rank, curr_file - 2))
    
    return valid_moves

def __valid_king_moves(piece, idx, board, has_king_moved, has_rook_moved):
    """Get all valid moves for a king, including castling"""
    curr_rank, curr_file = array_pos_to_rank_file_numeric(idx)
    valid_moves = []
    
    # Normal king moves
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for rank_dir, file_dir in directions:
        new_rank = curr_rank + rank_dir
        new_file = curr_file + file_dir
        
        if 0 <= new_rank < 8 and 0 <= new_file < 8:
            target_idx = rank_file_numeric_to_array_pos(new_rank, new_file)
            target_piece = board[target_idx]
            
            if target_piece == Piece.EMPTY or not target_piece.is_same_color(piece):
                valid_moves.append(target_idx)
    
    # Add castling moves if applicable
    if has_rook_moved is not None:  # Only check castling if rook movement history is provided
        castling_moves = valid_castling_moves(piece, idx, board, has_king_moved, has_rook_moved)
        valid_moves.extend(castling_moves)
            
    return valid_moves
