######################################################################
#Robert Hogsed
#hogsedr
#a03 gitty robotic turtle
#draw complex shapes
######################################################


import turtle


def make_rain(shape, angle, angle2, angle3, angle4):
    """
    makes the purple rain. uses lines to create the illusion of random rain fall
    """
    shape.speed(0)
    shape.penup()
    shape.setpos(angle, -400)
    shape.color('#FF32E0')
    shape.pendown()
    shape.left(90)
    for side in range(9):
        shape.pendown()
        shape.forward(800)
        shape.penup()
        angle = angle + 30
        shape.setpos(angle, -400)
        shape.left(.5)

    for side in range(9):
        shape.pendown()
        shape.forward(800)
        shape.penup()
        angle2 = angle2 + 30
        shape.setpos(angle2, -400)
        shape.right(.5)
    for side in range(9):
        shape.pendown()
        shape.forward(800)
        shape.penup()
        angle3 = angle3 + -30
        shape.setpos(angle3, -400)
        shape.right(.5)

    for side in range(9):
        shape.pendown()
        shape.forward(800)
        shape.penup()
        angle4 = angle4 + -30
        shape.setpos(angle4, -400)
        shape.left(.5)


def make_umbrella(shape, x, y, pen):
    """
    Makes umbrella over the doorway
    """
    shape.pensize(pen)
    shape.penup()
    shape.setpos(-236, 236)
    shape.pendown()
    shape.color('#000000')
    for side in range(10):
        shape.forward(474)
        shape.right(90)
        shape.forward(25)
        shape.right(90)
        shape.forward(474)
        shape.left(90)
        shape.forward(25)
        shape.left(90)


def draw_door(shape):
    """
    makes door for the building
    """
    shape.penup()
    shape.speed(0)
    shape.pensize(1)
    shape.setpos(100, -400)
    shape.pendown()
    shape.color('#966F33')
    shape.begin_fill()
    shape.forward(500)
    shape.left(90)
    shape.forward(200)
    shape.left(90)
    shape.forward(500)
    shape.left(200)
    shape.end_fill()

    shape.color('black')
    shape.penup()
    shape.setpos(85, -85)
    shape.pendown()
    shape.pensize(10)
    for side in range(4):
        shape.forward(2)
        shape.left(45)
    shape.penup()


def window(shape):
    """
    makes window into building
    """
    shape.setpos(-150, 210)
    shape.pendown()
    shape.begin_fill()
    shape.left(70)
    shape.forward(300)
    shape.right(90)
    shape.forward(100)
    shape.right(90)
    shape.forward(300)
    shape.right(90)
    shape.forward(100)
    shape.end_fill()
    shape.penup()
    """
    creates light through window
    """

    shape.begin_fill()
    shape.setpos(-25, 210)
    shape.color('yellow')
    shape.pendown()
    shape.right(200)
    shape.forward(105)
    shape.left(200)
    shape.right(90)
    shape.forward(105)
    shape.right(90)
    shape.left(200)
    shape.forward(105)
    shape.left(70)
    shape.forward(30)
    shape.end_fill()


def main():

    wn = turtle.Screen()
    wn.bgcolor('grey')
    pen =25
    shape = turtle.Turtle()
    shape.hideturtle()
    angle = -450
    angle2 = -460
    angle3 = 460
    angle4 = 450
    make_rain(shape, angle, angle2, angle3, angle4)
    make_umbrella(shape, 31, 46, pen)
    draw_door(shape)
    window(shape)
    wn.exitonclick()


main()
