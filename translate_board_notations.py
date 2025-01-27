from piece import Piece
files = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

fen_piece_to_piece = {
    'P': Piece.WHITE | Piece.PAWN,
    'R': Piece.WHITE | Piece.ROOK,
    'N': Piece.WHITE | Piece.KNIGHT,
    'B': Piece.WHITE | Piece.BISHOP,
    'Q': Piece.WHITE | Piece.QUEEN,
    'K': Piece.WHITE | Piece.KING,
    'p': Piece.BLACK | Piece.PAWN,
    'r': Piece.BLACK | Piece.ROOK,
    'n': Piece.BLACK | Piece.KNIGHT,
    'b': Piece.BLACK | Piece.BISHOP,
    'q': Piece.BLACK | Piece.QUEEN,
    'k': Piece.BLACK | Piece.KING
}

def array_pos_to_board_notation(index):
    rank = 8 - (index // 8)
    file = files[index % 8]
    return f"{file}{rank}"

def board_notation_to_array_pos(board_notation):
    file = board_notation[0]
    rank = int(board_notation[1])
    return (8 - rank) * 8 + files.index(file)

def fen_notation_to_board(fen):
    board = []
    for char in fen:
        if char == '/':
            continue
        if char.isdigit():
            for i in range(int(char)):
                board.append(Piece.EMPTY)
        else:
            board.append(fen_piece_to_piece[char])
    return board

def rank_file_numeric_to_array_pos(rank, file):
    return (rank * 8) + file

def array_pos_to_rank_file_numeric(index):
    rank = index // 8
    file = index % 8
    return (rank, file)