import turtle

# Clase base para las palas
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.moving = None
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.moving_up = False
        self.moving_down = False
        self.upper_bound = 250  # Límite superior
        self.lower_bound = -250  # Límite inferior

    def move_up(self):
        if self.ycor() < self.upper_bound:  # Verifica si la pala está por debajo del límite superior
            y = self.ycor() + 20
            self.sety(y)
        self.moving_up = True
        self.moving_down = False
        self.moving = 'up'

    def move_down(self):
        if self.ycor() > self.lower_bound:  # Verifica si la pala está por encima del límite inferior
            y = self.ycor() - 20
            self.sety(y)
        self.moving_up = False
        self.moving_down = True
        self.moving = 'down'
