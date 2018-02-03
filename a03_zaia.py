######################################################################
# Author: Ahad Zai
# Username: zaia
#
# Assignment: A03
#
# Purpose: A program that draws something complex like a house, animal, person

######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

#This function is used to draw a barn
import turtle



def drawBarn(t):
    turtle.colormode(255)
    t.begin_fill()
    t.fillcolor(139,69,19)
    #Makes a square for the barn
    for i in range (4):
        t.forward(200)
        t.right(90)
    t.end_fill()
    t.penup()
    #positions turtle to make triangle above square
    t.forward(200)
    t.right(60)
    t.pendown()
    #Defines the triangles attributes
    t.pencolor("black")
    t.fillcolor("black")
    #starts making the triangle
    t.begin_fill()
    t.forward(140)
    t.right(70)
    t.forward(110)
    t.right(230)
    t.left(90)
    t.forward(210)
    t.end_fill()
    #Positions turtle to make a circular window
    t.penup()
    for i in range (2):
        t.left(90)
        t.forward(100)
    #Starts making the window
    t.pendown()
    t.fillcolor("lightblue")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    #Makes cross in the window
    t.left(90)
    t.forward(80)
    t.left(180)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.forward(80)
    #Positions turtle to make door
    t.penup()
    t.left(90)
    t.forward(145)
    t.left(90)
    t.forward(80)
    t.left(90)
    #Starts makkng the door
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    t.forward(60)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(60)
    t.end_fill()
    #positions turtle to make door knob
    t.penup()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    #starts making the door knob
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
















def main():
    #Creates the screen and sets image of farm as background image.
    canvas = turtle.Screen()
    canvas.setup(600,400)
    canvas.bgpic('bg.png')

#Makes a turtle that calls the function drawBarn to draw a barn
    turt1 = turtle.Turtle()
    #Defines the attributes of the turtle
    turtle.colormode(255)
    turt1.hideturtle()
    turt1.pensize(6)
    turt1.pencolor(139,69,19)
    # turt1.hideturtle()
    turt1.penup()
    #Positions the turtle to fit in the screen
    turt1.forward(-200)
    turt1.left(90)
    turt1.forward(-150)
    turt1.pendown()
    turt1 = drawBarn(turt1)
    canvas.mainloop()


main()
