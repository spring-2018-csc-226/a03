######################################################################
# Author: Miranda Flannery
# Username: flannerymi
#
# Assignment: A03

######################################################################
# Acknowledgements:
#Adapted some code from Scott Heggen and from the online book.


# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle


def draw_house():
    house = turtle.Turtle()
    house.pensize(5)
    house.color("firebrick")
    house.penup()
    house.goto(-150, -200)
    house.pendown()
    house.begin_fill()
    for i in range(2):
        house.forward(300)
        house.left(90)
        house.forward(250)
        house.left(90)
    house.end_fill()
    house.hideturtle()


def draw_roof():
    roof = turtle.Turtle()
    roof.pensize(5)
    roof.color("dimgrey")
    roof.penup()
    roof.goto(-150, 50)
    roof.pendown()
    roof.begin_fill()
    roof.left(45)
    roof.forward(212)
    roof.right(90)
    roof.forward(212)
    roof.end_fill()
    roof.hideturtle()


def draw_door():
    door = turtle.Turtle()
    door.pensize(3)
    door.color('black')
    door.penup()
    door.goto(-20, -200)
    door.pendown()
    door.begin_fill()
    for j in range(2):
        door.forward(40)
        door.left(90)
        door.forward(80)
        door.left(90)
    door.end_fill()
    door.hideturtle()


def draw_window():
    window = turtle.Turtle()
    window.pensize(3)
    window.color('white')
    window.penup()
    #draws first window
    window.goto(-110, -150)
    window.pendown()
    window.begin_fill()
    for l in range(4):
        window.forward(60)
        window.left(90)
    window.end_fill()
    #draws second window
    window.penup()
    window.goto(50, -150)
    window.pendown()
    window.begin_fill()
    for l in range(4):
        window.forward(60)
        window.left(90)
    window.end_fill()
    #draws third window
    window.penup()
    window.goto(-110, -50)
    window.pendown()
    window.begin_fill()
    for l in range(4):
        window.forward(60)
        window.left(90)
    window.end_fill()
    #draws fourth window
    window.penup()
    window.goto(50, -50)
    window.pendown()
    window.begin_fill()
    for l in range(4):
        window.forward(60)
        window.left(90)
    window.end_fill()
    #draws fifth window
    window.penup()
    window.goto(0, -80)
    window.pendown()
    window.begin_fill()
    window.circle(20)
    window.end_fill()
    window.hideturtle()


def window_lines():
    lines = turtle.Turtle()
    lines.pensize(3)
    lines.color('black')
    #lines for 1st window
    lines.penup()
    lines.goto(-110, -120)
    lines.pendown()
    lines.forward(60)
    lines.right(90)
    lines.penup()
    lines.goto(-80, -90)
    lines.pendown()
    lines.forward(60)
    lines.left(90)
    #lines for 2nd window
    lines.penup()
    lines.goto(50, -120)
    lines.pendown()
    lines.forward(60)
    lines.right(90)
    lines.penup()
    lines.goto(80, -90)
    lines.pendown()
    lines.forward(60)
    lines.left(90)
    #lines for 3rd window
    lines.penup()
    lines.goto(-110, -20)
    lines.pendown()
    lines.forward(60)
    lines.right(90)
    lines.penup()
    lines.goto(-80, 10)
    lines.pendown()
    lines.forward(60)
    lines.left(90)
    #lines for 4th window
    lines.penup()
    lines.goto(50, -20)
    lines.pendown()
    lines.forward(60)
    lines.right(90)
    lines.penup()
    lines.goto(80, 10)
    lines.pendown()
    lines.forward(60)
    lines.left(90)
    #lines for 5th window
    lines.penup()
    lines.goto(-20, -60)
    lines.pendown()
    lines.forward(40)
    lines.right(90)
    lines.penup()
    lines.goto(0, -40)
    lines.pendown()
    lines.forward(40)
    lines.left(90)
    lines.hideturtle()


def draw_trees():
    tree = turtle.Turtle()
    tree.pensize(5)
    #1st tree trunk
    tree.pencolor((220, 125, 40))
    tree.penup()
    tree.goto(-250, -200)
    tree.pendown()
    tree.fillcolor((220, 125, 40))
    tree.begin_fill()
    for h in range(2):
        tree.forward(30)
        tree.left(90)
        tree.forward(80)
        tree.left(90)
    tree.end_fill()
    #1st tree top
    tree.pencolor((50, 200, 70))
    tree.penup()
    tree.goto(-250, -120)
    tree.pendown()
    tree.fillcolor((50, 200, 70))
    tree.begin_fill()
    tree.forward(30)
    tree.right(45)
    tree.circle(15, 200)
    for h in range(7):
        tree.right(130)
        tree.circle(15, 180)
    tree.end_fill()


def draw_sun():
    sun = turtle.Turtle()
    sun.pencolor('yellow')
    sun.pensize(5)
    sun.penup()
    sun.goto(225, 175)
    sun.pendown()
    size = 3
    for g in range(50):
        size = size + 1
        sun.forward(size)
        sun.right(45)
    sun.hideturtle()


def main():
    wn = turtle.Screen()
    wn.bgcolor('lightblue')
    wn.colormode(255)
    draw_house()
    draw_roof()
    draw_door()
    draw_window()
    window_lines()
    draw_trees()
    draw_sun()
    wn.exitonclick()


main()
