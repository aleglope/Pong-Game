# Este módulo manejará la inteligencia artificial de la pala de la computadora.

class AIController:
    def __init__(self, paddle, ball, difficulty):
        self.paddle = paddle
        self.ball = ball
        self.difficulty = difficulty

    def move_paddle(self):
        # Ajusta estos valores según la dificultad y la velocidad de la bola
        speed = 0.1 if self.difficulty == 'Easy' else 0.3
        anticipation_factor = 0.1 if self.difficulty == 'Easy' else 0.2

        # La IA anticipa el movimiento basándose en la dirección vertical de la bola y el movimiento del jugador
        anticipated_y = self.ball.ycor() + (self.ball.dy * anticipation_factor)

        # Mueve la pala de la IA hacia la posición anticipada de la bola
        if self.paddle.ycor() < anticipated_y and abs(self.paddle.ycor() - anticipated_y) > 10:
            self.paddle.sety(self.paddle.ycor() + speed)
        elif self.paddle.ycor() > anticipated_y and abs(self.paddle.ycor() - anticipated_y) > 10:
            self.paddle.sety(self.paddle.ycor() - speed)

