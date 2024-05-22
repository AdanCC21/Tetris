from colors import Colors
import pygame

class Piece:
    def __init__(self, id):
        self.id = id
        self.cells = {} # dictionary with the cells of ocupied space the piece use.
        self.cells_size = 30 # size of the cell.
        self.rotation_state = 0 # initial rotation state.
        self.colors = Colors.get_pieces_colors()  # get the colors of the pieces.

    # method to draw the piece.
    def draw_piece(self, screen):
        # each cell is a tile. 
        tiles = self.cells[self.rotation_state] # retrieves the list of positions for the current rotation state.
        # draw the piece.
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cells_size + 1, tile.row * self.cells_size + 1,
                        self.cells_size -1, self.cells_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)