import turtle

def make_roof(bob):
    '''
    Makes the top line of the car
    :param bob: bob is the turtle
    :return:
    '''
    bob.penup()
    bob.setpos(-100, 100)
    bob.pendown()
    bob.forward(200)
    bob.right(40)

def make_back_windshield(bob):
    '''
    draws the front windsheild
    :param bob: bob is the turtle
    :return:
    '''
    bob.forward(150)
    bob.left(40)

def make_trunk(bob):
    '''
    draws the front of the car
    :param bob:bob is the turtle
    :return:
    '''
    bob.forward(100)
    bob.right(90)
    bob.forward(90)
    bob.right(90)
    bob.forward(90)
    bob.right(90)

def make_wheel(bob):
    '''
    draws the right wheel
    :param bob:bob is the turtle
    :return:
    '''
    for side in range(540):
        bob.forward(0.8)
        bob.left(1)
    bob.right(90)

def make_bottom(bob):
    '''
    draws the line between the wheels
    :param bob: bob is the turtle
    :return:
    '''
    bob.forward(250)
    bob.right(90)

def make_wheel(bob):
    '''
    draws the left wheel
    :param bob: bob is the turtle
    :return:
    '''
    for side in range(540):
        bob.forward(0.8)
        bob.left(1)
    bob.right(90)

def make_front(bob):
    '''
    draws the trunk
    :param bob: bob is the turtle
    :return:
    '''
    bob.forward(80)
    bob.right(110)
    bob.forward(100)
    bob.right(70)
    bob.fd(65)

def make_front_windshield(bob):
    '''
    draws the line of the back windsheild
    :param bob: bob is the turtle
    :return:
    '''
    bob.left(46)
    bob.forward(128)

def make_back_window(bob):
    '''
    draws the the back windsheild
    :param bob: bob is the turtle
    :return:
    '''
    bob.right(136)
    bob.fd(90)
    bob.rt(90)
    bob.fd(90)

def make_passenger_window(bob):
    '''
    draws the back window
    :param bob: bob is the turtle
    :return:
    '''
    bob.penup()
    bob.rt(180)
    bob.fd(100)
    bob.pendown()
    for side in range(4):
        bob.fd(80)
        bob.lt(90)

def make_driver_window(bob):
    '''
     draws the right window with the person in it
    :param bob: bob is the turtle
    :return:
    '''
    bob.penup()
    bob.fd(90)
    bob.pendown()
    for side in range(4):
        bob.fd(80)
        bob.lt(90)

def make_windsheild(bob):
    '''
     draws the front windsheild
    :param bob: bob is the turtle
    :return:
    '''
    bob.penup()
    bob.fd(100)
    bob.lt(90)
    bob.fd(90)
    bob.rt(180)
    bob.pendown()
    bob.forward(95)
    bob.lt(90)
    bob.forward(115)

def make_stearing_wheel(bob):
    '''
    draws the stearing wheel
    :param bob: bob is the turtle
    :return:
    '''
    bob.penup()
    bob.right(180)
    bob.fd(50)
    bob.pendown()
    bob.right(90)
    for side in range(180):
        bob.fd(0.3)
        bob.lt(1)

def make_arm(bob):
    '''
    draws the line from stearing wheel to the end of the windowsheild
    :param bob:bob is the turtle
    :return:
    '''
    bob.penup()
    bob.rt(90)
    bob.fd(30)
    bob.rt(90)
    bob.fd(15)
    bob.pendown()
    bob.rt(90)
    bob.fd(50)

def make_driver(bob):
    '''
    draws the person in the cars
    :param bob: bob is the turtle
    :return:
    '''
    bob.penup()
    bob.rt(180)
    bob.fd(70)
    bob.pendown()
    bob.fd(10)
    bob.lt(90)
    bob.fd(10)
    bob.rt(90)
    bob.fd(20)
    bob.rt(90)
    bob.fd(10)
    bob.penup()
    bob.fd(10)
    bob.lt(90)
    bob.fd(5)
    bob.rt(90)
    bob.pendown()
    for side in range(360):
        bob.fd(0.25)
        bob.rt(1)
def make_sun(bob):
    '''
    draws the circle and the fils it in
    :param bob: bob is the turtle
    :return:
    '''
    bob.penup()
    bob.fd(200)
    bob.lt(90)
    bob.fd(200)
    bob.pendown()
    bob.pencolor('#DFE204')
    bob.rt(90)
    bob.color('#DFE204')
    bob.begin_fill()
    for side in range(360):
        bob.fd(0.5)
        bob.lt(1)
    bob.end_fill()
def main():

    turtle.colormode(255)

    wn = turtle.Screen()
    bob = turtle.Turtle()
    bob.speed(100)
    bob.hideturtle()
    wn.bgcolor('gray')

    make_roof(bob)
    make_back_windshield(bob)
    make_trunk(bob)
    make_wheel(bob)
    make_bottom(bob)
    make_wheel(bob)
    make_front(bob)
    make_front_windshield(bob)
    make_back_window(bob)
    make_passenger_window(bob)
    make_driver_window(bob)
    make_windsheild(bob)
    make_stearing_wheel(bob)
    make_arm(bob)
    make_driver(bob)
    make_sun(bob)
    wn.exitonclick()
main()
