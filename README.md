# Proyecto: Quiz Day

Este proyecto es un juego de trivia interactivo desarrollado en Python. El juego permite a los usuarios responder preguntas sobre varios temas como Geografía, Historia, Deportes, Cine y Cultura y Música, compitiendo por obtener el mejor puntaje. Además, el puntaje final de cada jugador se guarda en un archivo CSV para llevar un registro de los resultados.

## Características

- **Categorías de preguntas:**
  - Geografía
  - Historia
  - Deportes
  - Cine
  - Cultura y Música
- **Formato de las preguntas:**
  - Preguntas de selección múltiple con cuatro opciones (A, B, C, D).
- **Tiempo límite:** Los jugadores tienen un tiempo limitado para responder cada pregunta.
- **Sistema de puntuación:**
  - Respuesta correcta: +10 puntos
  - Tiempo excedido: -5 puntos
  - Respuesta incorrecta: 0 puntos
- **Registro de puntajes:** Los puntajes de los jugadores se almacenan en un archivo CSV al finalizar cada partida.

## Requisitos

- **Python 3.x**
- Bibliotecas necesarias:
  ```bash
  pip install pandas pygame
  ```

## Archivos del Proyecto

- **`main.py`**: Archivo principal que ejecuta el juego.
- **`preguntas.csv`**: Archivo que contiene las preguntas y respuestas organizadas por categoría.
- **`scores.csv`**: Archivo donde se almacenan los puntajes de los jugadores.

## Estructura del Archivo de Preguntas

El archivo `preguntas.csv` contiene las preguntas y respuestas en el siguiente formato:

```csv
Tema,Pregunta,Opción A,Opción B,Opción C,Opción D,Respuesta Correcta
Geografía,¿Cuántos océanos hay en la Tierra?,"Existen 5 océanos en todo el mundo...","Son 4 ocános que son...",Son 2 ocános,Ninguna de las Anteriores,a
...
```

- **Tema**: Categoría de la pregunta (Geografía, Historia, etc.).
- **Pregunta**: El texto de la pregunta.
- **Opciones**: Cuatro opciones posibles (A, B, C, D).
- **Respuesta Correcta**: La opción correcta (A, B, C o D).

## Cómo Jugar

1. Asegúrate de tener instaladas las bibliotecas necesarias ejecutando:
   ```bash
   pip install pandas pygame
   ```

2. Ejecuta el archivo principal:
   ```bash
   python QuizDay.py
   ```
2. Selecciona una categoría de preguntas.
3. Responde cada pregunta dentro del tiempo límite indicado.
4. Al finalizar, se mostrará tu puntaje total y se guardará en el archivo `scores.csv`.

## Estructura del Archivo de Puntajes

El archivo `scores.csv` registra el nombre de los jugadores y sus puntajes en el siguiente formato:

```csv
Nombre,Score
Juan,75
Ana,90
...
```

- **Nombre**: Nombre del jugador.
- **Score**: Puntaje total obtenido en la partida.

## Extensiones y Mejoras Futuras

- Agregar más categorías y preguntas al archivo `preguntas.csv`.
- Implementar un modo multijugador.
- Mejorar la interfaz del juego usando una librería como `curses` o `tkinter`.
- Incorporar gráficas de puntajes acumulados.

## Autor

Desarrollado por William garcia.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes consultar el archivo LICENSE para más detalles.

