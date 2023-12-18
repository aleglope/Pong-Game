import turtle

# Clase base para las palas
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        """Mueve la pala hacia arriba."""
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        """Mueve la pala hacia abajo."""
        y = self.ycor()
        y -= 20
        self.sety(y)
