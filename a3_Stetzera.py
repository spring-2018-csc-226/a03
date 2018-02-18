######################################################################
# Author: Heidi Stetzer
# Username: stetzera
# Assignment: A03
# Purpose: To do functions'n'stuff. And draw a field of flowers. Sort of.
######################################################################


import turtle


def make_flower(shape, x, y, c1, c2, l, s):
    """
    Makes a simple flower and stem.
    Change the l (long) and s (short) to change the petal shape and size.
    Change c1 and c2 to adjust the colors of the outside and inside petals.
    """
    shape.penup()
    shape.speed(20)
    shape.setpos(x, y)
    shape.color(c2, c1)
    shape.begin_fill()
    shape.pendown()
    for side in range(6):
        shape.left(60)
        shape.forward(s)   # s stands for short side
        shape.right(60)
        shape.forward(l)    # l stands for long side
        shape.right(60)
        shape.forward(s)
        shape.right(60)
        shape.forward(s)
        shape.right(60)
        shape.forward(l)
        shape.right(60)
        shape.forward(s)
        shape.right(60)
    shape.end_fill()
    shape.pendown()

    shape.color("green")
    shape.right(90)
    shape.penup()
    shape.forward(10)
    shape.pendown()
    shape.forward(110)
    shape.left(90)



    # ...


def make_grass_field(shape, x, y, z):
    """
    Makes a block of flat color for grass. Use multiple of slightly varying shades to make a makeshift gradient.
    """
    shape.penup()
    shape.speed(10)
    shape.setpos(x,y)
    shape.color(z)
    shape.begin_fill()
    for side in range(2):
        shape.forward(800)
        shape.right(90)
        shape.forward(800)
        shape.right(90)
    shape.end_fill()

    # ...


def main():
    """
    Docstring for main
    """
    wn= turtle.Screen()            # Makes a new turtle screen
    wn.bgcolor("light blue")       #Sets background color to light blue
    shape = turtle.Turtle()
    shape.hideturtle()
    shape.pensize(5)
    shape.speed(30)
    shape.shape("circle")

    make_grass_field(shape, -400, -100, '#1e7528')
    make_grass_field(shape, -400, -125, '#21822c')             #Makes the gradient(ish) background
    make_grass_field(shape, -400, -150, '#279934')
    make_grass_field(shape, -400, -175, '#2ead3d')
    make_grass_field(shape, -400, -200, '#34c145')

    make_flower(shape, 60, 40,'#c677a5', '#a04e74', 10, 5)       #Makes all the flowers in the background.
    make_flower(shape, -50, 20, '#c677a5', '#a04e74', 10, 5)
    make_flower(shape, 150, 25, '#c677a5', '#a04e74', 10, 5)
    make_flower(shape, -70, 10, '#c677a5', '#a04e74', 10, 5)
    make_flower(shape, -200, 40,'#c677a5', '#a04e74', 10, 5)
    make_flower(shape, -150, 20, '#c677a5', '#a04e74', 10, 5)
    make_flower(shape, 200, 25, '#c677a5', '#a04e74', 10, 5)
    make_flower(shape, 170, 10, '#c677a5', '#a04e74', 10, 5)

    make_flower(shape, 40, -30,'#a04e74', '#7a2e4a', 50, 25)
    make_flower(shape, -150, -60, '#a04e74', '#7a2e4a',  50, 25)       #Makes all the flowers in the midground.
    make_flower(shape, 200, -55, '#a04e74', '#7a2e4a',  50, 25)
    make_flower(shape, -90, -50, '#a04e74', '#7a2e4a',  50, 25)
    make_flower(shape, -250, -20, '#a04e74', '#7a2e4a',  50, 25)
    make_flower(shape, 0, -95, '#42ebf4', '#41c7f4',  60, 30)      #Makes the special blue flower

    make_flower(shape, -250, -100,'#7a2e4a', '#541529', 75, 50)         #Makes all the flowers in the foreground.
    make_flower(shape, -200, -200,'#7a2e4a', '#541529', 75, 50)
    make_flower(shape, -100, -300,'#7a2e4a', '#541529', 75, 50)
    make_flower(shape, 50, -275,'#7a2e4a', '#541529', 75, 50)
    make_flower(shape, 200, -220,'#7a2e4a', '#541529', 75, 50)
    make_flower(shape, 300, -200,'#7a2e4a', '#541529', 75, 50)

    wn.exitonclick()

main()



