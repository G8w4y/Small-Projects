from turtle import Turtle

MOVE_DISTANCE = 20


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(0, -290)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
