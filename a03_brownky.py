#######################################################################################################################
#A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#Making use of turtles' more complex functionality
#
#Kyree J. Brown - Section A
#Looking to draw a face with an afro
#######################################################################################################################
#Imports turtle library
import turtle

##############################################################################################
#Creating functions for the different turtles
def draw_spiral(object, x, k):                                               ##I TRIED SOMETHING NEW
    object.penup()                                                           ##BUT FAILED... I lied, kinda
    object.setpos(-250,-250)
    object.pendown()
    object.color("orange")
    object.pensize(5)
    object.forward(100)
    for i in range(k):
        for f in range(2):
            object.forward(x)
            object.left(90)
        for e in range(2):
            object.forward(x - 25)
            object.left(90)
        x = x - 25
    return x


def draw_circle(object,color,sz,x,y):
    """
    Used to create a variety of circles to compose the face

    :param object: which turtle is to complete the task
    :param color: what color will the circle be?
    :param sz: what is the size of the circle?
    :param x: what is the beginning x coordinate?
    :param y: what is thr beginning y coordinate?
    :return: none
    """
    object.penup()
    object.setpos(x,y)
    object.pendown()
    object.begin_fill()
    object.circle(sz)
    object.fillcolor(color)
    object.end_fill()

def draw_mouth(object,color,sz,x,y):
    """
    Used to draw mouth for the face

    :param object: which turtle is to complete the task
    :param color: what color will the mouth be?
    :param sz: what is the size of the circle?
    :param x: what is the beginning x coordinate?
    :param y: what is thr beginning y coordinate?
    :return: none
    """
    object.penup()
    object.setpos(x,y)
    object.pendown()
    object.begin_fill()
    object.left(270)
    object.circle(sz,180)
    object.fillcolor(color)
    object.end_fill()

def draw_tooth(object,color,x,y):
    """
    Used to draw a single tooth for the face

    :param object: which turtle is to complete the task
    :param color: what color will the tooth be?
    :param x: :param object: which turtle is to complete the task
    :param color: what color will the circle be?
    :param sz: what is the size of the circle?
    :param x: what is the beginning x coordinate?
    :param y: what is thr beginning y coordinate?
    :return: none
    """

    object.pencolor(color)
    object.penup()
    object.setpos(x,y)
    object.pendown()
    object.fillcolor("white")
    object.begin_fill()
    for i in range (2):
        object.right(90)
        object.forward(50)
        object.right(90)
        object.forward(100)
    object.end_fill()

################################################################################################
#Calling the functions
def main():
    hello = turtle.Screen()
    hello.bgcolor("teal")
    hello.colormode(255)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pensize(2)
    pen.pencolor("black")

    draw_spiral(pen,475,10)
    pen.color("black")
    draw_circle(pen,"brown",200,0,-250)
    draw_circle(pen,"white",25,50,0)
    draw_circle(pen,"white",25,-50,0)
    draw_mouth(pen,"red",150, -150,-35)
    draw_tooth(pen,"black",-72.5,-35)
    draw_tooth(pen,"black",27.5,-35)

    hello.exitonclick()
################################################################################################
#Running the Main program
main()

