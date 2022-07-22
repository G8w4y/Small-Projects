from time import time
from turtle import Turtle, Screen
from random import choice, randint
import turtle
from data import colors_list, direction_list
turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")
tim.speed("fastest")

# for n in range(4):
#     tim.right(90)
#     tim.forward(100)

tim.pencolor("black")

def shape(angles):
    corner_angles = 360 / angles
    paces = 100
    color = choice(colors_list)
    tim.pencolor(color)

    for i in range(angles):
        tim.right(corner_angles)
        tim.forward(paces)


def random_walk():
    color = choice(colors_list)
    tim.pensize(1)
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    #tim.pencolor(random_color)
    tim.right(choice(direction_list))
    tim.forward(40)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    my_tuple = r, g, b
    return my_tuple


def circle():
    angles = 30
    paces = 25
    color = choice(colors_list)
    tim.pencolor(0, 0, 0)

    for i in range(angles):
        tim.pencolor(color)
        tim.right(360 / angles)
        tim.forward(paces)


def spirograph(number_of_circles):
    turn_angle = 360 / number_of_circles

    for i in range(0, number_of_circles):
        tim.setheading(i*turn_angle)
        circle()


# for i in range(10, 501):
#     random_walk()
#     spirograph(30)

def pace():
    for paces in range(25):
        tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(25)


tim.pensize(18)
# y_list = []
y_list = list(range(-200, 400, 25))

#print(y_list)

tim.hideturtle()
tim.penup()
tim.setx(-300)
tim.sety(-200)
tim.pendown()

for element in range(0, len(y_list) - 1):
    tim.setx(-300)
    tim.sety(y_list[element])
    pace()

#pace()


#spirograph(30)

# for i in range(3, 20):
#     shape(i)


window = Screen()
window.screensize(500, 400)
#print(window.screensize())
window.exitonclick()
