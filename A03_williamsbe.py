##############################################################################################################
# Author: Bethanie Williams   TODO: Change this to your names
# Username: williamsbe
# williamsbe
#             TODO: Change this to your usernames
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose: Continue practicing creating and using functions and More practice on using the turtle library
##############################################################################################################



import turtle

# Function that draws the squared border around the house

def draw_square(t,size):
    """
    :param t: A turtle object
    :param size: The size of the square
    :return: none
    """

    t.penup()
    t.setpos(100,-50)
    t.right(90)
    t.pendown()
    t.color("yellow")


    # Algorithm for drawing the square
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Algorithm for making triangle
# Function that draws the triangle border around the house

def draw_triangle(h,size):

    """
    :param h: a turtle object
    :param size: The size of the triangle
    :return: none
    """
    h.penup()
    h.setpos(99,-45)
    h.pendown()
    h.begin_fill()
    h.color("red")
    h.pensize(10)
    h.left(45)
    h.fd(70)
    h.left(-90)
    h.fd(70)
    h.left(-135)
    h.forward(100)
    h.end_fill()

# Function that draws the door of the house

def draw_door(d,size):

    """
    :param d: a turtle object
    :param size: The size of the door
    :return: none
    """

    d.penup()
    d.setpos(135,-153)
    d.pensize(3)
    d.pendown()
    d.left(90)
    # Algorithm for making the door
    for i in range (2):
        d.forward(50)
        d.right(90)
        d.forward(25)
        d.right(90)
    d.penup()
    d.setpos(140,-130)
    d.pendown()
    d.circle(.5)

# Function that draws the window of the house

def draw_window(w,size):

    """
    :param w: a turtle object
    :param size: The size of the window
    :return:none
    """

    w.penup()
    w.setpos(180,-85)
    w.pensize(3)
    w.pendown()
    w.begin_fill()

#algorithim for outside shape of the window
    for i in range(4):
        w.left(90)
        w.forward(25)
 #unkown color implented
    w.color("#9ACD32")
    w.end_fill()
    w.color("black")
    w.left(90)
    w.penup()
    w.setpos(180,-80)
    w.pendown()
    w.forward(7)
    w.left(90)
    w.forward(25)
    w.right(90)
    w.forward(12.5)
    w.right(90)
    w.forward(12.5)
    w.right(90)
    w.forward(26)
    w.penup()
    w.setpos(500,500)

def main():
    """
    Main function that invokes all other previously defined functions.
    :return: none
    """
    wn = turtle.Screen()
    wn.bgpic("background.png")
    t = turtle.Turtle()
    t.speed(20) # makes bob go faster
    t.pensize(10)
    draw_square(t,100)

    h = turtle.Turtle()
    draw_triangle(h,100)
    h.speed(15)

    d = turtle.Turtle()
    draw_door(d,100)
    d.speed(15)

    w= turtle.Turtle()
    draw_window(w,100)
    wn.exitonclick()

main()

