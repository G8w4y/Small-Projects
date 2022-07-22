from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def return_home():
    tim.penup()
    tim.home()
    tim.pendown()


def clear_screen():
    screen.resetscreen()


screen = Screen()
screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=return_home, key="space")
screen.onkeypress(fun=clear_screen, key="c")
screen.exitonclick()
