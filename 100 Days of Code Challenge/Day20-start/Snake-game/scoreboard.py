from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("grey")
        self.speed("fastest")
        self.goto(x=0, y=270)

        self.score = 0
        self.write(f"SCORE: {self.score}", move=False,align="center",font=("Arial", 20,"normal"))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", move=False,align="center",font=("Arial", 20,"normal"))
