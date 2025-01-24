from board import Board
import pygame
import sys
from piece import Piece
from translate_board_notations import rank_file_numeric_to_array_pos
from move import Move
from move_rules import valid_moves
# Main game loop
pygame.init()

# Function to load and resize an image
def load_and_resize_image(path, size):
    image = pygame.image.load(path)  # Load the image
    return pygame.transform.scale(image, size)  # Resize the image

WIDTH, HEIGHT = 64 * 8, 64 * 8  # Window size
SQ_SIZE = 64  # Size of each square
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE_COLOR = (238, 238, 210)  # Light square color
DARK_SQUARE_COLOR = (118, 150, 86)  # Dark square color
BLACK_CIRCLE_COLOR = (0, 0, 0) # Black circle color

PIECE_IMAGES = {
    (Piece.BLACK | Piece.PAWN): load_and_resize_image("images/bP.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.BLACK | Piece.ROOK): load_and_resize_image("images/bR.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.BLACK | Piece.KNIGHT): load_and_resize_image("images/bN.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.BLACK | Piece.BISHOP): load_and_resize_image("images/bB.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.BLACK | Piece.QUEEN): load_and_resize_image("images/bQ.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.BLACK | Piece.KING): load_and_resize_image("images/bK.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.WHITE | Piece.PAWN): load_and_resize_image("images/wP.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.WHITE | Piece.ROOK): load_and_resize_image("images/wR.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.WHITE | Piece.KNIGHT): load_and_resize_image("images/wN.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.WHITE | Piece.BISHOP): load_and_resize_image("images/wB.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.WHITE | Piece.QUEEN): load_and_resize_image("images/wQ.png", (SQ_SIZE, SQ_SIZE)),
    (Piece.WHITE | Piece.KING): load_and_resize_image("images/wK.png", (SQ_SIZE, SQ_SIZE))
}

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")
board = Board()
board.set_up_game_start()
valid_moves_list = []

def draw_board():
    for rank in range(8):
        for file in range(8):
            color = LIGHT_SQUARE_COLOR if (rank + file) % 2 == 0 else DARK_SQUARE_COLOR
            pygame.draw.rect(screen, color, (file * SQ_SIZE, rank * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
            # Rank and file to index in 64 length board array
            index = (8 * rank) + file
            # Draw pieces if any
            piece = board.board[index]
            if piece:
                screen.blit(PIECE_IMAGES[piece], (file * SQ_SIZE, rank * SQ_SIZE))

dragging_piece = None
dragging_piece_pos = None
start_array_pos = None
end_array_pos = None
piece = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            file = x // SQ_SIZE
            rank = y // SQ_SIZE
            start_array_pos = rank_file_numeric_to_array_pos(rank, file)
            piece = board.board[start_array_pos]
            if piece:
                dragging_piece = piece
                dragging_piece_pos = (x, y)
                # Temporarily remove the piece from the board
                board.board[start_array_pos] = Piece.EMPTY



        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_piece:
                x, y = event.pos
                new_file = x // SQ_SIZE
                new_rank = y // SQ_SIZE
                end_array_pos = rank_file_numeric_to_array_pos(new_rank, new_file)
                if end_array_pos in valid_moves(piece, start_array_pos, board.board):
                    move = Move(board.board, start_array_pos, end_array_pos, piece)
                    move.move()
                else: # If the move is invalid, put the piece back
                    board.board[start_array_pos] = piece
                dragging_piece = None
                dragging_piece_pos = None
                draw_board()
                pygame.display.flip()

        elif event.type == pygame.MOUSEMOTION:
            if dragging_piece:                
                x, y = event.pos
                # screen.fill(WHITE)
                # draw_board()
                dragging_piece_pos = (x, y)
    
    # Change cursor depending on hover and action
    hover_x, hover_y = pygame.mouse.get_pos()
    hover_file = hover_x // SQ_SIZE
    hover_rank = hover_y // SQ_SIZE
    hover_array_pos = rank_file_numeric_to_array_pos(hover_rank, hover_file)
    if dragging_piece:
        pygame.mouse.set_cursor(pygame.cursors.broken_x)
    elif board.board[hover_array_pos]:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    
    
    draw_board()
    # Draw the dragging piece if exists
    if dragging_piece:
        screen.blit(PIECE_IMAGES[dragging_piece], (dragging_piece_pos[0] - SQ_SIZE // 2, dragging_piece_pos[1] - SQ_SIZE // 2))
        valid_moves_list = valid_moves(piece, start_array_pos, board.board)
        ## Overlay a light pink color on the valid move squares
        for valid_move in valid_moves_list:
            rank, file = divmod(valid_move, 8)
            center = (file * SQ_SIZE + SQ_SIZE // 2, rank * SQ_SIZE + SQ_SIZE // 2)
            radius = SQ_SIZE // 2
            border_width = 3
            pygame.draw.circle(screen, BLACK_CIRCLE_COLOR, center, radius, border_width)

    
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
