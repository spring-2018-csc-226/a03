######################################################################
# Author: Ricardo Santos
# Username: santosr
#
# Assignment: A3: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
######################################################################
# Purpose:
# Grow to appreciate pair programming a little more
# Continue practicing creating and using functions
# More practice on using the turtle library
# Learn about how computers represent colors
# Learn about source control and git
######################################################################
# Acknowledgements:
# https://docs.python.org/3.0/library/turtle.html  turtle info
# http://www.wolframalpha.com/widgets/gallery/view.jsp?id=c0abe9808671bca189c7e6a560739ae4 for colors
##################################################################
import turtle


def make_turtle(color):
    """
    Make a turtle
    :param color: gives color of turtle
    :return: turtle object
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(5)
    t.speed(10)
    t.hideturtle()
    return t


def set_turtle(name, coor1, coor2):
    """
    To move the turtles into position for drawing
    :param name: name of the
    :param coor1:
    :param coor2:
    :return: none
    """
    name.penup()
    name.goto(coor1, coor2)
    name.pendown()


def make_rectangle(name, length1, length2):
    """
    Makes a rectangle or square
    :param name: name of the turtle drawing
    :param length1: one side of the rectangle
    :param length2: other side of rectangle
    :return: none
    """
    for rectangles in range(2):
        name.forward(length1)
        name.left(90)
        name.forward(length2)
        name.left(90)


def make_trianlge(name, side1):
    """
    To make a triangle
    :param name: is the name of the turtle drawing
    :param side1: sides of the triangle
    :return: none
    """
    for tri in range(3):
        name.forward(side1)
        name.left(120)


def main():
    wn = turtle.Screen()            # make the screen
    wn.bgcolor('lightblue')

    rico = make_turtle('black')     # make the base of the house
    rico.begin_fill()
    wn.colormode(255)
    rico.fillcolor((220, 20, 60))   # give it a rgb color
    set_turtle(rico, -200, -250)
    make_rectangle(rico, 300, 300)
    rico.end_fill()

    john = make_turtle('black')     # make chimney
    john.begin_fill()
    set_turtle(john, 30, 50)
    make_rectangle(john, 50, 150)
    john.end_fill()

    josh = make_turtle('black')     # make roof
    set_turtle(josh, -200, 50)
    josh.fillcolor('white')
    josh.begin_fill()
    make_trianlge(josh, 300)
    josh.end_fill()

    dean = make_turtle('black')     # make door
    dean.begin_fill()
    set_turtle(dean, -40, -250)
    make_rectangle(dean, 100, 200)
    dean.end_fill()
    make_trianlge(josh, 300)
    josh.end_fill()

    vent = make_turtle('black')     # make the frame for window
    vent.begin_fill()
    vent.fillcolor('white')
    set_turtle(vent, -140, -200)
    make_rectangle(vent, 50, 100)
    vent.end_fill()

    set_turtle(vent, -140, -150)     # add detail to window
    make_rectangle(vent, 50, 50)

    set_turtle(vent, -140, -200)    # add detail to window
    make_rectangle(vent, 25, 100)

    hank = make_turtle('white')     # add doorknob to door
    hank.shape('circle')
    set_turtle(hank, 40, -170)
    hank.stamp()
    wn.exitonclick()                # end on click


main()
