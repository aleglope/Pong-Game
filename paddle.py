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
        self.moving_up = False
        self.moving_down = False
        self.upper_bound = 250  # Límite superior
        self.lower_bound = -250  # Límite inferior
        self.speed = 1  # Velocidad de movimiento de la pala

    def start_moving_up(self):
        self.moving_up = True
        self.moving_down = False

    def start_moving_down(self):
        self.moving_up = False
        self.moving_down = True

    def stop_moving(self):
        self.moving_up = False
        self.moving_down = False

    def move(self):
        if self.moving_up and self.ycor() < self.upper_bound:
            self.sety(self.ycor() + self.speed)
        elif self.moving_down and self.ycor() > self.lower_bound:
            self.sety(self.ycor() - self.speed)
