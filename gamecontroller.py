from screen import GameScreen
from paddle import Paddle
from ball import Ball
from collision import CollisionManager
from score import ScoreBoard
from AI import AIController
import turtle


# Controlador principal del juego
class GameController:
    def __init__(self):
        self.screen = GameScreen()
        self.paddle_a = Paddle((-350, 0))
        self.paddle_b = Paddle((350, 0))
        self.ball = Ball()

        self.screen.screen.listen()
        self.screen.screen.onkeypress(self.paddle_a.move_up, "w")
        self.screen.screen.onkeypress(self.paddle_a.move_down, "s")
        self.screen.screen.onkeypress(self.paddle_b.move_up, "Up")
        self.screen.screen.onkeypress(self.paddle_b.move_down, "Down")
        self.scoreboard = ScoreBoard()
        self.ai_controller = AIController(self.paddle_b, self.ball, self.scoreboard)
        self.collision_manager = CollisionManager(self.ball, [self.paddle_a, self.paddle_b])


    def run(self):
        """Ejecuta el bucle principal del juego."""
        while True:
            self.screen.update()
            self.ball.move()

            # Movemos la pala de la IA
            self.ai_controller.move_paddle()

            # Verificamos las colisiones y el marcador
            goal = self.collision_manager.update()
            if goal:
                self.scoreboard.add_point(goal)
                self.ball.reset_position()

            # Verificamos las condiciones de finalización del juego
            if self.scoreboard.score_a == 5 or self.scoreboard.score_b == 5:
                self.stop()
                break

    def stop(self):
        """Detiene el juego."""
        self.screen.close()


# Inicializa y ejecuta el juego
if __name__ == "__main__":
    game = GameController()
    game.run()
