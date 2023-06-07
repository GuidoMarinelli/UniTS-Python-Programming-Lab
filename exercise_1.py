#
# File: exercise_1.py
#
# Author: G.Marinelli,
#
# Date: 2023/05/27
#
# Version: 1.0
#
# Description: Lezione 3 - Funzioni: Soluzione Esercizio 1.
#
import turtle


# Utilizzando come spunto le righe di codice negli esempi delle funzioni, ed il turtle_program “vol.2”:
def make_window(bkg_color, title):
    """Crea una finestra con background e titolo e ritorna la nuova finestra"""
    w = turtle.Screen()
    w.bgcolor(bkg_color)
    w.title(title)
    return w


def make_turtle(pen_color, pen_size):
    """Crea una nuova tartaruga dato un colore e dimensione del tratto e ritorna la nuova tartaruga"""
    t = turtle.Turtle()
    t.color(pen_color)
    t.pensize(pen_size)
    return t


# 1. Semplificate il `turtle_program` utilizzando le funzioni per creare la finestra e le tartarughe e per disegnare
# i 2 quadrati (`draw_square()`) e i 2 triangoli (`draw_triangle()`)
def draw_square(t, steps):
    """Disegna un quadrato di lato steps"""
    for i in range(4):
        t.forward(steps)
        t.left(90)


def draw_triangle(t, side):
    """Disegna un triangolo di lato steps"""
    for i in range(3):
        t.forward(side)
        t.left(120)


def solution_1():
    """Soluzione compito 1."""
    window = make_window("lightgreen", "Raffaello e Donatello")

    raffaello = make_turtle("red", 5)

    donatello = make_turtle("violet", 1)

    michelangelo = make_turtle("orange", 5)

    leonardo = make_turtle("blue", 5)

    draw_square(raffaello, 50)
    draw_triangle(donatello, 80)
    michelangelo.forward(50)
    draw_square(michelangelo, 50)
    leonardo.forward(100)
    draw_triangle(leonardo, 80)

    window.mainloop()


# 2. Aggiungete al `turtle_program` una funzione `draw_cross()` per disegnare una croce come questa:
def draw_cross(t, steps):
    """Disegna una croce di lato steps"""
    for i in range(4):
        for angle in [90, -90, 90]:
            t.forward(steps)
            t.left(angle)


# 3. Disegnate 5 quadrati concentrici, ognuno 12 passi più grande del precedente
def solution_3():
    """Soluzione compito 3."""
    window = make_window("lightgreen", "Raffaello e Donatello")

    raffaello = make_turtle("blue", 2)

    size = 12

    for square in range(5):
        raffaello.pendown()
        draw_square(raffaello, size)
        raffaello.penup()
        raffaello.goto(-(size / 2), -(size / 2))
        size = size + 12

    window.mainloop()


# 4. Disegnate 3 triangoli allineat ed equispaziati
def solution_4():
    """Soluzione compito 4."""
    window = make_window("lightgreen", "Raffaello e Donatello")

    raffaello = make_turtle("red", 5)

    size = 80
    step = 10

    for triangle in range(3):
        draw_triangle(raffaello, size)
        raffaello.penup()
        raffaello.forward(size + step)
        raffaello.pendown()

    window.mainloop()


# 5. Disegna la figura indicata
def move_turtle(t, steps):
    t.penup()
    t.forward(steps)
    t.pendown()


def solution_5():
    """Soluzione compito 5."""
    window = make_window("lightgreen", "Raffaello e Donatello")

    raffaello = make_turtle("green", 2)
    raffaello.speed(10.0)

    size = 12
    step = 6

    for figure in range(5):
        raffaello.color("green")
        draw_triangle(raffaello, size)
        move_turtle(raffaello, step + size)

        raffaello.color("violet")
        draw_square(raffaello, size)
        move_turtle(raffaello, step + size + (size / 3))

        raffaello.color("blue")
        draw_cross(raffaello, size / 3)

        # spostamento finale della tartaruga
        raffaello.penup()
        raffaello.forward(size * (2 / 3))
        raffaello.left(90)
        move_turtle(raffaello, size + step)

        size = size + 12
        step = step + 5

    window.mainloop()


# programma principale (main)
choice_solution = input('Inserisci quale soluzione al compito vuoi vedere (1 | 3 | 4| 5): ')

if choice_solution == '1':
    solution_1()
elif choice_solution == '3':
    solution_3()
elif choice_solution == '4':
    solution_4()
elif choice_solution == '5':
    solution_5()
