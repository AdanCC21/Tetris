# execute game with python3.10 main.py
# ----------------------------------------------------------------
# LIBRARIES
import pygame, sys
from grid import Grid
from pieces import *

# Pygame initialization and screen configuration
pygame.init()

# Configurations
# ----------------------------------------------------------------
# Colors
BLACK = (0, 0, 0)

# Screen configuration.
screen = pygame.display.set_mode((300, 600))  # (width, height)
pygame.display.set_caption("TETRIS")  # program title.

# Objects ----------------------------------------------------------------
clock = pygame.time.Clock()  # Clock object to control the game's frame rate.

game_grid = Grid()  # Create a grid object.
Lblock = LPiece()  # Create an L piece object.
ZBlock = ZPiece()  # Create a Z piece object.
SBlock = SPiece()  # Create an S piece object.
JBlock = JPiece()  # Create a J piece object.
SquareBlock = SquarePiece()  # Create a Square piece object.
IBlock = IPiece()  # Create an I piece object.
TBlock = TPiece()  # Create a T piece object.

# Game loop ----------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Update the screen
    # Draw the screen
    screen.fill(BLACK)
    game_grid.draw_color_pieces(screen)
    # Draw the piece
    # Lblock.draw_piece(screen) # red
    # ZBlock.draw_piece(screen) # purple
    # SBlock.draw_piece(screen) # yellow
    # JBlock.draw_piece(screen) # green
    # SquareBlock.draw_piece(screen) # blue
    # IBlock.draw_piece(screen) # orange
    # TBlock.draw_piece(screen) # pink


    pygame.display.update()
    clock.tick(60)  # 60 frames per second.
