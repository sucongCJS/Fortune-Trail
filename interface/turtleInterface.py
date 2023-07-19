import turtle


class TurtleInterface:
    def __init__(self, tiles) -> None:
        self.chess_len = 20  # the pixel len of a chess
        self.cell_len = self.chess_len * 2
        self.chess_tiles = tiles
        self.chessboard_height = len(tiles)
        self.chessboard_width = len(tiles[0])
        self.canvas_height = self.chessboard_height * 30 + 200
        self.canvas_width = self.chessboard_width * 30

        turtle.setup(self.canvas_width, self.canvas_height, startx=200, starty=100)
        turtle.hideturtle()
        turtle.tracer(False)
        self.path = turtle.Turtle(visible=False)

    def _square(self, x, y):
        """Draw square using path at (x, y)."""
        self.path.up()
        self.path.goto(x, y)
        self.path.down()
        self.path.begin_fill()

        for _ in range(4):
            self.path.forward(self.cell_len)
            self.path.left(90)

        # self.path.end_fill()

    def update(self):   
        turtle.bgcolor('black')
        
        self.path('white')
        for i in range(self.chessboard_height):
            for j in range(self.chessboard_width):
                tile = self.chess_tiles[i][j]

                if tile > 0:
                    x = (i % self.chess_len) 
        

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        turtle.done()

