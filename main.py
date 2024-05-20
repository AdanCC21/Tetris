# execute game with python3.10 main.py
# ----------------------------------------------------------------
# LIBRARIES
import pygame, sys
from grid import Grid
# Pygame initialization and screen configuration
pygame.init()

# Configurations
# ----------------------------------------------------------------
# Colors
BLACK = (0, 0, 0)

# Screen configuration.
screen = pygame.display.set_mode((300, 600))  # (width, height)
pygame.display.set_caption("TETRIS")  # program title.

# Objects
clock = pygame.time.Clock()  # Clock object to control the game's frame rate.

game_grid = Grid()  # Create a grid object.

# example of the grid with colors.
game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 2
game_grid.grid[17][8] = 3

game_grid.draw_grid()  # Print the grid. 20 rows and 10 columns.
game_grid.draw_color_pieces(screen)  # Draw the grid with colors.

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Update the screen
    # Draw the screen
    screen.fill(BLACK)
    game_grid.draw_color_pieces(screen)
    pygame.display.update()
    clock.tick(60)  # 60 frames per second.
