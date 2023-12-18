import turtle

# Este módulo manejará la puntuación del juego.

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        """Inicializa el marcador del juego."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_a = 0
        self.score_b = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Actualiza y muestra la puntuación en la pantalla."""
        self.clear()
        self.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align="center", font=("Courier", 24, "normal"))

    def add_point(self, player):
        """Añade un punto al jugador especificado y actualiza el marcador."""
        if player == 'Player A':
            self.score_a += 1
        elif player == 'Player B':
            self.score_b += 1
        self.update_scoreboard()
