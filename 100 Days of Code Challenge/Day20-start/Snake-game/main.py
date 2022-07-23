from ast import While
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake_head1 = Turtle()
snake_head2 = Turtle()
snake_head3 = Turtle()

#snake_head_list = [snake_head1, snake_head2, snake_head3]

snake_starting_positions_list = [(0, 0), (-20, 0), (-40, 0)]

positions_list = []

snakes_list = []

snake_heading = []

def set_snake_head_starting_position():
    for position in range(0, len(snake_starting_positions_list)):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.setposition(snake_starting_positions_list[position])
        snakes_list.append(new_segment)
    for segment in range(0, len(snakes_list)):
        positions_list.append(snakes_list[segment].position())
    screen.update()

def move_snake_forward():
    move_counter = 0
    snakes_list[0].forward(20)
    for segment in range(1, len(snakes_list)):
        snakes_list[segment].setposition(positions_list[move_counter])
        move_counter += 1
    for segment in range(0, len(snakes_list)):
        positions_list[segment] = snakes_list[segment].position()
    print(positions_list)


def turn_left():
    snake_heading[0] += 90.0
    snakes_list[0].setheading(snake_heading[0])


def turn_right():
    snake_heading[0] -= 90.0
    snakes_list[0].setheading(snake_heading[0])


set_snake_head_starting_position()
snake_heading.append(snakes_list[0].heading())
# print(positions_list)
# print(snakes_list[0].heading())
# snakes_list[0].setheading(snakes_list[0].heading() - 90.0)
# print(snakes_list[0].heading())

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.13)
    move_snake_forward()
    screen.listen()
    screen.onkeypress(fun=turn_left, key="a")
    screen.onkeypress(fun=turn_right, key="d")

screen.exitonclick()
