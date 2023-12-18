import turtle

# Clase para la bola
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.1  # Velocidad de la bola en el eje X
        self.dy = 0.1  # Velocidad de la bola en el eje Y

    def move(self):
        """Mueve la bola."""
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

    def bounce_y(self):
        """Invierte la dirección vertical de la bola."""
        self.dy *= -1

    # Puedes necesitar un método similar para el rebote horizontal
    def bounce_x(self):
        """Invierte la dirección horizontal de la bola."""
        self.dx *= -1

    def reset_position(self):
        """Coloca la bola de nuevo en el centro y la lanza en una dirección aleatoria."""
        self.goto(0, 0)
        self.dx *= -1  # Cambia la dirección horizontal
        # Puedes también querer cambiar la dirección vertical o ajustar la velocidad