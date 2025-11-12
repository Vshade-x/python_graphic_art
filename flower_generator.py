from turtle import *
import colorsys

"""Generador de flor con turtle.

Este script dibuja un patrón floral usando arcos repetidos y colores HSV.
Las constantes y valores numéricos del comportamiento (tamaño, velocidad,
iteraciones, incrementos de color) se han dejado exactamente como estaban.

Comentarios añadidos explican qué hace cada parte del código.
"""

# --- Configuración inicial de la ventana y el lápiz ---
bgcolor("black")   # color de fondo (no cambiar)
pensize(2)         # grosor del trazo (no cambiar)
tracer(8)          # actualizaciones de pantalla (mayor = menos actualizaciones)
speed(30)          # velocidad del cursor de turtle (mayor = más rápido)

# Hue inicial para el color (valor en el espacio HSV)
h = 0


def draw(a, n):
    """Dibuja dos segmentos en forma de pétalo.

    Parámetros:
    - a: ángulo de giro entre los dos arcos (degrees)
    - n: factor de radio que escala el radio del arco

    Conserva el mismo comportamiento que antes, sólo que aquí los comandos
    están en líneas separadas para mayor claridad.
    """
    circle(5 + n, 60)
    left(a)
    circle(5 + n, 60)


# --- Bucle principal de dibujo ---
# Repite 300 veces: calcula color, dibuja un pétalo rellenado, y realiza
# algunos trazos adicionales para crear el patrón complejo.
for i in range(300):
    # 1) calcular color usando HSV -> RGB
    # h es la componente hue (tono) que se incrementa cada iteración
    c = colorsys.hsv_to_rgb(h, 1, 1)

    # 2) incrementar hue para la siguiente iteración (paso fijo)
    h += 0.008

    # 3) fijar color de trazo y rellenado (fondo usado como color de relleno)
    color(c, 'black')
    begin_fill()

    # 4) dibujar el pétalo principal (usa los mismos valores que antes)
    draw(90, i / 2)
    end_fill()

    # 5) dibujar el segundo segmento que genera el solapamiento
    draw(160, i * 1.2)

    # 6) mover el lápiz sin dibujar y posicionar para la siguiente iteración
    penup()
    draw(0, 0)
    draw(90, i / 2)
    pendown()


# Mantener la ventana abierta hasta que el usuario la cierre
done()