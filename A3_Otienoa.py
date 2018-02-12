#####################################################################################################
# Anne Otieno
# otienoa

# Assignment A3
# Purpose: Making Functions using the Turtle Library to draw objects
##############################################################################


import turtle


def draw_vase(turt):
    """
    Helps draw a flower vase that will sit on a table.
    :param turt: the turtle object from the turtle class instance
    :return: None
    """
    for i in range(2):
        turt.left(90)               # turns the turtle to the left by 90 degrees
        turt.forward(100)           # moves the turtle forward to the left
        turt.left(90)
        turt.forward(100)           # moves the turtle forward


def draw_flower(turt, length):
    """
    Draws the flower that will be inside the vase
    :param turt: turtle object
    :param length: turtle length
    :return: None
    """

    for i in range(50):
        turt.forward(length)          # moves turtle forward upwards
        turt.backward(length)         # moves the turtle back to the origin and then the loop
        turt.right(360/50)            # the turtle turn through 360/number of the objects


def draw_table(turt, height, width):
    """
    Draws a flower in which the vase will rest upon.
    :param turt: a turtle instance from the turtle Class
    :param height: the height of the window
    :param width: the width of the table
    :return: None
    """
    turt.left(90)                       # turns the turtle to the left by 90 degrees to face up
    turt.forward(width)                 # moves the turtle forward by a length width
    turt.right(90)
    turt.forward(height)                 # turn the turtle to face East by a length height
    turt.right(90)                       # turns the turtle to face down
    turt.forward(width)
    turt.right(90)


def draw_window(turt, side):
    """
    Draws a window comprising of four combines squares and of a two alternating colors
    :param turt: the turtle object from class Turtle
    :param side: the length of the side of the window
    :return: None
    """

    for i in range(1, 5):
        turt.pensize(0.1)
        if i % 2 == 0:
            turt.begin_fill()                       # fills in the first square and does two alternates
            turt.color(0.8, 0.8, 0.1)               # the color of the first and the third square on the window
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.end_fill()

        else:
            turt.begin_fill()                       # fills the second square yellow and alternated twice
            turt.color(0.2, 0.1, 0.5)
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.forward(side)
            turt.right(90)
            turt.end_fill()

# Scott adding a comment


def draw_chair(turt, high):
    """
    Draws a chair next to the table
    :param turt: a turtle object from the Turtle class
    :param high: how high the chair is
    :return: None
    """
    turt.left(90)
    turt.forward(high)
    turt.right(90)
    turt.forward(high)
    turt.left(90)
    turt.forward(high)
    turt.backward(high*2)


def main():
    """
    Draws a table with flower, vase, and window
    :return: None
    """
    wn = turtle.Screen()
    wn.bgcolor('light green')

    tamu = turtle.Turtle()                  # my first turtle instance from the Turtle class
    tamu.penup()                            # puts the pen up so that there is no drawing left
    tamu.hideturtle()
    tamu.goto(50, - 100)                    # sets the original position of the turtle
    tamu.pendown()                          # puts the pen down to start drawing
    tamu.color(0.75, 0.5, 0.3)              # the color of the vase
    tamu.begin_fill()                       # fills the vase with the above named color
    draw_vase(tamu)                         # Calls the function to draw a vase
    tamu.end_fill()

    toto = turtle.Turtle()                  # the second Turtle instance from the Turtle class
    toto.hideturtle()
    toto.setpos(0.00, 0.00)                 # the position of the turtle
    length = 70
    toto.pensize(2)                         # the size of the pen
    toto.pendown()
    toto.speed(0)
    toto.color(1, 0.5, 0.8)
    toto.left(90)
    toto.forward(length + 30)               # moves the turtle forward
    draw_flower(toto, length)               # calls the function to draw the flower

    kaka = turtle.Turtle()                  # the third turtle instance from Turtle Class
    kaka.hideturtle()
    kaka.color(0.1, 0.2, 0.3)
    kaka.penup()
    kaka.goto(-150, -200)                   # sets the position of the turtle based on the grid
    kaka.pendown()
    kaka.pensize(10)
    height = 300                            # the horizontal distance of the table
    width = 100                             # the vertical distance of the table
    draw_table(kaka, height, width)

    sisi = turtle.Turtle()                  # the fourth turtle instance
    sisi.hideturtle()
    sisi.hideturtle()                       # makes the turtle invisible while drawing
    side = 50
    sisi.pensize(0.1)
    sisi.penup()
    sisi.goto(-280, 230)
    sisi.pendown()
    draw_window(sisi, side)                 # calls the function to draw a window

    papa = turtle.Turtle()
    papa.hideturtle()                       # the fifth turtle instance
    papa.penup()
    papa.color(0.1, 0.2, 0.3)
    papa.goto(250, -200)
    papa.pendown()
    papa.pensize(10)
    high = 80
    draw_chair(papa, high)                  # calls the turtle to draw a chair

    wn.exitonclick()


main()
