#################################################################################
# Header Block
#################################################################################

import turtle
import random

def draw_cloud_circle(turtle,size):
    """
        This is a background function and will not be called in main(). Its purpose is to randomize the size of the circle
        and at the same time prevent me from typing all that a bunch of times.

    :param turtle: Is the turtle that is going to be used
    :param size: the size eof the circle
    :return: None
    """
    turtle.speed(11)
    turtle.hideturtle()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(size,360,100)
    turtle.end_fill()

def draw_cloud(turtle,x,y):
    """
        This function creates a cloud that is somewhat randomized in its shape so it looks less artificial and more fun.

    :param turtle: Is the turtle that is going to be used
    :param x: the x coordinate of the right corner of the cloud
    :param y: the y coordinate of the right corner of the cloud
    :return: None
    """
    cloud_spread = random.Random()

    turtle.speed(11)
    # I draw the cloud by drawing a bunch of white circles randomly within a certain range.

    for i in range (cloud_spread.randrange(4,6,1)): # the number of times the circle is drawn to determine/
                                                    #\the size of the single cloud
        turtle.penup()
        turtle.goto((x+cloud_spread.randrange(10,30,10)),y) #the distance between each circle
        turtle.pendown()
        draw_cloud_circle(turtle,cloud_spread.randrange(15,40,6)) #the size of each circles
        x = x + cloud_spread.randrange(10,30,5)
        y = y + cloud_spread.randrange(-15,15,5)

def ran_cloud(turtle):
    """
        Randomizes the position of the clouds
    :param turtle: Is the turtle that is going to be used
    :return: None
    """
    cloud_pos=random.Random()
    draw_cloud(turtle, cloud_pos.randrange(-340,340,100),cloud_pos.randrange(100,250,50))

def draw_ground(ground,curve,hor_line):
    """
        Draws ground in the color of grass.

    :param ground: Is the turtle that is going to be used.
    :param curve: The curvature of the horizon line, the more it is the less curved it is.
    :param hor_line: The vertical locus of the horizon.
    :return:
    """
    ground.begin_fill()
    ground.speed(11)
    ground.hideturtle()
    ground.color(124,252,0)
    ground.penup()
    ground.goto(-350,hor_line)
    ground.lt(370)
    ground.pendown()
    ground.pensize(10)
    ground.circle(-(curve),360,curve//10)
    ground.end_fill()

def draw_arc(tort):

    tort.penup()
    tort.pendown()
    tort.pensize(25)
    tort.color(255, 0 , 0)
    tort.lt(90)
    tort.penup()
    tort.goto(-350,-100)
    tort.pendown()
    start_turn = 10
    angle = 5900
    fd = 30
    exp =fd/200
    for i in range (10):
        tort.rt(start_turn+angle)
        tort.fd(fd)
        angle=angle**exp

def main():
##########################################################
    cloud=turtle.Turtle()
    sc=turtle.Screen()
    ground=turtle.Turtle()
    tort=turtle.Turtle()
    sc.colormode(255)
###########################################################

    sc.bgcolor(135,206,250)
    cloud.hideturtle()
    draw_ground(ground,2000,-100)
    for i in range(9):
        ran_cloud(cloud)
###########################################################
    tort.penup()
    tort.pendown()
    tort.pensize(25)
    tort.color(255, 0 , 0)
    tort.lt(90)
    tort.penup()
    tort.goto(-350,-100)
    tort.pendown()
    start_turn = 10
    angle = 30
    fd = 100
    exp =fd/150


    for i in range (40):
        tort.rt(start_turn+angle)
        tort.fd(fd)
        angle=angle**exp




    sc.exitonclick()

main()
