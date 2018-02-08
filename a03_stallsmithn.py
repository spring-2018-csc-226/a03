#################################################################################
# Author: Natasha Stallsmith
# Username: stallsmithn
#
# Assignment: A3: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draw the constellation Orion.
#################################################################################
import turtle


def right_head(turt):
    """
    Draw right side of Orion's head.
    :param turt: A turtle object.
    :return: None.
    """
    turt.penup()
    turt.goto(28, 235)          # top of head
    turt.pendown()
    turt.right(60)
    turt.forward(110)
    # print(turt.pos())             # starting point of right arm


def right_arm(turt):
    """
    Draw's Orion's right arm.
    :param turt: A turtle object.
    :return: None.
    """
    turt.left(30)
    turt.forward(228)
    # print(turt.pos())                 # bow midpoint


def bow_up(turt):
    """
    Draws top half of bow.
    :param turt: A turtle object.
    :return: None.
    """
    turt.left(120)
    turt.forward(70)
    turt.left(35)
    turt.forward(70)


def bow_down(turt):
    """
    Draws lower half of bow.
    :param turt: A turtle object.
    :return: None.
    """
    turt.penup()
    turt.goto(280.45, 25.74)                # bow midpoint
    turt.pendown()
    turt.right(225)
    turt.forward(50)
    turt.right(20)
    turt.forward(45)
    turt.right(17)
    turt.forward(35)


def body(turt):
    """
    Draws the main part of Orion's body.
    :param turt: A turtle object.
    :return: None.
    """
    turt.penup()
    turt.goto(83, 139.74)               # starting point of right arm
    turt.pendown()
    turt.left(25)
    turt.forward(170)
    # print(turt.pos())                 # right side of belt
    turt.left(45)
    turt.forward(230)
    turt.right(112)
    turt.forward(210)
    turt.right(110)
    turt.forward(190)
    # print(turt.pos())                 # left side of belt
    turt.left(34)
    turt.forward(240)
    # print(turt.pos())                 # starting point of left arm
    turt.goto(28, 235)                  # top of head


def left_arm(turt):
    """
    Draws Orion's left arm.
    :param turt: A turtle object.
    :return: None.
    """
    turt.penup()
    turt.goto(-101.04, 178.21)          # starting point of left arm
    turt.pendown()
    turt.left(19)
    turt.forward(68)
    turt.right(4)
    turt.forward(125)
    turt.right(92)
    turt.forward(48)
    turt.goto(-101.04, 178.21)          # starting point of left arm


def belt(turt):
    """
    Draws decorative belt.
    :param turt: A turtle object.
    :return: None.
    """
    turt.penup()
    turt.goto(-38.93, -53.61)           # left side of belt
    turt.pendown()
    turt.color("#00f2f2")               # light blue
    turt.pensize(2)
    turt.seth(60)
    turt.forward(20)
    # print(turt.pos())
    turt.right(70)
    turt.forward(20)
    # print(turt.pos())                # belt midpoint
    turt.left(70)
    turt.forward(25)
    # print(turt.pos())
    turt.goto(19.32, -17.88)            # right side of belt
    turt.right(160)
    turt.forward(18)
    # print(turt.pos())
    turt.goto(3.27, -18.11)
    turt.goto(-28.93, -36.29)
    turt.penup()
    turt.goto(16.19, -35.61)
    turt.pendown()
    turt.goto(-9.23, -39.76)            # belt midpoint
    turt.right(2)
    turt.forward(18)
    # print(turt.pos())
    turt.goto(16.19, -35.61)
    turt.goto(-14.79, -56.88)
    turt.goto(-28.93, -36.29)
    turt.goto(-14.79, -56.88)
    turt.goto(-38.93, -53.61)           # left side of belt


def main():
    orion = turtle.Turtle()
    wn = turtle.Screen()
    wn.screensize(500, 800)
    wn.bgpic("orion.gif")
    orion.speed(5)
    orion.hideturtle()
    orion.color("#4c0068")
    orion.pensize(4)

    right_head(orion)
    right_arm(orion)
    bow_up(orion)
    bow_down(orion)
    body(orion)
    left_arm(orion)
    belt(orion)

    wn.exitonclick()


main()
