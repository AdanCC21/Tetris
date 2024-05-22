from colors import Colors

class Piece:
    def __init__(self):
        self.id = id
        self.cells = {} # dictionary with the cells of ocupied space the piece use.
        self.cells_size = 30 # size of the cell.
        self.rotation_state = 0 # initial rotation state.
        self.colors = Colors.get_pieces_colors()  # get the colors of the pieces.

        # method to draw the piece.
    def draw_piece(self, screen):
