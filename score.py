import turtle

class ScoreBoard(turtle.Turtle):
    """Represents the scoreboard in the Pong game, displaying each player's score."""

    def __init__(self):
        """Initializes the scoreboard with default settings."""
        super().__init__()
        self.color("white")  # Set the color of the scoreboard text
        self.penup()  # Lift the pen to prevent drawing lines
        self.hideturtle()  # Hide the turtle icon since we only need to display text
        self.goto(0, 260)  # Position the scoreboard at the top of the screen
        self.score_a = 0  # Initialize score for Player A
        self.score_b = 0  # Initialize score for Player B
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the current score display and updates it with the new score."""
        self.clear()  # Clear the previous score display
        # Write the new score to the screen
        self.write(f"Player A: {self.score_a}  Player B: {self.score_b}",
                   align="center", font=("Courier", 24, "normal"))

    def add_point(self, player):
        """Adds a point to the specified player and updates the scoreboard display."""
        if player == 'Player A':
            self.score_a += 1  # Increment score for Player A
        elif player == 'Player B':
            self.score_b += 1  # Increment score for Player B
        self.update_scoreboard()  # Update the scoreboard with the new score

