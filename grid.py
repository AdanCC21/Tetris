import pygame

class Grid:
    # Constructor
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_color()

    # Method to draw the grid
    def draw_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    
    # Method to add the color of the pieces.
    def get_color(self):
        DARK_GRAY = (26, 31, 40)
        RED = (232, 18, 18)
        GREEN = (47,230,23)
        BLUE = (13, 64, 216)
        YELLOW = (237, 234, 4)
        PURPLE = (166, 0, 247)
        PINK = (255, 105, 180)
        ORANGE = (255, 165, 0)
        # return the color of the piece.
        return [DARK_GRAY, RED, GREEN, BLUE, YELLOW, PURPLE, PINK, ORANGE]
    
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