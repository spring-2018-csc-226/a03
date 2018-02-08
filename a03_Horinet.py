#######################################################
# Author: Tayttum Horine
# Purpose: To better understand turtles and incorporate new ideas
#######################################################


import turtle

def make_square (t): # creates bottom of house
    """
    The function creates the base of the house.
    :param t: turtle class
    :return: none
    """
    t.color("#DC143C")
    t.pensize(3)
    t.penup()
    t.goto(-50,0)
    t.pendown()
    t.begin_fill()
    for i in range (4):
        t.fd(100)
        t.rt(90)
    t.end_fill()

def make_door (t):
    """
    This function creates the door of the house.
    :param t: turtle
    :return: none
    """
    t.penup()
    t.color("blue")
    t.goto(-10,-100)
    t.pendown()
    t.begin_fill()
    for i in range (2):
        t.fd(20)
        t.lt(90)
        t.fd(40)
        t.lt(90)
    t.end_fill()


def make_roof  (t):  # creates roof
    """
    This function creates the roof of the house.
    :param t: turtle
    :return: none
    """
    t.color('#DC130C')
    t.pensize(3)
    t.begin_fill()
    t.bk(25)
    t.goto(0,50)
    t.goto(75,0)
    t.bk(125)
    t.end_fill()


def make_sun (t):
    """
    This function creates a sun in the sky.
    :param t: turtle
    :return: none
    """
    t.color("#ffff00")
    t.penup()
    t.goto (220,170)
    t.pendown()
    t.begin_fill()
    t.circle(45)
    t.end_fill()

def make_window1 (t):
    """
    This function creates the first window
    :param t: turtle
    :return: none
    """
    t.color("black")
    t.penup()
    t.goto(-30,-5)
    t.pendown()
    t.speed(2)
    t.fillcolor("white")
    t.begin_fill()
    for i in range (8):
        t.fd(6)
        t.rt(45)
        t.fd(6)
    t.end_fill()

def make_window2 (t):
    """
    This function creates the second window
    :param t: turtle
    :return: none
    """
    t.color("black")
    t.penup()
    t.goto(30,-5)
    t.pendown()
    t.speed(2)
    t.fillcolor("white")
    t.begin_fill()
    for i in range (8):
        t.fd(6)
        t.rt(45)
        t.fd(6)
    t.end_fill()

def make_cloud(t):
    t.color("white")
    t.penup()
    t.goto(-190,160)
    t.pendown()
    for i in range (3):
        t.begin_fill()
        t.circle(30)
        t.end_fill()
        t.penup()
        t.fd(30)
        t.pendown()

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("#87ceeb")

    make_square(t)

    make_roof(t)

    make_sun(t)

    make_cloud(t)

    make_door(t)

    make_window1(t)

    make_window2(t)

    t.color("#FF1493")
    t.penup()
    t.setpos(0, 90)
    t.pendown()
    t.write("Tayttums Smol Home", align='center', font=("Times New Roman", 20 ))

    wn.exitonclick()
main()
