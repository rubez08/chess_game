from translate_board_notations import fen_notation_to_board

class Game:
    def __init__(self, color='white'):
        self.board = []
        self.set_up_game_start(color)
        self.color = color
        self.turn = color
        self.moves = []
    
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
        self.moves.append(move)
        self.turn = 'white' if self.turn == 'black' else 'black'
    
    def get_moves(self):
        return self.moves