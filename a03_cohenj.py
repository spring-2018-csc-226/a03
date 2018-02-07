#################################################################################
# Jason Cohen
# username: Cohenj
# A 03: Branching the whacky turtle assignment
#################################################################################

import turtle

def background_window(wn):
    """
    Creates a screen
    Sets the background image
    Gives a title
    Return: none

    """
    wn.bgpic("zoltar.gif")
    wn.bgcolor('#fc8d59')
    wn.title("Can't skate without its mate.")

    # ...


def exterior_blade(z, short_side):
    """
    z: a turtle object that, in this case, is used to draw and fill
    short_side: the diameter and rectangle shortest side.
    return: none
    """
    z.penup()               #    The shape is supposed to be a rollerblade. Be forgiving.
    z.pencolor('#de2d26')
    z.setpos(-200,-200)
    z.pendown()
    z.pensize(3)
    z.begin_fill()
    z.color('#999999')
    z.left(90)
    z.forward(short_side * 3)
    z.right(90)
    z.forward(short_side / 2)
    z.dot(50)
    z.right(90)
    z.forward(short_side * 2.5)
    z.left(90)
    z.forward(short_side * 4)
    z.right(90)
    z.forward(short_side / 2)
    z.dot(50)
    z.right(90)
    z.forward(short_side * 3)
    z.end_fill()
    z.ht()

def blade_wheel(q, wheel_rad):
    """
    q: a turtle object that, in this case, is used to draw and fill a series of 4 circles as wheels
    wheel_rad: radius of the wheel.
    return: none
    Again, if I were clever, I would make spokes using radial lines in each wheel. Not this time.
    """
    n = -25
    for i in range(4):
        q.penup()
        q.color('#e7e1ef')
        q.setpos(n,-225)
        q.pendown()
        q.circle(wheel_rad)
        n = n-50
        q.penup()
        q.ht()



def buckles(j):
    """
    j: a turtle object
    return: none
    This function draws three buckles using the setpos commands.
    If I were clever, I would do the diagonal lines better, but this is what I've managed.
    """
    x = -175
    y = -150
    for i in range(3):
        j.pu()              #iterates the drawing of "buckles." Let's just agree that they're buckles, ok?
        j.color('#e6550d')
        j.setheading(0)
        j.setpos(x,y + i * 25)
        j.pensize(2)
        j.pd()
        j.fd(-4)
        j.left(90)
        j.fd(-1)
        j.left(90)
        j.fd(4)
        j.right(90)
        j.fd(-1)
        j.right(90)
        j.fd(-4)
        j.left(90)
        j.fd(-1)
        j.left(90)
        j.fd(4)
        j.right(90)
        j.fd(-1)
    j.ht()


def wryturt(s):
    """"
    :param s: a turtle object
    :return:none
    This function writes. That's it.
    """

    s.showturtle()
    s.color("black")
    s.penup()
    s.setpos(25,110)
    s.pd()
    s.write("Zoltar Says 'This is a Rollerblade!' Believe Zoltar!",move=False,align='center',font=("Courier",12,("bold","normal")))
    s.ht()

def main():
    """
    calls all of the functions above and assigns variables for the required parameters
    return: none
    """
    alex = turtle.Turtle()      # each function has a distinct turtle object
    zoe = turtle.Turtle()
    bs = turtle.Turtle()
    job = turtle.Turtle()
    wn = turtle.Screen()

    buckle_width = 4            # assigning variable parameters
    ss = 50
    wr = 10

    background_window(wn)       #calling the functions as part of main with the variable parameters assigned
    exterior_blade(alex,ss)
    blade_wheel(zoe, 10)
    buckles(bs)
    wryturt(job)

    wn.exitonclick()            # had a huge problem of scope earlier. Happy to have that worked out with this

main()
