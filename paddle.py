import turtle

class Paddle(turtle.Turtle):
    """Represents a paddle for the Pong game, handling its movement and boundaries."""

    def __init__(self, position):
        """Initializes the paddle with a specific position and default settings."""
        super().__init__()
        self.shape("square")  # The shape of the paddle
        self.color("white")  # The color of the paddle
        self.shapesize(stretch_wid=5, stretch_len=1)  # The size of the paddle
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(position)  # Set the starting position of the paddle
        self.moving_up = False  # State to track if the paddle is moving up
        self.moving_down = False  # State to track if the paddle is moving down
        self.upper_bound = 250  # The upper boundary for the paddle's movement
        self.lower_bound = -250  # The lower boundary for the paddle's movement
        self.speed = 1  # The speed at which the paddle moves

    def start_moving_up(self):
        """Signals the paddle to start moving up."""
        self.moving_up = True
        self.moving_down = False

    def start_moving_down(self):
        """Signals the paddle to start moving down."""
        self.moving_up = False
        self.moving_down = True

    def stop_moving(self):
        """Stops the paddle's movement."""
        self.moving_up = False
        self.moving_down = False

    def move(self):
        """Moves the paddle within the set boundaries based on its current movement state."""
        if self.moving_up and self.ycor() < self.upper_bound:
            self.sety(self.ycor() + self.speed)  # Move the paddle up
        elif self.moving_down and self.ycor() > self.lower_bound:
            self.sety(self.ycor() - self.speed)  # Move the paddle down

