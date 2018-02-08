#################################################################################
# Jose Cortes
# username: Cortesj

# Assignment: A03
#################################################################################

import turtle


def draw_grass():
    """
    Docstring for draw_grass
    :return:
    """
    grass = turtle.Turtle()
    grass.speed(0)
    grass.penup()
    grass.pencolor("lightgreen")
    grass.goto(-250, -250)
    grass.pendown()
    grass.fillcolor("#65DE31")
    grass.begin_fill()
    for i in range(2):
        grass.forward(500)
        grass.left(90)
        grass.forward(40)
        grass.left(90)
    grass.end_fill()

def drawcircle(a, b, r, color):
    """
    Docstring for function_2
    :return:
    """
    circle = turtle.Turtle()
    circle.penup()
    circle.pencolor(color)
    circle.fillcolor(color)
    #TEMP SPEED
    circle.speed(0)

    circle.goto(a, b)
    circle.begin_fill()
    circle.circle(r)
    circle.end_fill()
    circle.penup()
    circle.goto(a, b + 5)


def draw_cloud():
    """
    Docstring for draw_cloud
    :return:
    """
    drawcircle(0, 150, 25, "White")
    drawcircle(20, 170, 25, "White")
    drawcircle(45, 165, 25, "White")
    drawcircle(50, 150, 25, "White")
    drawcircle(70, 170, 25, "White")
    drawcircle(95, 165, 25, "White")


def draw_square(a, b, size, color):
    square = turtle.Turtle()
    square.penup()
    #TEMP SPEED
    square.speed(0)
    square.goto(a, b)
    square.pencolor(color)
    square.fillcolor(color)
    square.pendown()
    square.begin_fill()
    for i in range(4):
        square.forward(size)
        square.left(90)
    square.end_fill()
    square.penup()
    square.goto((a + 10), (b + 10))


def draw_rectangle(a, b, l, w, color):
    rectangle = turtle.Turtle()
    rectangle.penup()
    #TEMP SPEED
    rectangle.speed(0)
    rectangle.goto(a, b)
    rectangle.pencolor(color)
    rectangle.fillcolor(color)
    rectangle.pendown()
    rectangle.begin_fill()
    for i in range(2):
        rectangle.forward(l)
        rectangle.left(90)
        rectangle.forward(w)
        rectangle.left(90)
    rectangle.end_fill()
    rectangle.penup()
    rectangle.goto((a + 10), (b + 10))

def draw_hill():
    hill = turtle.Turtle()
    hill.penup()
    #TEMP SPEED
    hill.speed(0)
    hill.goto(250, 100)
    hill.pencolor("green")
    hill.fillcolor("green")
    hill.pendown()
    hill.begin_fill()
    #Hill Drawing Motions
    hill.begin_fill()
    hill.goto(150, -210)
    hill.forward(100)
    hill.left(90)
    hill.forward(310)
    hill.end_fill()


def main():
    """
    Docstring for Main
    :return:
    """
    wn = turtle.Screen()
    wn.setup(500, 500)
    wn.bgcolor("#00F5FF")
    wn.colormode((0, 0, 0))

    draw_grass()
    drawcircle(-200, 150, 100, "#F3F70A")
    #Draws the sun ^
    draw_cloud()
    #Draws house
    draw_square(-200, -210, 160, "red")
    draw_square(-40, -210, 100, "red")
    #Door Drawing
    draw_rectangle(-175, -210, 50, 100, "brown")
    #Window Frame
    draw_rectangle(-20, -190, 50, 60, "gray")
    draw_hill()
    wn.exitonclick()


main()
