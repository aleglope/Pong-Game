# 🎮 Juego de Pong con IA 🤖

## Descripción
¡Bienvenido al juego de Pong! 🏓 Este juego clásico cuenta con un sistema de IA que controla uno de los paddles. ¡Intenta vencer a la IA y obtener la mayor puntuación! El juego está desarrollado en Python utilizando el módulo `turtle`.

## Requisitos Previos
Asegúrate de tener Python instalado en tu sistema. Puedes descargar Python desde el [sitio web oficial](https://www.python.org/).

También necesitarás instalar el módulo `turtle` si no está ya instalado. Puedes hacerlo usando pip:
```bash
pip install PythonTurtle
```

## Instrucciones para Jugar
1. **Clona o Descarga el Repositorio**: Obtén los archivos del juego clonando este repositorio o descargando el archivo ZIP y extrayéndolo.

2. **Navega al Directorio del Juego**: Abre una terminal (o símbolo del sistema) y navega al directorio donde se encuentran los archivos del juego.
   ```bash
   cd ruta/al/directorio/del/juego
   ```

3. **Ejecuta el Juego**: Ejecuta el archivo `main.py` para iniciar el juego.
   ```bash
   python main.py
   ```

4. **Controles del Juego**: Usa las siguientes teclas en tu teclado para controlar tu paddle:
   - **W**: Mover hacia arriba ⬆️
   - **S**: Mover hacia abajo ⬇️

5. **Jugabilidad**:
   - **Objetivo**: Intenta que la pelota pase el paddle controlado por la IA (lado derecho) para anotar puntos. Evita que la pelota pase tu paddle (lado izquierdo).
   - **Puntuación**: El primer jugador en alcanzar 5 puntos gana el juego. ¡Buena suerte! 🍀

## Resumen de Archivos
- `main.py`: El archivo principal para ejecutar el juego.
- `screen.py`: Configura y gestiona la pantalla del juego.
- `paddle.py`: Contiene la clase `Paddle`, que gestiona el movimiento y los límites del paddle.
- `ball.py`: Contiene la clase `Ball`, que gestiona el movimiento y el comportamiento de la pelota.
- `collision.py`: Contiene la clase `CollisionManager`, que maneja las colisiones entre la pelota y los paddles y las paredes.
- `score.py`: Contiene la clase `ScoreBoard`, que muestra y actualiza la puntuación de los jugadores.
- `AI.py`: Contiene la clase `AIController`, que gestiona el comportamiento del paddle controlado por la IA.

## Solución de Problemas
- Si el juego no se inicia, asegúrate de que todos los archivos necesarios (`main.py`, `screen.py`, `paddle.py`, `ball.py`, `collision.py`, `score.py`, `AI.py`) estén en el mismo directorio.
- Asegúrate de tener los permisos necesarios para ejecutar Python y acceder a los archivos en el directorio del juego.
- Asegúrate de estar usando una versión compatible de Python (preferiblemente 3.x).

¡Disfruta jugando al Pong! 🏓 Trata de vencer a la IA y diviértete. 😃

