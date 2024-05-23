# execute game with python3.10 main.py
# ----------------------------------------------------------------
# LIBRARIES
import pygame, sys
from game import Game
from colors import Colors


# Pygame initialization and screen configuration
pygame.init()

# Configurations
# ----------------------------------------------------------------
# Font
title_font = pygame.font.Font(None,40)

score_surface = title_font.render("SCORE", True, Colors.YELLOW)
next_surface = title_font.render("NEXT", True, Colors.YELLOW)
game_over_surface = title_font.render("GAME OVER", True, Colors.YELLOW)

score_rec = pygame.Rect(320,55,170,60)
next_rec =  pygame.Rect(320,215,170,180)

# Screen configuration.
screen = pygame.display.set_mode((500, 620))  # (width, height)
pygame.display.set_caption("TETRIS")  # program title.

# Objects ----------------------------------------------------------------
clock = pygame.time.Clock()  # Clock object to control the game's frame rate.

game=Game()
GAME_UPDATE = pygame.USEREVENT # special event
pygame.time.set_timer(GAME_UPDATE,220) # timer

# Game loop ----------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #move of piece
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Update the screen
    # Draw the screen
    screen.fill(Colors.DARK_BLUE)
    screen.blit(score_surface,(365,20,50,50))
    screen.blit(next_surface,(375,180,50,50))
    score_value = title_font.render(str(game.score), True,Colors.WHITE)

    if game.game_over == True:
        screen.blit(game_over_surface,(320,450,50,50))

    pygame.draw.rect(screen, Colors.DARK_GRAY, score_rec,0,10)
    screen.blit(score_value, score_value.get_rect(centerx = score_rec.centerx,
                                                  centery = score_rec.centery,))
    pygame.draw.rect(screen, Colors.DARK_GRAY, next_rec,0,10)
    game.draw(screen)


    pygame.display.update()
    clock.tick(60)  # 60 frames per second.
