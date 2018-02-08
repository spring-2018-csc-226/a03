######################################################################
# Author: Ezra Skwarka              TODO: Change this to your name, if modifying
# Username: Skwarkae                     TODO: Change this to your username, if modifying
#
# Assignment: A#: A Pair of Fully Functional Gitty Psychedelic  Robotic Turtles
# Purpose: Make a complex thing even more complex
######################################################################
import turtle


def make_house(turt, center_x, center_y):
    """
    Make the whole thing

    :param turt: is turtle
    :param center_x: supposed to be the center x cord...
    :param center_y: see above
    :return: None
    """
    # Roof
    turt.pensize(4)
    turt.pencolor("orange")
    turt.up()
    turt.goto(center_x+40, center_y - 100) #left tip
    turt.down()
    turt.circle(90, -90) #right tip
    turt.up()
    turt.goto(center_x-48, center_y)
    turt.circle(-110, 90)
    turt.down()
    turt.circle(-110, -80)
    turt.circle(-10,-180) #curl
    turt.circle(10,-180)
    turt.circle(10,180) #uncurl and go to start of body
    turt.circle(-10,180)
    turt.circle(-110, 45)
    # Body
    turt.pencolor("brown")
    turt.goto(turt.xcor()+20,center_y-165) #left base
    turt.goto(turt.xcor()+40,turt.ycor())
    x_holder = turt.xcor()
    y_holder = turt.ycor()
    turt.pencolor("#738778") #start door
    turt.goto(x_holder,y_holder+60)
    turt.goto(turt.xcor()-20,turt.ycor())
    turt.goto(turt.xcor(),turt.ycor()-60)
    turt.up()
    turt.goto(x_holder,y_holder)
    turt.down() #end door
    turt.pencolor("brown")
    turt.goto(turt.xcor()+22,center_y-85) #right base
    draw_window(turt, -65, -75, 10, center_x, center_y)


def draw_window(turt, x_window, y_window, window_rad, center_x, center_y ):
    """
    Windows are hard

    :param turt: is still turtle
    :param x_window: X cord of middle of window
    :param y_window: Y cord of middle of window
    :param window_rad: Window radius
    :param center_x: Center X of house
    :param center_y: Center Y of house
    :return:
    """
    x_holder = turt.xcor()
    y_holder = turt.ycor()
    turt.pencolor("#738778")
    turt.up()
    turt.goto(center_x + x_window-window_rad,center_y + y_window-window_rad)
    turt.down()
    turt.circle(window_rad)
    turt.up()
    turt.goto(x_holder,y_holder)
    turt.down()


def main():
    screen = turtle.Screen()
    screen.bgcolor("light gray")
    house_boi=turtle.Turtle()
    house_boi.speed(0)
    for i in range(6):
        make_house(house_boi,0,-100 +(i*100))
    screen.exitonclick()


main()
