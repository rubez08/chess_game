from game import Game
import pygame
import sys
from piece import Piece
from translate_board_notations import rank_file_numeric_to_array_pos, files
from move import Move
from move_rules import valid_moves
# Main game loop
pygame.init()

# Function to load and resize an image
def load_and_resize_image(path, size):
    image = pygame.image.load(path)  # Load the image
    return pygame.transform.scale(image, size)  # Resize the image

# Constants
FONT = pygame.font.SysFont("geneva", 10)
WIDTH, HEIGHT = 64 * 8, 64 * 8  # Window size
SQ_SIZE = 64  # Size of each square
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE_COLOR = (238, 238, 210)  # Light square color
DARK_SQUARE_COLOR = (118, 150, 86)  # Dark square color
BLACK_CIRCLE_COLOR = (0, 0, 0) # Black circle color

PIECE_IMAGES = {
    Piece.BLACK_PAWN: load_and_resize_image("images/bP.png", (SQ_SIZE, SQ_SIZE)),
    Piece.BLACK_ROOK: load_and_resize_image("images/bR.png", (SQ_SIZE, SQ_SIZE)),
    Piece.BLACK_KNIGHT: load_and_resize_image("images/bN.png", (SQ_SIZE, SQ_SIZE)),
    Piece.BLACK_BISHOP: load_and_resize_image("images/bB.png", (SQ_SIZE, SQ_SIZE)),
    Piece.BLACK_QUEEN: load_and_resize_image("images/bQ.png", (SQ_SIZE, SQ_SIZE)),
    Piece.BLACK_KING: load_and_resize_image("images/bK.png", (SQ_SIZE, SQ_SIZE)),
    Piece.WHITE_PAWN: load_and_resize_image("images/wP.png", (SQ_SIZE, SQ_SIZE)),
    Piece.WHITE_ROOK: load_and_resize_image("images/wR.png", (SQ_SIZE, SQ_SIZE)),
    Piece.WHITE_KNIGHT: load_and_resize_image("images/wN.png", (SQ_SIZE, SQ_SIZE)),
    Piece.WHITE_BISHOP: load_and_resize_image("images/wB.png", (SQ_SIZE, SQ_SIZE)),
    Piece.WHITE_QUEEN: load_and_resize_image("images/wQ.png", (SQ_SIZE, SQ_SIZE)),
    Piece.WHITE_KING: load_and_resize_image("images/wK.png", (SQ_SIZE, SQ_SIZE))
}

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")
game = Game('white')
valid_moves_list = []
new_pick_up = False

def draw_board():
    for rank_idx in range(8):
        rank = 8 - rank_idx if game.color == 'white' else rank_idx + 1
        for file in range(8):
            color = LIGHT_SQUARE_COLOR if (rank_idx + file) % 2 == 0 else DARK_SQUARE_COLOR
            pygame.draw.rect(screen, color, (file * SQ_SIZE, rank_idx * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if rank_idx == 7:
                file_name = FONT.render(files[file], False, DARK_SQUARE_COLOR) if color == LIGHT_SQUARE_COLOR else FONT.render(files[file], False, LIGHT_SQUARE_COLOR)
                file_name_rect = file_name.get_rect()
                file_name_rect.center = (file * SQ_SIZE + (SQ_SIZE - 10), rank_idx * SQ_SIZE + (SQ_SIZE - 10))
                screen.blit(file_name, file_name_rect)
            if file == 0:
                rank_name = FONT.render(str(rank), False, DARK_SQUARE_COLOR) if color == LIGHT_SQUARE_COLOR else FONT.render(str(rank), False, LIGHT_SQUARE_COLOR)
                rank_name_rect = rank_name.get_rect()
                rank_name_rect.center = (10, rank_idx * SQ_SIZE + 10)
                screen.blit(rank_name, rank_name_rect)
            
            # Rank and file to index in 64 length board array
            index = (8 * rank_idx) + file
            # Draw pieces if any
            piece = game.board[index]
            if piece:
                screen.blit(PIECE_IMAGES[piece], (file * SQ_SIZE, rank_idx * SQ_SIZE))

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
            piece = game.board[start_array_pos]
            is_correct_color = (game.turn == 'white' and piece.is_white()) or (game.turn == 'black' and piece.is_black())
            if is_correct_color:
                new_pick_up = True
                dragging_piece = piece
                dragging_piece_pos = (x, y)
                # Temporarily remove the piece from the board
                game.board[start_array_pos] = Piece.EMPTY

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_piece:
                x, y = event.pos
                new_file = x // SQ_SIZE
                new_rank = y // SQ_SIZE
                end_array_pos = rank_file_numeric_to_array_pos(new_rank, new_file)
                if end_array_pos in valid_moves(dragging_piece, start_array_pos, game.board, game.color, game.turn, game):
                    move = Move(game.board, start_array_pos, end_array_pos, dragging_piece, game.board[end_array_pos], game.get_last_move())
                    move.move()
                    game.add_move(move)
                    game.update_check_status()
                    if game.is_white_in_check or game.is_black_in_check:
                        if game.is_checkmate():
                            print(f"{game.turn} is in checkmate!")
                        else:
                            print(f"{game.turn} is in check!")

                else: # If the move is invalid, put the piece back
                    game.board[start_array_pos] = dragging_piece
                dragging_piece = None
                dragging_piece_pos = None
                draw_board()
                pygame.display.flip()

        elif event.type == pygame.MOUSEMOTION:
            if dragging_piece:                
                x, y = event.pos
                dragging_piece_pos = (x, y)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and len(game.move_history) > 0:
                game.undo()
                draw_board()
                pygame.display.flip()
    
    # Change cursor depending on hover and action
    hover_x, hover_y = pygame.mouse.get_pos()
    hover_file = hover_x // SQ_SIZE
    hover_rank = hover_y // SQ_SIZE
    hover_array_pos = rank_file_numeric_to_array_pos(hover_rank, hover_file)
    if dragging_piece:
        pygame.mouse.set_cursor(pygame.cursors.broken_x)
    elif game.board[hover_array_pos]:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    
    
    draw_board()
    # Draw the dragging piece if exists
    if dragging_piece:
        screen.blit(PIECE_IMAGES[dragging_piece], (dragging_piece_pos[0] - SQ_SIZE // 2, dragging_piece_pos[1] - SQ_SIZE // 2))
        if new_pick_up:
            valid_moves_list = valid_moves(piece, start_array_pos, game.board, game.color, game.turn, game)
            new_pick_up = False
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
