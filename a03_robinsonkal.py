######################################################################
# Author: Kaleb Robinson
# Username: robinsonkal
#
# Assignment: A03 A Pair of Fully Functional....
######################################################################

import turtle

def house():#makes house building
    """Moves the building outline turtle and the building fill turtle into place"""
    turtle1=turtle.Turtle() #makes outline of house
    housefill=turtle.Turtle() #fills house
    turtle1.penup()
    turtle1.left(180)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.pendown()
    housefill.penup()
    housefill.left(180)
    housefill.forward(100)
    housefill.right(90)
    housefill.forward(100)
    housefill.left(90)
    housefill.pendown()


    for i in range(4):#makes building outline
        turtle1.forward(200)
        turtle1.right(90)
    for b in range(100):#fills building
        housefill.pencolor('red')
        housefill.forward(200)
        housefill.left(90)
        housefill.forward(1)
        housefill.left(90)
        housefill.forward(200)
        housefill.right(90)
        housefill.forward(1)
        housefill.right(90)
        housefill.speed(0)

        pass


def top():
    """Makes the roof, chimney, and smoke"""
    roof=turtle.Turtle()
    chimney=turtle.Turtle()
    smoke=turtle.Turtle()
    smoke2=turtle.Turtle()
    smoke3=turtle.Turtle()
    roof.shape('triangle')
    roof.shapesize(13)
    roof.color(0,0,.255)
    roof.penup()
    roof.left(90)
    roof.forward(100)
    roof.left(90)
    roof.forward(200)
    roof.right(90)
    roof.forward(30)
    roof.pendown()
    chimney.color('gray')
    chimney.shape('square')
    chimney.shapesize(2)
    chimney.penup()
    chimney.left(90)
    chimney.forward(100)
    chimney.left(90)
    chimney.forward(150)
    chimney.right(90)
    chimney.forward(50)
    chimney.pendown()
    smoke.shape('circle')
    smoke.shapesize(1)
    smoke.color('black')
    smoke.penup()
    smoke.left(180)
    smoke.forward(150)
    smoke.right(90)
    smoke.forward(180)
    smoke.pendown()
    smoke2.shape('circle')
    smoke2.shapesize(1.5)
    smoke2.color('black')
    smoke2.penup()
    smoke2.left(180)
    smoke2.forward(140)
    smoke2.right(90)
    smoke2.forward(190)
    smoke2.pendown()
    smoke3.shape('circle')
    smoke3.shapesize(2)
    smoke3.color('black')
    smoke3.penup()
    smoke3.left(180)
    smoke3.forward(130)
    smoke3.right(90)
    smoke3.forward(200)
    smoke3.pendown()
    pass


def door():
    """Makes the door and door knob"""

    door=turtle.Turtle()
    doorknob=turtle.Turtle()
    doorknob.shape('circle')
    doorknob.shapesize(.5)
    doorknob.color('yellow')
    door.penup()
    door.right(90)
    door.forward(100)
    door.right(90)
    door.forward(200)
    door.pendown()
    door.forward(20)
    door.right(90)
    door.forward(60)
    door.right(90)
    door.forward(40)
    door.right(90)
    door.forward(60)
    doorknob.penup()
    doorknob.right(90)
    doorknob.forward(100)
    doorknob.right(90)
    doorknob.forward(200)
    doorknob.right(90)
    doorknob.forward(30)
    doorknob.right(90)
    doorknob.forward(10)
    doorknob.pendown()
    pass


































def main():
    wn=turtle.Screen()
    wn.bgcolor('lightblue')
    house()
    door()
    top()
    wn.exitonclick()




main()
