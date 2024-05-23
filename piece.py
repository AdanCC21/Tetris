from colors import Colors
import pygame
from positions import Positions
class Piece:
    def __init__(self, id):
        self.id = id
        self.cells = {} # dictionary with the cells of ocupied space the piece use.
        self.cells_size = 30 # size of the cell.
        self.row_offset= 0 # move in row
        self.column_offset = 0 # move in column
        self.rotation_state = 0 # initial rotation state.
        self.colors = Colors.get_pieces_colors()  # get the colors of the pieces.

    # method to draw the piece.
    def draw_piece(self, screen, offset_x, offset_y):
        # each cell is a tile. 
        tiles = self.get_cell_position() # retrieves the list of positions for the current rotation state.
        # draw the piece.
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cells_size, offset_y + tile.row * self.cells_size,
                        self.cells_size -1, self.cells_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
    
    # method to move the piece.
    def move(self,rows,columns):
        self.row_offset += rows
        self.column_offset += columns
    
    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles=[]
        for pos in tiles:
            pos = Positions (pos.row + self.row_offset,pos.column + self.column_offset )
            moved_tiles.append(pos)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state +=1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -=1
        if self.rotation_state ==0:
            self.rotation_state = len(self.cells)-1
