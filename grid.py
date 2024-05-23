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
                cell_piece = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11, # (x, y, width, height) add margin to the cell.
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_piece)
    
    def is_inside(self,row,column):
        if (row >=0 and row < self.num_rows) and (column >=0 and column <self.num_cols):
            return True
        return False
    
    def is_empy(self,row,column):
        if self.grid[row][column] == 0:
            return True
        return False
    def is_row_full(self,row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    def clear_row(self,row):
        for column in range(self.num_cols):
            self.grid[row][column]
    
    def move_row_down(self, row,numer_row):
        for column in range(self.num_cols):
            self.grid[row+numer_row][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1,0,-1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed >0:
                self.move_row_down(row,completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0