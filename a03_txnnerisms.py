##############################################
# AUTHOR: MONTANA HITE
# USERNAME: TXNNERISMS
#
# ASSIGNMENT: A3: PSYCHADELIC TURTLES
#
#############################################

# I believe, as the programmer, it is important to say that, after looking
# at the finished product of my little doodle, that there is a reason that I
# am NOT an art major. I really hope I'm not being graded on my artistic ability.

import turtle


def house_body(builder):
    """
    Draws a square that acts as the "body"/structure of the house.

    :param builder:
    :return: None
    """

    builder.penup()
    builder.setx(-150)
    builder.sety(-175)
    builder.pendown()
    builder.color('#f2e4a2')
    builder.begin_fill()
    for i in range(4):
      builder.forward(250)
      builder.left(90)
    builder.end_fill()

def house_roof(builder):
    """
    Draws a triangle that acts as the "roof" of the house.

    :param builder:
    :return: None
    """
    builder.penup()
    builder.setx(-150)
    builder.sety(75)
    builder.left(45)
    builder.color('#FF0000')
    builder.begin_fill()
    builder.pendown()
    builder.forward(175)
    builder.right(90)
    builder.forward(180)
    builder.right(45)
    builder.end_fill()

def house_chimney(builder):
    """
    Draws a small, vertical rectangle that looks like a house's chimney.

    :param builder:
    :return: None
    """
    builder.color('#FF0000')
    builder.penup()
    builder.sety(74)
    builder.setx(55)
    builder.pendown()
    builder.left(180)

    builder.begin_fill()
    for i in range(2):
        builder.forward(90)
        builder.right(90)
        builder.forward(45)
        builder.right(90)
    builder.end_fill()

def window_design(builder):
    """
    Utilized in function 'house_decor', used primarily to clean up the code and to use the same "cross" design in both windows.


    :param builder:
    :return: None
    """

    builder.right(90)
    builder.forward(30)
    builder.left(90)
    builder.forward(60)
    builder.left(90)
    builder.forward(30)
    builder.left(90)
    builder.forward(30)
    builder.left(90)
    builder.forward(60)

def house_decor(builder):
    """
    Draws two cute windows and a door to decorate the house.

    :param builder:
    :return: None
    """
    builder.penup()
    builder.setx(20)
    builder.sety(0)
    builder.pendown()
    for i in range(4):                        # This begins the first window of the house.
        builder.forward(60)
        builder.right(90)
    window_design(builder)                    # This calls a function to draw the design of the window.
    builder.penup()
    builder.setx(-130)
    builder.sety(0)
    builder.left(90)
    builder.pendown()
    for i in range(4):                        # This begins the second window of the house.
        builder.forward(60)
        builder.right(90)
    window_design(builder)

    builder.penup()                           # This begins the door of the house.
    builder.setx(0)
    builder.sety(-175)
    builder.pendown()
    builder.color('#632001')
    builder.left(90)
    builder.begin_fill()
    for i in range(2):
        builder.forward(120)
        builder.left(90)
        builder.forward(60)
        builder.left(90)
    builder.end_fill()


def main():
    builder_turt = turtle.Turtle()              # creates a turtle named 'builder'
    wn = turtle.Screen()                        # sets up the window
    wn.bgcolor('#d3d3d3')                        # sets the screen color to grey - like a rainy day!

    house_body(builder_turt)
    house_roof(builder_turt)
    house_chimney(builder_turt)
    house_decor(builder_turt)
    wn.exitonclick()


main()
