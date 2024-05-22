from grid import Grid
from pieces import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.pieces = [IPiece(),JPiece(),TPiece(),LPiece(),SPiece(),ZPiece(),SquarePiece()]
        self.current_piece = self.get_random_piece()
        self.next_piece = self.get_random_piece()

    def get_random_piece(self):
        if len(self.pieces) == 0:
            self.pieces = [IPiece(),JPiece(),TPiece(),LPiece(),SPiece(),ZPiece(),SquarePiece()]
        piece = random.choice(self.pieces)
        self.pieces.remove(piece)
        return piece 
    
    def draw(self, screen):
        self.grid.draw_color_pieces(screen)
        self.current_piece.draw_piece(screen)


    def piece_inside(self):
        tiles = self.current_piece.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row,tile.column) == False:
                return False
        return True
    

    def rotate(self):
        self.current_piece.rotate()
        if self.piece_inside() == False:
            self.current_piece.undo_rotation()


    def move_left(self):
        self.current_piece.move(0,-1)
        if self.piece_inside() == False:
            self.current_piece.move(0,1)

    def move_right(self):
        self.current_piece.move(0,1)
        if self.piece_inside() == False:
            self.current_piece.move(0,-1)
    def move_down(self):
        self.current_piece.move(1,0)
        if self.piece_inside() == False:
            self.current_piece.move(-1,0)
