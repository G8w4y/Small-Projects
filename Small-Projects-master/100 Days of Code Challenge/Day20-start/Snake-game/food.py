from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))


    def reset_food_placement(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
