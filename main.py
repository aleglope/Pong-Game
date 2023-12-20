from screen import GameScreen
from paddle import Paddle
from ball import Ball
from collision import CollisionManager
from score import ScoreBoard
from AI import AIController
import turtle

class GameController:
    """
    Main controller for the Pong game, handling game initialization,
    event listening, and the main game loop.
    """

    def __init__(self):
        """Initializes the game by setting up the screen, paddles, ball, scoreboard, AI, and collision manager."""
        self.game_screen = GameScreen()
        self.paddle_a = Paddle((-350, 0))  # Player's paddle
        self.paddle_b = Paddle((350, 0))  # AI's paddle
        self.ball = Ball()
        self.scoreboard = ScoreBoard()
        self.ai_controller = AIController(self.paddle_b, self.ball, self.scoreboard)
        self.collision_manager = CollisionManager(self.ball, [self.paddle_a, self.paddle_b])

        # Setting up keyboard event listeners
        self.game_screen.screen.listen()
        self.game_screen.screen.onkeypress(self.paddle_a.start_moving_up, "w")
        self.game_screen.screen.onkeypress(self.paddle_a.start_moving_down, "s")
        self.game_screen.screen.onkeyrelease(self.paddle_a.stop_moving, "w")
        self.game_screen.screen.onkeyrelease(self.paddle_a.stop_moving, "s")

    def run(self):
        """
        Runs the main loop of the game. This method keeps the game running,
        updates the screen, moves the objects, checks for collisions, and
        updates the scoreboard.
        """
        while True:
            self.game_screen.update()
            self.ball.move()
            self.ai_controller.move_paddle()
            self.paddle_a.move()

            # Check for collisions and update the scoreboard
            goal = self.collision_manager.update()
            if goal:
                self.scoreboard.add_point(goal)
                self.ball.reset_position()  # This method should be implemented in the Ball class

            # Check if the game has ended
            if self.scoreboard.score_a >= 5 or self.scoreboard.score_b >= 5:
                winner = "Player A" if self.scoreboard.score_a > self.scoreboard.score_b else "Player B"
                print(f"The winner is {winner}!")
                break

    def stop(self):
        """
        Stops the game and closes the game window.
        This method should be called to properly close the game.
        """
        self.game_screen.close()

# Start the game
if __name__ == "__main__":
    game_controller = GameController()
    try:
        game_controller.run()
    except turtle.Terminator:
        # Catch the exception thrown by turtle when the window is closed
        pass

