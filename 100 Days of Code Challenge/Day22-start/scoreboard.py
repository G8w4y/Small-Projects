from turtle import Turtle

class LeftScoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("grey")
        self.speed("fastest")
        self.goto(x=-20, y=250)

        self.score = 0
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 28, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 28, "normal"))


    def game_over(self):
        self.goto(0, 100)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 34, "normal"))

class RightScoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("grey")
        self.speed("fastest")
        self.goto(x=20, y=250)

        self.score = 0
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 28, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 28, "normal"))


    def game_over(self):
        self.goto(0, 100)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 34, "normal"))


class CenterLine(Turtle):

    def __init__(self) -> None:
        super().__init__()
        for i in range(-300,310,15):
            center_line_dot = Turtle()
            center_line_dot.penup()
            center_line_dot.shape("circle")
            center_line_dot.color("white")
            center_line_dot.speed("fastest")
            center_line_dot.shapesize(stretch_len=0.25, stretch_wid=0.25)
            center_line_dot.goto(x=0, y=i)
