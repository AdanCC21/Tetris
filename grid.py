import pygame
from colors import Colors

class Grid:
    # Constructor
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_pieces_colors();

    # Method to draw the grid. In the terminal.
    def draw_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    
    
    
    # Method to draw the grid with colors.
    def draw_color_pieces(self, screen):
        # color in the grid asign by the value of the cell.
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # if the cell value is 0, the cell is empty. Draw a black rectangle.
                # we need it to be 29 pixels wide and 29 pixels high to watch the grid.
                cell_piece = pygame.Rect(column * self.cell_size +1, row * self.cell_size +1, # (x, y, width, height) add margin to the cell.
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_piece)
    
    def is_inside(self,row,column):
        if (row >=0 and row < self.num_rows) and (column >=0 and column <self.num_cols):
            return True
        return False