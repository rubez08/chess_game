from position import Position
from colors import Color
starting_piece_positions = {
    Position('a', 1): ("Rook", Color.WHITE), Position('b', 1): ("Knight", Color.WHITE), Position('c', 1): ("Bishop", Color.WHITE),
    Position('d', 1): ("Queen", Color.WHITE), Position('e', 1): ("King", Color.WHITE), Position('f', 1): ("Bishop", Color.WHITE),
    Position('g', 1): ("Knight", Color.WHITE), Position('h', 1): ("Rook", Color.WHITE),
    Position('a', 2): ("Pawn", Color.WHITE), Position('b', 2): ("Pawn", Color.WHITE), Position('c', 2): ("Pawn", Color.WHITE),
    Position('d', 2): ("Pawn", Color.WHITE), Position('e', 2): ("Pawn", Color.WHITE), Position('f', 2): ("Pawn", Color.WHITE),
    Position('g', 2): ("Pawn", Color.WHITE), Position('h', 2): ("Pawn", Color.WHITE),

    Position('a', 8): ("Rook", Color.BLACK), Position('b', 8): ("Knight", Color.BLACK), Position('c', 8): ("Bishop", Color.BLACK),
    Position('d', 8): ("Queen", Color.BLACK), Position('e', 8): ("King", Color.BLACK), Position('f', 8): ("Bishop", Color.BLACK),
    Position('g', 8): ("Knight", Color.BLACK), Position('h', 8): ("Rook", Color.BLACK),
    Position('a', 7): ("Pawn", Color.BLACK), Position('b', 7): ("Pawn", Color.BLACK), Position('c', 7): ("Pawn", Color.BLACK),
    Position('d', 7): ("Pawn", Color.BLACK), Position('e', 7): ("Pawn", Color.BLACK), Position('f', 7): ("Pawn", Color.BLACK),
    Position('g', 7): ("Pawn", Color.BLACK), Position('h', 7): ("Pawn", Color.BLACK)
}
