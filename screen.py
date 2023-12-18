import turtle

# Configuración inicial de la pantalla
class GameScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)  # Desactiva la actualización automática

    def update(self):
        """Actualiza la pantalla del juego."""
        self.screen.update()

    def close(self):
        """Cierra la pantalla del juego."""
        self.screen.bye()
