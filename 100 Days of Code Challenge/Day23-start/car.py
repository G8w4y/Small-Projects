from turtle import Turtle
from random import randint, choice

# Create possible y-range list
Y_RANGE = list(range(-300, 301))
print(Y_RANGE)

SNAKE_STARTING_POSITIONS_LIST = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Car(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.cars_list = []
        color = tuple(red=randint(0, 255), green=randint(0, 255), blue=randint(0, 255))
        random_y = choice(Y_RANGE)
        car_starting_positions_list = [(random_y, 300), (random_y + 10, 300), (random_y + 20, 300)]
        for position in car_starting_positions_list:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.goto(position)
            new_segment.shape("square")
            new_segment.color(color)
            new_segment.setheading(180)
            self.cars_list.append(new_segment)
