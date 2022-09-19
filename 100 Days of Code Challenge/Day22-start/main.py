# Create the screen
from turtle import Screen, Turtle

from scoreboard import LeftScoreboard, RightScoreboard, CenterLine
from paddle import Paddles
from ball import Ball
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(llx= -290,lly= -300, urx= 302, ury=290)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

# Create and move the paddle
paddles = Paddles()
ball = Ball()
left_scoreboard = LeftScoreboard()
right_scoreboard = RightScoreboard()
center_line = CenterLine()


# Create another paddle
# Create the ball and make it move
# Detect collission with wall and bounce
# Detect collission with paddle
# Detect when paddle misses
# Kepp score

def game():
    game_is_on = True
    while game_is_on:
        screen.update()
        
        paddles.move_paddle_one_turn_on_toggle_or_wall()
        paddles.move_paddle_two_turn_on_toggle_or_wall()
        ball.move_ball_forward()
        time.sleep(0.13)
        ball.ball_wall_bounce()
        #print(paddles.paddle_one_list[0].pos())
        #print(paddles.paddle_one_list[0].ycor() >= 300)

        #Detect collision with paddle one and revert direction
        for paddle in range(len(paddles.paddle_one_list)):
            if paddles.paddle_one_list[paddle].distance(ball) < 20:
                ball.setheading(ball.heading() - 180)

        #Detect collission with paddle two and revert direction
        for paddle in range(len(paddles.paddle_two_list)):
            if paddles.paddle_two_list[paddle].distance(ball) < 20:
                ball.setheading(ball.heading() + 180)

        screen.listen()
        # Listen for paddle 1 movement
        screen.onkeypress(fun=paddles.toggle_paddle_one, key="space")
        # screen.onkeypress(fun=paddles.move_paddle_one_up, key="w")
        # screen.onkeypress(fun=paddles.move_paddle_one_down, key="s")
        # Listen for paddle 2 movement
        screen.onkeypress(fun=paddles.toggle_paddle_two, key="0")
        #screen.onkeypress(fun=paddles.move_paddle_two_up, key="Up")
        #screen.onkeypress(fun=paddles.move_paddle_two_down, key="Down")


game()
keep_playing = screen.textinput(title="Wan't to play again?", prompt="Press y to continue and anything else to quit.").lower()
if keep_playing == "y":
    game()


screen.exitonclick()