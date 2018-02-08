#############################################################################
# Author: Erin Powers
# Username: powerse
# Assignment 03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#############################################################################

import turtle


def specs(t, draw_col, fill_col, t_shape):
    t.color(draw_col, fill_col)
    t.shape(t_shape)


def pos(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def solid_cir(t, rad):
    t.begin_fill()
    t.circle(rad)
    t.end_fill()


def feat(t, x, y, rad):
    pos(t, x, y)
    solid_cir(t, rad)


def band(t, col):
    t.color(col)
    t.setheading(45)
    pos(t, -130, 90)
    t.stamp()
    for i in range(19):
        t.right(4.5)
        t.forward(15)
        t.stamp()
    t.setheading(0)


def bow_center(t):
    t.color("pink")
    pos(t, -25, 145)
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.end_fill()


def bow(t):
    pos(t, 0, 160)
    t.begin_fill()
    t.left(30)
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.right(120)
    t.forward(300)
    t.left(120)
    t.forward(150)
    t.left(120)
    t.forward(150)
    t.end_fill()


def main():
    wn = turtle.Screen()
    wn.bgcolor(.3137, .0667, .7045)
    minnie = turtle.Turtle()
    minnie.speed(0)
    specs(minnie, "black", "black", "circle")
    feat(minnie, 0, -150, 150)
    feat(minnie, 125, 100, 85)
    feat(minnie, -125, 100, 85)
    band(minnie, "white")
    bow_center(minnie)
    bow(minnie)
    wn.exitonclick()


main()
