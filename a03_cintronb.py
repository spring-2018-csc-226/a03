#################################################################################
# Authors: Berucha Citron
# Usernames: citronb
# Assignment: A3:A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#################################################################################

import turtle


def draw_square(turt, size):
    """
    Draws the body of the house
    :param turt: a turtle object
    :param size: size of sides
    :return: None
    """
    for i in range(4):
        turt.forward(size)
        turt.left(90)



def draw_roof(turt, size):
    """
    Draws the roof of the house
    :param turt: a turtle object
    :param size: size of sides
    :return: None
    """
    for i in range(3):
        turt.forward(size)
        turt.left(120)


def draw_head(turt):
    """
    Draws the head of the person body
    :param turt: a turtle object
    :return: None
    """
    for i in range(360):
        turt.forward(1)
        turt.left(-1)


def draw_sun(turt):
    """
    Draws the sun in the sky
    :param turt: a turtle object
    :return: None
    """
    turt.penup()
    turt.setpos(175, 175)
    turt.pensize(4)
    turt.pendown()
    for i in range(15):
        turt.forward(100)
        turt.backward(100)
        turt.right(360 / 15)
    turt.setpos(175, 115)
    turt.begin_fill()
    turt.circle(60)
    turt.end_fill()


def main():
    """
    Draws a house with a person in front of it and a sun in the sky
    :return:None
    """
##########################################################################
    # creates the window
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    wn.title("Mi Casa, Su Casa")

    # establishes the attributes of the house
    house = turtle.Turtle()
    house.speed(10)
    house.penup()
    house.setpos(-250.0, -250.0)
    house.pendown()
    house.color(0, .5, 0)

    # estblishes the attributes of the person
    person = turtle.Turtle()
    person.speed(10)
    person.penup()
    person.setpos(0.0, 0.0)
    person.pendown()
    person.color(0.824, 0.412, 0.118)

    # establishes the attributes of the sun
    sun = turtle.Turtle()
    sun.speed(10)
    sun.penup()
    sun.setpos(0.0, 0.0)
    sun.pendown()
    sun.color(1, 0.8431, 0)
##########################################################################

    # draws the body of the house and fills it with color
    house.begin_fill()
    draw_square(house, 250)
    house.end_fill()

    # draws the roof of the house and fills it with color
    house.setpos(-250.0, 0.0)
    house.color("brown")
    house.begin_fill()
    draw_roof(house, 250)
    house.end_fill()

    # draws the head of the body and fills it with color
    person.setpos(-125.0, -75.0)
    person.begin_fill()
    person.circle(50)
    person.end_fill()

    # draws the arms and the torso of the body
    person.color(0.62, 0.13, 0.94)
    person.pensize(30)
    person.right(135)
    person.forward(75)
    person.backward(75)
    person.left(90)
    person.forward(75)
    person.backward(75)
    person.right(45)
    person.forward(75)

    # draws the legs
    person.color(0.1, 0.3, 0.5)
    person.right(45)
    person.forward(75)
    person.backward(75)
    person.left(90)
    person.forward(75)

    # calls the function that draws the sun
    draw_sun(sun)

    wn.exitonclick()

main()
