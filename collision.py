# Este módulo manejará la detección de colisiones de la bola con las palas y las paredes.

class CollisionManager:
    def __init__(self, ball, paddles):
        """Inicializa el gestor de colisiones con la bola y las palas."""
        self.ball = ball
        self.paddles = paddles

    def check_paddle_collision(self):
        for paddle in self.paddles:
            if self.ball.distance(paddle) < 50 and abs(self.ball.xcor() - paddle.xcor()) < 10:
                self.ball.bounce_x(paddle)  # Pasamos el objeto paddle como argumento

    def check_wall_collision(self):
        """Verifica la colisión de la bola con las paredes superior e inferior."""
        if abs(self.ball.ycor()) > 290:
            self.ball.bounce_y()

    def check_goal(self):
        """Verifica si la bola ha pasado alguna de las palas, indicando un gol."""
        if self.ball.xcor() > 350:
            return 'Player A'
        elif self.ball.xcor() < -350:
            return 'Player B'
        return None

    def update(self):
        """Actualiza y verifica todas las colisiones."""
        self.check_paddle_collision()
        self.check_wall_collision()
        return self.check_goal()
