class Colors:
    DARK_GRAY = (26, 31, 40)
    RED = (232, 18, 18)
    GREEN = (47,230,23)
    BLUE = (13, 64, 216)
    YELLOW = (237, 234, 4)
    PURPLE = (166, 0, 247)
    PINK = (255, 105, 180)
    ORANGE = (255, 165, 0)
    WHITE = (255, 255, 255)
    DARK_BLUE = (44, 44, 127)
    LIGHT_BLUE = (59,85,162)

    """ 
    classmethod is a decorator that is an alternative constructor.
    Instead of operating on an object instance, it operates on the class itself. 
    If you need to manipulate or access attributes that are shared by all instances 
    of the class, class methods are useful.
    """

    @classmethod
    def get_pieces_colors(cls): # cls is the class itself.
        # return the color of the piece.
        return [cls.DARK_GRAY, cls.RED, cls.GREEN, cls.BLUE, cls.YELLOW, cls.PURPLE, cls.PINK, cls.ORANGE]