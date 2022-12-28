from turtle import Turtle
from random import randint, choice
import time

COLORS_LIST = [
    'red', 'orange', 'yellow', 'green', 'blue',
    'purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro', 'gray',
    'dimgray', 'LightSlateGray', 'AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki'
]

# Create possible y-range list
Y_RANGE = list(range(-270, 291, 20))
#print(Y_RANGE)

LEVEL = 0

CAR_LENGTH = 2 #Was 1.5
CAR_WIDTH = 1


class Car(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()

        self.cars_list = []
        #car_starting_positions_list = [(random_y, 300), (random_y + 10, 300), (random_y + 20, 300)]
        # for position in car_starting_positions_list:
        #     new_segment = Turtle()
        #     new_segment.penup()
        #     new_segment.goto(position)
        #     new_segment.shape("square")
        #     new_segment.color(color)
        #     new_segment.setheading(180)
        #     self.cars_list.append(new_segment)

    def spawn_new_car(self):
        #if len(self.cars_list) < 20:
            #time.sleep(0.2)
        random_y = choice(Y_RANGE)
        #print(random_y)
        position = (300, random_y)
        new_car = Turtle()
        new_car.penup()
        new_car.goto(position)
        new_car.shape("square")
        new_car.shapesize(stretch_len=CAR_LENGTH, stretch_wid=CAR_WIDTH)
        new_car.color(choice(COLORS_LIST))
        new_car.setheading(180)
        self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            move_distance = 5
            car.forward(move_distance)

    def delete_car(self):
        #if len(self.cars_list) > 10:
        for car in self.cars_list:
            if car.xcor() < -310:
                del self.cars_list[self.cars_list.index(car)]
                #print(len(self.cars_list))
