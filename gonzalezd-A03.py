######################################################################
# Author: David Gonzalez
# Username: gonzalezd
#
# Assignment: A3: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To demonstrate different turtle methods.
######################################################################
# Acknowledgements:
# Fountain.gif- https://i5.walmartimages.com/asr/06ed5458-6b68-43ae-bb31-ce1f763d82b1_1.3c852cc410ed2cd74eb4c958521d531c.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF
# trump.gif- https://i.pinimg.com/564x/10/bf/c5/10bfc54257f17286269fcb92a2c699c9--donald-trump-donald-oconnor.jpg
# field.png- Me
#################################################################################

import turtle


def draw_house(t):
    """
Draws a 1:1 replica of my house.
    :param t: turtle object
    :return: none
    """
    # Draws the main Builiding of the house
    t.penup()
    t.setpos(50,-230)
    t.color("blue")
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    # Draws the Roof
    t.begin_fill()
    t.penup()
    t.setpos(44,-130)
    t.pendown()
    t.color("#B46400")
    t.begin_fill()
    t.forward(112)
    t.left(149.5)
    t.forward(65)
    t.left(59.5)
    t.forward(65)
    t.end_fill()
    # draws the door
    t.penup()
    t.setpos(100,-230)
    t.color("brown")
    t.left(150)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(10)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()
    # draws the Windows
    t.penup()
    t.setpos(65,-180)
    t.color("#00FFFF")
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.left(90)
    t.end_fill()
    t.penup()
    t.setpos(115,-180)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.left(90)
    t.end_fill()

def draw_sun(t):
    """
    Draws the sun in the top left corner
    :param t: A turtle object
    :return: none
    """
    t.penup()
    t.setpos(-300,205)
    t.color("#C8C800")
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
def fountain(wn,t):
    """
    Places a fountain in front of my house.
    :param wn: The turtle Screen
    :param t: Turtle Object
    :return: none
    """
    wn.register_shape("fountain.gif") # registers shape
    t.penup()
    t.setpos(10,-210)
    t.shape("fountain.gif") # makes turtle take shape of the one defined above
    t.stamp()
def trump(wn,t):
    """
    Places a Super Trump flying under the sun as he is rushing off to fight the infidels.
    :param wn: Turtle Screen.
    :param t: A turtle object
    :return: none
    """
    wn.register_shape("trump.gif") # registers shape
    t.penup()
    t.setpos(-300,220)
    t.shape("trump.gif") # makes turtle take the shape of the shape registered above.
    t.right(90)
    t.stamp()
def write_text(t, text):
    """
    writes text on the screen.

    :param t: a turtle object
    :return: None
    """
    t.penup()
    t.color("#000000")
    t.setpos(0,120)
    t.pendown()
    t.write(text,move=False,align='center',font=("Times New Roman",20,("bold","normal")))
    t.hideturtle()

def main():
    """
    Main function that organizes other functions into one.
    :return: none
    """
    wn = turtle.Screen() # Creates a turtle Screen
    wn.bgpic("field.png") # Sets the background to field.png
    alex = turtle.Turtle() # Creates alex, a turtle object.
    alex.speed(5) # Makes alex go fast AF.
    draw_house(alex) # Tells alex to build my house.
    draw_sun(alex) # Tells alex to create the sun
    fountain(wn,alex) # Has alex go to Home Depot and purchase a fountain, after which he installs it outside my house.
    trump(wn,alex) # alex takes the form of the almighty Super Trump and goes off to fight crime.
    alex = turtle.Turtle() # alex is reborn
    write_text(alex, "Damn it feels good to be a gangster!") # Writes text on the screen
    wn.exitonclick()
main()
