import turtle
import time
import random


class Ball(turtle.Turtle):
    MAX_SPEED = 3.0  # Velocidad máxima
    SPEED_INCREMENT = 0.3  # Incremento de velocidad en cada colisión
    SPEED_REDUCTION_FACTOR = 1.5  # Factor de reducción de velocidad
    DEFAULT_SPEED = 0.2  # Velocidad predeterminada

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = self.DEFAULT_SPEED
        self.dy = self.DEFAULT_SPEED
        self.last_collision_time = time.time()

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        self.adjust_speed_over_time()

    def bounce_y(self):
        self.dy *= -1
        self.last_collision_time = time.time()

    def bounce_x(self, paddle):
        self.dx *= -1
        self.adjust_speed_based_on_paddle(paddle)

    def adjust_speed_based_on_paddle(self, paddle):
        if paddle.moving_up:
            self.dy = min(self.dy + self.SPEED_INCREMENT, self.MAX_SPEED)
        elif paddle.moving_down:
            self.dy = max(self.dy - self.SPEED_INCREMENT, -self.MAX_SPEED)

    def adjust_speed_over_time(self):
        current_time = time.time()
        if current_time - self.last_collision_time > 3:  # Ajusta la velocidad después de 3 segundos sin colisión
            # Asegúrate de que la velocidad se reduce solo si es mayor que la velocidad predeterminada
            if abs(self.dx) > self.DEFAULT_SPEED:
                # Aplica una reducción proporcional para evitar que la bola se detenga de golpe
                self.dx -= self.dx * (self.SPEED_REDUCTION_FACTOR / self.MAX_SPEED)
                self.dx = max(min(self.dx, self.MAX_SPEED), -self.MAX_SPEED)

            if abs(self.dy) > self.DEFAULT_SPEED:
                self.dy -= self.dy * (self.SPEED_REDUCTION_FACTOR / self.MAX_SPEED)
                self.dy = max(min(self.dy, self.MAX_SPEED), -self.MAX_SPEED)

            # Establece un límite inferior en la velocidad predeterminada
            if abs(self.dx) < self.DEFAULT_SPEED:
                self.dx = self.DEFAULT_SPEED if self.dx > 0 else -self.DEFAULT_SPEED
            if abs(self.dy) < self.DEFAULT_SPEED:
                self.dy = self.DEFAULT_SPEED if self.dy > 0 else -self.DEFAULT_SPEED

    def reset_position(self):
        self.goto(0, 0)
        self.dx = self.DEFAULT_SPEED * random.choice([-1, 1])
        self.dy = self.DEFAULT_SPEED * random.choice([-1, 1])