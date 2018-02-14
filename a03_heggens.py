#################################################################################
#Author: Gerardo Soto
#Assignment: A04
#################################################################################

import turtle


def house(t):
    """
    creates house box house
    :param t: turtle object
    :return:
    """
    t.begin_fill()
    for c in range(4):
        t.color("red")
        t.forward(98)
        t.right(90)
    t.end_fill()
    # ...


def top(d):
    """
    Docstring for function_1
    """
    d.color("brown")
    d.begin_fill()
    d.left(45)
    d.forward(70)
    d.right(90)
    d.forward(70)
    d.end_fill()

def things(m):
    m.setposition(40,-98)
    m.color("blue")
    m.begin_fill()
    m.left(90)
    m.forward(40)
    m.right(90)
    m.forward(20)
    m.right(90)
    m.forward(40)
    m.end_fill()
    m.penup()
    m.setpos(15, -20)
    m.pendown

def windows(w):
    w.begin_fill()
    w.color("blue")
    w.forward(15)
    w.left(90)
    w.forward(15)
    w.left(90)
    w.forward(15)
    w.left(90)
    w.forward(15)
    w.left(90)
    w.end_fill()
    w.penup()
    w.setpos(65, -20)
    w.begin_fill()
    w.color("blue")
    w.forward(15)
    w.left(90)
    w.forward(15)
    w.left(90)
    w.forward(15)
    w.left(90)
    w.forward(15)
    w.left(90)
    w.end_fill()

    # ...
def horizon(h):
    """
    makes the grass and sky.
    :param h: the turtle in use.
    :return:
    """
    h.penup()
    h.left(90)
    h.setpos(-350, -98)
    h.pendown()
    h.color("green")
    h.begin_fill()
    h.forward(900)
    h.right(90)
    h.forward(500)
    h.right(90)
    h.forward(1000)
    h.end_fill()
    h.penup()
    h.setpos(350, 98)
    h.pendown()
    h.color("lightblue")
    h.begin_fill()
    h.forward(900)
    h.right(90)
    h.forward(500)
    h.right(90)
    h.forward(1000)
    h.end_fill(

def sun(s):
    """
    makes the sun.
    """
    s.penup()
    s.color("yellow")
    s.shape("circle")
    s.pensize(10)
    s.setpos(250, 200)
    s.stamp()

def main():
    """
    Makes the Roof, the house, the door, and the windows for the house. :^)
    """
    wn = turtle.Screen()
    wn.bgcolor("#DDA0DF")
    alex = turtle.Turtle()
    alex.pensize(2)
    alex.speed(10)
    top(alex)
    alex.setpos(0,0)
    alex.left(45)
    house(alex)
    things(alex)
    windows(alex)
    horizon(alex)
    sun(alex)
    wn.exitonclick()

main()
