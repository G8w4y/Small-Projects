from turtle import Turtle, Screen

import another_module

print(another_module.another_variable)

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("coral")
my_screen = Screen()
timmy.forward(100)

print(my_screen.canvheight)
my_screen.exitonclick()