#################################################################################
# Authors: Joseph Opaleye
# Usernames: opaleyej
# Assignment: A03
##################################################################################

import turtle


def draw_laptop_screen1():
    """
    Draw a laptop
    :return:
    """
    laptop_screen1 = turtle.Turtle()
    laptop_screen1.pensize(5)
    laptop_screen1.color("grey")
    laptop_screen1.penup()
    laptop_screen1.goto(-90, -10)
    laptop_screen1.pendown()
    laptop_screen1.begin_fill()
    for i in range(2):
        laptop_screen1.forward(200)
        laptop_screen1.left(90)
        laptop_screen1.forward(180)
        laptop_screen1.left(90)
    laptop_screen1.end_fill()


def draw_keyboard_part():
    """
    Draw a laptop keyboard seat
    :return:
    """
    keyboard_part= turtle.Turtle()
    keyboard_part.pensize(5)
    keyboard_part.color("black")
    keyboard_part.penup()
    keyboard_part.goto(-90, -10)
    keyboard_part.pendown()
    keyboard_part.begin_fill()
    keyboard_part.right(120)
    keyboard_part.forward(130)
    keyboard_part.left(120)
    keyboard_part.forward(235)
    keyboard_part.left(75)
    keyboard_part.forward(120)
    keyboard_part.end_fill()


def draw_screen2():
    """
    Draw a laptop screen
    :return:
    """
    screen2 = turtle.Turtle()
    screen2.pensize(5)
    screen2.color("white")
    screen2.penup()
    screen2.goto(-70, 15)
    screen2.pendown()
    screen2.begin_fill()
    for i in range(2):
        screen2.forward(160)
        screen2.left(90)
        screen2.forward(140)
        screen2.left(90)
    screen2.end_fill()


def draw_keyboard2():
    """
    Draw a laptop keyboard
    :return:
    """
    keyboard2= turtle.Turtle()
    keyboard2.pensize(5)
    keyboard2.color("white")
    keyboard2.penup()
    keyboard2.goto(-75, -30)
    keyboard2.pendown()
    keyboard2.begin_fill()
    keyboard2.right(120)
    keyboard2.forward(70)
    keyboard2.left(120)
    keyboard2.forward(175)
    keyboard2.left(75)
    keyboard2.forward(63)
    keyboard2.end_fill()



def main():
    wn = turtle.Screen()
    wn.bgcolor('white')
    wn.colormode(255)
    draw_laptop_screen1()
    draw_keyboard_part()
    draw_screen2()
    draw_keyboard2()

    wn.exitonclick()

main()






