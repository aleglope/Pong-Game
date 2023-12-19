import turtle
import time
import random


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.2  # Velocidad inicial de la bola en el eje X
        self.dy = 0.2  # Velocidad inicial de la bola en el eje Y
        self.default_dx = 0.2  # Velocidad horizontal predeterminada
        self.default_dy = 0.2  # Velocidad vertical predeterminada
        self.last_collision_time = time.time()
        self.time_to_start_slowing = 1.0  # Tiempo en segundos para comenzar a disminuir la velocidad
        self.slowing_factor = 0.5 # Factor de reducción de la velocidad para el enfriamiento
        self.time_of_last_adjustment = time.time()  # Nuevo: Guarda la última vez que se ajustó la velocidad

    def move(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

        # Comienza a reducir la velocidad si han pasado más de 2 segundos desde el último golpe
        if (time.time() - self.last_collision_time) > self.time_to_start_slowing:
            self.adjust_speed()

    def bounce_y(self):
        self.dy *= -1
        self.last_collision_time = time.time()

    def bounce_x(self, paddle):
        """Invierte la dirección horizontal de la bola y la acelera si la pala se está moviendo."""
        self.dx *= -1

        # Incrementa ligeramente la velocidad en la dirección y si la pala se mueve hacia arriba o hacia abajo
        if paddle.moving == 'up':
            self.dy += 0.5  # Aumenta la velocidad un 10%
        elif paddle.moving == 'down':
            self.dy -= 0.5  # Disminuye la velocidad un 10%

        # Limita la velocidad máxima para evitar que se acelere demasiado
        max_speed = 3.0
        self.dy = max(min(self.dy, max_speed), -max_speed)

    def adjust_speed(self):
        """Reduce la velocidad de la bola gradualmente hasta la velocidad predeterminada si ha sido excedida."""
        # Verifica si la velocidad ha excedido el valor predeterminado y ajusta si es necesario
        if abs(self.dx) > self.default_dx or abs(self.dy) > self.default_dy:
            self.dx *= 0.99 if abs(self.dx) > self.default_dx else 1.0
            self.dy *= 0.99 if abs(self.dy) > self.default_dy else 1.0
            self.time_of_last_adjustment = time.time()

    def reset_position(self):
        """Resetea la posición y la velocidad de la bola."""
        self.goto(0, 0)  # Coloca la bola en el centro de la pantalla
        self.dx = self.default_dx * random.choice([-1, 1])  # Reinicia la velocidad horizontal con una dirección aleatoria
        self.dy = self.default_dy * random.choice([-1, 1])  # Reinicia la velocidad vertical con una dirección aleatoria