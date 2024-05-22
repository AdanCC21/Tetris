"""
class that will contain all the pieces of the game
It will inherit from the Piece class.
"""
from piece import Piece
from positions import Positions

# L piece shape that contains the position of each tile of the piece for each rotation state on the cell.
class LPiece(Piece):
    def __init__(self):
        # call the constructor of the parent class. Piece id. For that we use super() method.
        super().__init__(id = 1) 
        # dictionary of the pieces, the key is the rotation state (0:3) and the value is the position of the piece.
        self.cells = { 
            # the value is a list containing the positions of the occupied cells.
            # In this case, with the L piece, we have 4 cells. 
            0: [Positions(0,2), Positions(1,0), Positions(1,1), Positions(1,2)], # row, column (x, y)
            1: [Positions(0,1), Positions(1,1), Positions(2,1), Positions(2,2)],
            2: [Positions(1,0), Positions(1,1), Positions(1,2), Positions(2,0)],
            3: [Positions(0,0), Positions(0, 1), Positions(1, 1), Positions(2, 1)]
        }

# J piece shape that contains the position of each tile of the piece for each rotation state on the cell.
class JPiece(Piece):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Positions(0,0), Positions(1,0), Positions(1,1), Positions(1,2)],
            1: [Positions(0,1), Positions(0,2), Positions(1,1), Positions(2,1)],
            2: [Positions(1,0), Positions(1,1), Positions(1,2), Positions(2,2)],
            3: [Positions(0,1), Positions(1,1), Positions(2,0), Positions(2,1)]
        }

# Square piece shape that contains the position of each tile of the piece for each rotation state on the cell.
class SquarePiece(Piece):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Positions(0,0), Positions(0,1), Positions(1,0), Positions(1,1)],
            1: [Positions(0,0), Positions(0,1), Positions(1,0), Positions(1,1)],
            2: [Positions(0,0), Positions(0,1), Positions(1,0), Positions(1,1)],
            3: [Positions(0,0), Positions(0,1), Positions(1,0), Positions(1,1)]
        }

# S piece shape that contains the position of each tile of the piece for each rotation state on the cell.
class SPiece(Piece):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Positions(0,1), Positions(0,2), Positions(1,0), Positions(1,1)],
            1: [Positions(0,1), Positions(1,1), Positions(1,2), Positions(2,2)],
            2: [Positions(1,1), Positions(1,2), Positions(2,0), Positions(2,1)],
            3: [Positions(0,0), Positions(1,0), Positions(1,1), Positions(2,1)]
        }

# Z piece shape that contains the position of each tile of the piece for each rotation state on the cell.
class ZPiece(Piece):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Positions(0,0), Positions(0,1), Positions(1,1), Positions(1,2)],
            1: [Positions(0,2), Positions(1,1), Positions(1,2), Positions(2,1)],
            2: [Positions(1,0), Positions(1,1), Positions(2,1), Positions(2,2)],
            3: [Positions(0,1), Positions(1,0), Positions(1,1), Positions(2,0)]
        }

# T piece shape that contains the position of each tile of the piece for each rotation state on the cell.
class TPiece(Piece):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Positions(0,1), Positions(1,0), Positions(1,1), Positions(1,2)],
            1: [Positions(0,1), Positions(1,1), Positions(1,2), Positions(2,1)],
            2: [Positions(1,0), Positions(1,1), Positions(1,2), Positions(2,1)],
            3: [Positions(0,1), Positions(1,0), Positions(1,1), Positions(2,1)]
        }

# I piece shape that contains the position of each tile of the piece for each rotation state on the cell.
class IPiece(Piece):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Positions(1,0), Positions(1,1), Positions(1,2), Positions(1,3)],
            1: [Positions(0,2), Positions(1,2), Positions(2,2), Positions(3,2)],
            2: [Positions(2,0), Positions(2,1), Positions(2,2), Positions(2,3)],
            3: [Positions(0,1), Positions(1,1), Positions(2,1), Positions(3,1)]
        }
