class CollisionManager:
    """
    Manages the detection of collisions within the Pong game, specifically collisions
    between the ball and the paddles, and the ball and the walls.
    """

    def __init__(self, ball, paddles):
        """
        Initializes the CollisionManager with the ball and paddles.

        :param ball: The ball object which will be checked for collisions.
        :param paddles: A list of paddle objects to check for collisions with the ball.
        """
        self.ball = ball
        self.paddles = paddles

    def check_paddle_collision(self):
        """
        Checks for and handles collisions between the ball and any of the paddles.
        """
        for paddle in self.paddles:
            # If the ball is close enough to a paddle, a collision is detected.
            if self.ball.distance(paddle) < 50 and abs(self.ball.xcor() - paddle.xcor()) < 10:
                self.ball.bounce_x(paddle)  # Pass the paddle object as an argument

    def check_wall_collision(self):
        """
        Checks for and handles collisions between the ball and the top or bottom walls.
        """
        # If the ball hits the top or bottom of the screen, it bounces.
        if abs(self.ball.ycor()) > 290:
            self.ball.bounce_y()

    def check_goal(self):
        """
        Checks if the ball has passed beyond a paddle, indicating a goal has been scored.

        :return: The scoring player's identifier or None if no goal has been scored.
        """
        # If the ball goes beyond the right paddle, Player A scores.
        if self.ball.xcor() > 350:
            return 'Player A'
        # If the ball goes beyond the left paddle, Player B scores.
        elif self.ball.xcor() < -350:
            return 'Player B'
        return None

    def update(self):
        """
        Updates and checks for all types of collisions.

        :return: A string indicating which player scored, or None if no goal occurred.
        """
        self.check_paddle_collision()
        self.check_wall_collision()
        return self.check_goal()

