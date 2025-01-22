from board import Board
from position import Position
import pygame
import sys
from files import files

# board = Board()
# board.printBoard()
# board.movePiece(Position("e", 2), Position("e", 4))
# print()
# board.printBoard()

# Main game loop
pygame.init()

WIDTH, HEIGHT = 800, 800  # Window size
SQ_SIZE = WIDTH // 8  # Size of each square
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE_COLOR = (238, 238, 210)  # Light square color
DARK_SQUARE_COLOR = (118, 150, 86)  # Dark square color

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")
board = Board()

def draw_board():
    for rank in range(8):
        for file in range(8):
            color = LIGHT_SQUARE_COLOR if (rank + file) % 2 == 0 else DARK_SQUARE_COLOR
            pygame.draw.rect(screen, color, (file * SQ_SIZE, rank * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
            # Draw pieces if any
            piece = board.rows[rank][file].piece
            if piece:
                screen.blit(piece.image, (file * SQ_SIZE, rank * SQ_SIZE))

dragging_piece = None
dragging_piece_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            file = x // SQ_SIZE
            rank = y // SQ_SIZE
            piece = board.rows[rank][file].piece
            if piece:
                dragging_piece = piece
                dragging_piece_pos = (rank, file)
                board.rows[rank][file].piece = None
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_piece:
                x, y = event.pos
                new_file = x // SQ_SIZE
                new_rank = y // SQ_SIZE
                start_pos = Position(files[dragging_piece_pos[1]], 8 - dragging_piece_pos[0])
                end_pos = Position(files[new_file], 8 - new_rank)
                try:
                    board.move_piece(start_pos, end_pos, dragging_piece)
                except ValueError as e:
                    board.rows[dragging_piece_pos[0]][dragging_piece_pos[1]].piece = dragging_piece
                    print(e)
                dragging_piece = None
                dragging_piece_pos = None
                draw_board()
                pygame.display.flip()
        elif event.type == pygame.MOUSEMOTION:
            if dragging_piece:
                x, y = event.pos
                screen.fill(WHITE)
                draw_board()
                screen.blit(dragging_piece.image, (x - SQ_SIZE // 2, y - SQ_SIZE // 2))
                pygame.display.flip()
    
    if not dragging_piece:
        draw_board()
        pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
