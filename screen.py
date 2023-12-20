import turtle

class GameScreen:
    """Class for the initial setup and management of the game screen."""

    def __init__(self):
        """Initializes the game screen with its properties."""
        self.screen = turtle.Screen()
        self.screen.title("Pong Game")  # Set the title of the game window
        self.screen.bgcolor("black")  # Set the background color of the game window
        self.screen.setup(width=800, height=600)  # Set the size of the game window
        self.screen.tracer(0)  # Disable automatic screen updates for better control over the animation

    def update(self):
        """Updates the game screen. Call this method to refresh the screen."""
        self.screen.update()

    def close(self):
        """Closes the game screen. Call this method to close the game window and exit the game."""
        self.screen.bye()
