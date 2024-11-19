import turtle
import math

# Funzione per disegnare una rosa
def draw_rose(petals, size):
    turtle.color("blue")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range(petals):
        # Disegna un petalo
        turtle.circle(size, 60)  # Disegna una curva di un cerchio
        turtle.left(120)  # Ruota a sinistra
        turtle.circle(size, 60)  # Disegna la curva opposta
        turtle.left(60)  # Ruota a sinistra per prepararsi al prossimo petalo
    turtle.end_fill()

# Inizializzazione della tartaruga
turtle.speed(2)

# Posizionamento della tartaruga
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()

# Chiamata alla funzione per disegnare la rosa
draw_rose(6, 100)  # 6 petali, dimensione 100

# Nascondi la tartaruga
turtle.hideturtle()

# Mantieni la finestra aperta
turtle.done()
