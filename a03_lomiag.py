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
        draw_cloud_circle(turtle,cloud_spread.randrange(20,40,10)) #the size of each circles
        x = x + cloud_spread.randrange(10,30,5)
        y = y + cloud_spread.randrange(-15,15,5)

def ran_cloud(turtle):
    """
        Randomizes the position of the clouds
    :param turtle: Is the turtle that is going to be used
    :return: None
    """
    cloud_pos=random.Random()
    draw_cloud(turtle, cloud_pos.randrange(-300,300,100),cloud_pos.randrange(100,250,50))

def main():

    rainbow=turtle.Turtle()
    sc=turtle.Screen()
    sc.bgcolor("Blue")
    for i in range(9):
        ran_cloud(rainbow)
