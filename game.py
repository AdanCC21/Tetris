from grid import Grid
from pieces import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.pieces = [IPiece(),JPiece(),TPiece(),LPiece(),SPiece(),ZPiece(),SquarePiece()]
        self.current_piece = self.get_random_piece()
        self.next_piece = self.get_random_piece()
        self.game_over = False
        self.score=0
        self.rotate_sound = pygame.mixer.Sound("uf.mp3")
        self.clear_sound = pygame.mixer.Sound("uf.mp3")

        pygame.mixer.music.load("MusicGame.mp3")
        pygame.mixer.music.play(-1)
    
    def update_score(self,lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score +=100
        elif lines_cleared == 2:
            self.score +=300
        elif lines_cleared == 3:
            self.score +=500
        self.score += move_down_points


    def get_random_piece(self):
        if len(self.pieces) == 0:
            self.pieces = [IPiece(),JPiece(),TPiece(),LPiece(),SPiece(),ZPiece(),SquarePiece()]
        piece = random.choice(self.pieces)
        self.pieces.remove(piece)
        return piece 
    
    def draw(self, screen):
        self.grid.draw_color_pieces(screen)
        self.current_piece.draw_piece(screen, 11, 11)

        if self.next_piece.id == 3:
            self.next_piece.draw_piece(screen, 255,290)

        elif self.next_piece.id == 4:
            self.next_piece.draw_piece(screen, 255,280)
        
        else:
            self.next_piece.draw_piece(screen, 270,270)


    def piece_inside(self):
        tiles = self.current_piece.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row,tile.column) == False:
                return False
        return True
    

    def rotate(self):
        self.current_piece.rotate()
        if self.piece_inside() == False or self.piece_fits() == False:
            self.current_piece.undo_rotation()
        else:
                self.rotate_sound.play()


    def move_left(self):
        self.current_piece.move(0,-1)
        if self.piece_inside() == False or self.piece_fits() == False:
            self.current_piece.move(0,1)

    def move_right(self):
        self.current_piece.move(0,1)
        if self.piece_inside() == False or self.piece_fits() == False:
            self.current_piece.move(0,-1)

    def move_down(self):
        self.current_piece.move(1,0)
        if self.piece_inside() == False or self.piece_fits() == False:
            self.current_piece.move(-1,0)
            self.lock_piece()

    def lock_piece(self):
        tiles = self.current_piece.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_piece.id
        self.current_piece=self.next_piece
        self.next_piece = self.get_random_piece()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.piece_fits() == False:
            self.game_over = True


    def reset(self):
        self.grid.reset()
        self.pieces = [IPiece(),JPiece(),TPiece(),LPiece(),SPiece(),ZPiece(),SquarePiece()]
        self.current_piece = self.get_random_piece()
        self.next_piece = self.get_random_piece()
        self.score = 0

    
    def piece_fits(self):
        tiles = self.current_piece.get_cell_position()
        for tile in tiles:
            if self.grid.is_empy(tile.row,tile.column) == False:
                return False
        return True