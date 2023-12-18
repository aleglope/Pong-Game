# Este módulo manejará la inteligencia artificial de la pala de la computadora.

class AIController:
    def __init__(self, paddle, ball, difficulty):
        """Inicializa el controlador de IA con la pala, la bola y la dificultad."""
        self.paddle = paddle
        self.ball = ball
        self.difficulty = difficulty

    def move_paddle(self):
        """Mueve la pala de la computadora según la posición de la bola y la dificultad."""
        if self.difficulty == 'Easy':
            speed = 0.1
        elif self.difficulty == 'Hard':
            speed = 0.3

        if self.paddle.ycor() < self.ball.ycor() and abs(self.paddle.ycor() - self.ball.ycor()) > 10:
            self.paddle.sety(self.paddle.ycor() + speed)
        elif self.paddle.ycor() > self.ball.ycor() and abs(self.paddle.ycor() - self.ball.ycor()) > 10:
            self.paddle.sety(self.paddle.ycor() - speed)
