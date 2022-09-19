from turtle import Turtle
import random

BALL_LENGTH = 0.5
BALL_WIDTH = 0.5
MOVE_DISTANCE = 20

HEADING_LIST = []
for element in range(-80, 81):
    HEADING_LIST.append(element)

for element in range(160, 261):
    HEADING_LIST.append(element)

#print(HEADING_LIST)


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=BALL_LENGTH, stretch_wid=BALL_WIDTH)
        self.speed("fastest")
        self.set_random_heading()
      
    def set_random_heading(self):
        self.setheading(random.choice(HEADING_LIST))
    
    def move_ball_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_ball(self):
        self.goto(x=0, y=0)

    def ball_wall_bounce(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            if self.heading in range(0, 91):
                self.setheading(self.heading() + 270)
            elif self.heading in range(91, 181):
                self.setheading(self.heading() + 90)
            elif self.heading in range(181, 271):
                self.setheading(self.heading() - 90)
            elif self.heading in range(271, 1):
                self.setheading(self.heading() + 90)
        print(self.heading())
