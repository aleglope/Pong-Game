from screen import GameScreen
from paddle import Paddle
from ball import Ball
from collision import CollisionManager
from score import ScoreBoard
from AI import AIController
import turtle


# Controlador principal del juegosssss
class GameController:
    def __init__(self):
        # Configuración inicial
        self.game_screen = GameScreen()
        self.paddle_a = Paddle((-350, 0))
        self.paddle_b = Paddle((350, 0))
        self.ball = Ball()
        self.scoreboard = ScoreBoard()
        self.collision_manager = CollisionManager(self.ball, [self.paddle_a, self.paddle_b])
        self.ai_controller = AIController(self.paddle_b, self.ball, 'Easy')

        # Configurar escucha de eventos del teclado
        self.game_screen.screen.listen()
        self.game_screen.screen.onkeypress(self.paddle_a.move_up, "w")
        self.game_screen.screen.onkeypress(self.paddle_a.move_down, "s")

    def run(self):
        """Ejecuta el bucle principal del juego."""
        while True:
            self.game_screen.update()
            self.ball.move()
            self.ai_controller.move_paddle()

            # Verifica las colisiones y actualiza el marcador
            goal = self.collision_manager.update()
            if goal:
                self.scoreboard.add_point(goal)
                self.ball.reset_position()  # Debes implementar este método en la clase Ball

            # Verifica si el juego ha terminado
            if self.scoreboard.score_a >= 5 or self.scoreboard.score_b >= 5:
                winner = "Player A" if self.scoreboard.score_a > self.scoreboard.score_b else "Player B"
                print(f"The winner is {winner}!")
                break

    def stop(self):
        """Detiene el juego y cierra la ventana."""
        self.game_screen.close()


# Inicia el juego
if __name__ == "__main__":
    game_controller = GameController()
    try:
        game_controller.run()
    except turtle.Terminator:
        # Captura la excepción lanzada por turtle cuando se cierra la ventana
        pass
