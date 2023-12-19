class AIController:
    def __init__(self, paddle, ball, scoreboard):
        self.paddle = paddle
        self.ball = ball
        self.scoreboard = scoreboard
        self.base_speed = 0.5  # La velocidad base de la IA
        self.base_anticipation = 0.5  # El factor de anticipación base de la IA

    def move_paddle(self):
        # Ajusta la velocidad y el factor de anticipación basados en la puntuación actual
        if self.scoreboard.score_a - self.scoreboard.score_b >= 2:
            speed = self.base_speed * 1.0  # Aumenta la velocidad en un 50%
            anticipation_factor = self.base_anticipation * 4.0  # Mejora la anticipación en un 50%
        else:
            speed = self.base_speed
            anticipation_factor = self.base_anticipation

        # La IA anticipa el movimiento basándose en la dirección vertical de la bola
        anticipated_y = self.predict_future_y(anticipation_factor)

        # Mueve la pala de la IA hacia la posición anticipada de la bola
        if self.ball.dx > 0:  # Si la bola se dirige hacia la pala de la IA
            if self.paddle.ycor() < anticipated_y:
                new_y = self.paddle.ycor() + speed
                self.paddle.sety(min(new_y, self.paddle.upper_bound))  # No mover arriba del límite superior
            elif self.paddle.ycor() > anticipated_y:
                new_y = self.paddle.ycor() - speed
                self.paddle.sety(max(new_y, self.paddle.lower_bound))  # No mover debajo del límite inferior

    def predict_future_y(self, anticipation_factor):
        # Esta es una función simplificada. En un juego real, deberías tener en cuenta
        # los rebotes de la bola en las paredes superior e inferior.
        ball_distance_to_paddle = self.paddle.xcor() - self.ball.xcor()
        time_until_collision = ball_distance_to_paddle / self.ball.dx
        future_ball_y = self.ball.ycor() + self.ball.dy * time_until_collision * anticipation_factor
        return future_ball_y
