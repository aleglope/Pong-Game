class AIController:
    """
    Manages the AI behavior for controlling a paddle in the Pong game, making it react to the ball's movement.
    """

    def __init__(self, paddle, ball, scoreboard):
        """
        Initializes the AIController with a paddle, ball, and scoreboard.

        :param paddle: The paddle object controlled by the AI.
        :param ball: The ball object that the AI will react to.
        :param scoreboard: The scoreboard object to consider the current score for adjusting AI difficulty.
        """
        self.paddle = paddle
        self.ball = ball
        self.scoreboard = scoreboard
        self.base_speed = 0.5  # The base speed of the AI paddle.
        self.base_anticipation = 0.5  # The base anticipation factor of the AI to predict the ball's movement.

    def move_paddle(self):
        """
        Moves the AI paddle by anticipating where the ball will be, adjusting speed and anticipation based on the score.
        """
        # Adjust the speed and anticipation factor based on the current score
        if self.scoreboard.score_a - self.scoreboard.score_b >= 2:
            speed = self.base_speed * 1.5  # Increase speed by 50%
            anticipation_factor = self.base_anticipation * 1.5  # Increase anticipation by 50%
        else:
            speed = self.base_speed
            anticipation_factor = self.base_anticipation

        # The AI anticipates the ball's movement based on its vertical direction
        anticipated_y = self.predict_future_y(anticipation_factor)

        # Move the AI paddle towards the anticipated position of the ball
        if self.ball.dx > 0:  # If the ball is heading towards the AI's paddle
            if self.paddle.ycor() < anticipated_y:
                new_y = self.paddle.ycor() + speed
                self.paddle.sety(min(new_y, self.paddle.upper_bound))  # Don't move above the upper boundary
            elif self.paddle.ycor() > anticipated_y:
                new_y = self.paddle.ycor() - speed
                self.paddle.sety(max(new_y, self.paddle.lower_bound))  # Don't move below the lower boundary

    def predict_future_y(self, anticipation_factor):
        """
        Predicts the future y-coordinate of the ball using its current speed and direction,
        adjusted by the anticipation factor.

        :param anticipation_factor: The factor by which to adjust the prediction.
        :return: The predicted future y-coordinate of the ball.
        """
        # This is a simplified function. In a real game, you would need to account
        # for the ball's bounces on the top and bottom walls.
        ball_distance_to_paddle = self.paddle.xcor() - self.ball.xcor()
        time_until_collision = ball_distance_to_paddle / self.ball.dx
        future_ball_y = self.ball.ycor() + self.ball.dy * time_until_collision * anticipation_factor
        return future_ball_y

