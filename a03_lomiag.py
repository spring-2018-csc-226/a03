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

def draw_arc(tort,x_start,y_start,red,green,blue,r,ext,speed):
    """
        Draws a circular arc.
    :param tort: Is the turtle that is going to be used.
    :param x_start: The Starting X position of the arc
    :param y_start: The Starting Y position of the arc
    :param red: The amount of red in the color scheme
    :param green: The amount of green in the color scheme
    :param blue: The amount of blue in the color scheme
    :param r: Radius of the arc
    :param ext: The "roundness" of the arc
    :param speed: The speed of drawing
    :return: None
    """
    tort.hideturtle()
    tort.speed(speed)
    if r <0:
        tort.pensize(-r/8.4)
    else:
        tort.pensize(r/8.4)
    tort.color(red, green, blue)
    tort.lt(90)
    tort.penup()
    if r < 0:
        tort.goto(x_start,y_start)
    else:
        tort.goto(-x_start,-y_start)
    tort.pendown()

    tort.circle(r,180,ext)

def draw_rainbow(torty,r,speed):
    """
        Draws a rainbow that is centered on the screen, and adjusts to the size on itself.
    :param torty: Is the turtle that is going to be used.
    :param r: the radius of the rainbow
    :param speed: drawing speed
    :return: None
    """
    if r < 0:
        pens = r/8.4 + 4
    else:
        pens = -r/8.4 - 4

    draw_arc(torty,r,-65,255,0,0,r,100,speed)
    torty.lt(90)
    draw_arc(torty,r-pens,-65,255,127,0,r-pens,100,speed)
    torty.lt(90)
    draw_arc(torty,r-pens-pens-1,-65,255,255,0,r-pens-pens-1,100,speed)
    torty.lt(90)
    draw_arc(torty,r-pens-pens-pens/1.2,-65,0, 255, 0,r-pens-pens-pens/1.2,100,speed)
    torty.lt(90)
    draw_arc(torty,r-pens-pens-2*(pens/1.22),-65,0, 0, 255,r-pens-pens-2*(pens/1.22),100,speed)
    torty.lt(90)
    draw_arc(torty,r-pens-pens-3*(pens/1.3),-65,75, 0, 130,r-pens-pens-3*(pens/1.3),100,speed)
    torty.lt(90)
    draw_arc(torty,r-pens-pens-4*(pens/1.5),-65,148, 0, 211,r-pens-pens-4*(pens/1.5),100,speed)


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
    for i in range(10):
        ran_cloud(cloud)
    draw_rainbow(tort,-250,11)



    sc.exitonclick()

main()
