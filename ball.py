import turtle
import time
import random


class Ball(turtle.Turtle):
    """Represents the ball in the Pong game, handling its movement and collision behavior."""

    MAX_SPEED = 3.0  # The maximum speed the ball can achieve.
    SPEED_INCREMENT = 0.3  # The amount of speed increase on paddle collision.
    SPEED_REDUCTION_FACTOR = 1.5  # The factor by which the speed is reduced over time.
    DEFAULT_SPEED = 0.2  # The default speed of the ball at the start of the game and after resetting.

    def __init__(self):
        """Initialize the ball with default settings."""
        super().__init__()
        self.shape("circle")  # The shape of the ball
        self.color("white")  # The color of the ball
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(0, 0)  # Start the ball at the center of the screen
        self.dx = self.DEFAULT_SPEED  # The horizontal speed of the ball
        self.dy = self.DEFAULT_SPEED  # The vertical speed of the ball
        self.last_collision_time = time.time()  # Record the time of the last collision

    def move(self):
        """Move the ball in the game space and adjust its speed over time."""
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        self.adjust_speed_over_time()

    def bounce_y(self):
        """Invert the vertical movement of the ball on collision with top or bottom walls."""
        self.dy *= -1
        self.last_collision_time = time.time()

    def bounce_x(self, paddle):
        """Invert the horizontal movement of the ball on collision with a paddle."""
        self.dx *= -1
        self.adjust_speed_based_on_paddle(paddle)

    def adjust_speed_based_on_paddle(self, paddle):
        """Adjust the ball's vertical speed based on the paddle's movement."""
        if paddle.moving_up:
            self.dy = min(self.dy + self.SPEED_INCREMENT, self.MAX_SPEED)
        elif paddle.moving_down:
            self.dy = max(self.dy - self.SPEED_INCREMENT, -self.MAX_SPEED)

    def adjust_speed_over_time(self):
        """Gradually reduce the ball's speed if there hasn't been a collision for a set period."""
        current_time = time.time()
        if current_time - self.last_collision_time > 3:  # Adjust speed after 3 seconds without collision
            # Ensure that the speed is only reduced if it is greater than the default speed
            if abs(self.dx) > self.DEFAULT_SPEED:
                # Apply a proportional reduction to avoid stopping the ball abruptly
                self.dx -= self.dx * (self.SPEED_REDUCTION_FACTOR / self.MAX_SPEED)
                self.dx = max(min(self.dx, self.MAX_SPEED), -self.MAX_SPEED)

            if abs(self.dy) > self.DEFAULT_SPEED:
                self.dy -= self.dy * (self.SPEED_REDUCTION_FACTOR / self.MAX_SPEED)
                self.dy = max(min(self.dy, self.MAX_SPEED), -self.MAX_SPEED)

            # Set a lower limit at the default speed
            if abs(self.dx) < self.DEFAULT_SPEED:
                self.dx = self.DEFAULT_SPEED if self.dx > 0 else -self.DEFAULT_SPEED
            if abs(self.dy) < self.DEFAULT_SPEED:
                self.dy = self.DEFAULT_SPEED if self.dy > 0 else -self.DEFAULT_SPEED

    def reset_position(self):
        """Reset the ball to the center of the screen with a random direction."""
        self.goto(0, 0)
        self.dx = self.DEFAULT_SPEED * random.choice([-1, 1])  # Randomize the horizontal direction
        self.dy = self.DEFAULT_SPEED * random.choice([-1, 1])  # Randomize the vertical direction
