######################################################################
# Author: Annette Dangerfield             TODO: Change this to your name, if modifying
# Username: dangerfielda                  TODO: Change this to your username, if modifying
#
# Assignment: A03
#
######################################################################

import turtle


def draw_DeathStarFill(shape):          #draws the main bulk of the Death Star
    shape.penup()
    shape.setpos(200, 230)
    shape.pendown()
    shape.color("grey")
    shape.begin_fill()
    for side in range(25):
        shape.right(15)
        shape.forward(25)
    shape.end_fill()

def draw_DeathStarOutline(shape):       #draws an outline around the Death Star
    shape.penup()
    shape.setpos(270, 180)
    shape.pendown()
    shape.pensize(5)
    shape.color("black")
    for side in range(25):
        shape.right(15)
        shape.forward(25)

def draw_DeathStarLaser(shape):         #draws the shape were the laser comes out
    shape.penup()
    shape.setpos(180, 200)
    shape.pendown()
    shape.color("black")
    shape.begin_fill()
    for side in range (20):
        shape.right(20)
        shape.forward(10)
    shape.end_fill()

def draw_DeathStarBeam(shape):          #draws the multiple beams of the laser
    shape.penup()
    shape.setpos(179,199)
    shape.color("lime green")
    shape.pendown()
    shape.right(55)
    shape.forward(30)
    shape.penup()
    shape.setpos(195,180)
    shape.pendown()
    shape.right(40)
    shape.forward(30)
    shape.penup()
    shape.setpos(183,152)
    shape.pendown()
    shape.right(58)
    shape.forward(30)
    shape.penup()
    shape.setpos(147,157)
    shape.pendown()
    shape.right(90)
    shape.forward(20)
    shape.penup()
    shape.setpos(145,190)
    shape.pendown()
    shape.right(100)
    shape.forward(20)

    shape.penup()
    shape.setpos(160,170)
    shape.pendown()
    shape.right(90)
    shape.forward(300)
    shape.penup()


# def draw_DeathStarCurve(shape):         #would have drawn the bisection of the Death Star
#     shape.penup()                       #in the interest of time and feasibility I had to leave it like this
#     shape.setpos(100,125)               #it would reshuffle all the other components each time I'd test it
#     shape.color("dark grey")            #not sure what I was doing wrong, but I might go back and fix it later
#     shape.left(90)
#     shape.pendown()
#     for side in range (7):
#         shape.right(10)
#         shape.forward(25)

def draw_explosion(wn, shape):          #adds an explosion
    wn.register_shape("fire1.gif")
    shape.setpos(-70,-10)
    shape.shape("fire1.gif")
    shape.stamp()

def main():
    wn = turtle.Screen()
    wn.bgpic("fullsizeoutput_54.gif")
    wn.title("In a galaxy much, much closer to home...")

    shape = turtle.Turtle()
    shape.hideturtle()

    draw_DeathStarFill(shape)

    # draw_DeathStarCurve(shape)

    draw_DeathStarLaser(shape)

    draw_DeathStarOutline(shape)

    draw_DeathStarBeam(shape)

    draw_explosion(wn, shape)

    wn.exitonclick()
main()
