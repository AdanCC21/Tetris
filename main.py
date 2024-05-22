# execute game with python3.10 main.py
# ----------------------------------------------------------------
# LIBRARIES
import pygame, sys
from game import Game


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

game=Game()

# Game loop ----------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #move of piece
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
    # Update the screen
    # Draw the screen
    
    screen.fill(BLACK)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)  # 60 frames per second.
