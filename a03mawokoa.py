#################################################################################
# Authors: Azariah Mawoko
# Usernames: mawokoa
#
#
# Assignment: A3: Assignment: A3: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles

import turtle


def draw_trophy(silva):
        """
        draws top part of trophy
        :param silva:
        :return:None
        """

        Silva = turtle.Turtle()
        Silva.hideturtle()
        Silva.backward(50)
        Silva.color("sky blue")
        Silva.pensize(10)
        for side in range(8):
            Silva.forward(90)
            Silva.left(45)
        Silva.pensize(5)
        Silva.begin_fill()
        for i in range(8):
            Silva.color("gold")
            Silva.forward(90)
            Silva.left(60)
        Silva.end_fill()
        Silva.penup()
        Silva.goto(40.00,0.00)
        Silva.color('red')
        Silva.pendown()
        Silva.begin_fill()
        for x in range(3):
            Silva.forward(90)
            Silva.left(120)
        Silva.end_fill()


def draw_base(t):

        t = turtle.Turtle()
        t.pensize(10)
        t.penup()
        t.goto(-50.00,0.00)
        t.pendown()
        t.pencolor('Sky blue')
        for a in range(2):
            t.forward(100)
            t.right(90)
            t.forward(140)
            t.right(90)


def main():
    wn = turtle.Screen()
    wn.bgpic('soccer pitch.jpg')
    wn.bgcolor('Indigo')
    wn.title("The trophy!")
    t = turtle.Turtle()
    wn = turtle.Screen()
    silva = turtle.Turtle()
    silva.hideturtle()

    wn.exitonclick()


main()
