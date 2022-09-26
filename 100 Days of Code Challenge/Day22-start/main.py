# Create the screen
from turtle import Screen, Turtle

from scoreboard import LeftScoreboard, RightScoreboard, CenterLine
from paddle import Paddles
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
#screen.setworldcoordinates(llx= -390,lly= -300, urx= 302, ury=290)
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
        time.sleep(0.10)
        screen.update()
        paddles.move_paddle_one_turn_on_toggle_or_wall()
        paddles.move_paddle_two_turn_on_toggle_or_wall()
        ball.move_ball_forward()
        ball.ball_wall_bounce()
        #print(paddles.paddle_one_list[0].pos())
        #print(paddles.paddle_one_list[0].ycor() >= 300)

        #Detect collision with paddle one and revert direction
        for paddle in range(len(paddles.paddle_one_list)):
            if paddles.paddle_one_list[paddle].distance(ball) < 20:
                if ball.x_move < 0:
                    ball.x_move -= 1
                else:
                    ball.x_move +=1
                #ball.y_move += 1
                ball.x_move *= -1

        #Detect collission with paddle two and revert direction
        for paddle in range(len(paddles.paddle_two_list)):
            if paddles.paddle_two_list[paddle].distance(ball) < 20:
                if ball.x_move < 0:
                    ball.x_move -= 1
                else:
                    ball.x_move +=1
                ball.x_move *= -1

        if ball.xcor() < -400:
            right_scoreboard.increase_score()
            ball.reset_ball()
        elif ball.xcor() > 400:
            left_scoreboard.increase_score()
            ball.reset_ball()

        if left_scoreboard.score == 10:
            game_is_on = False
        elif right_scoreboard.score == 10:
            game_is_on = False

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
while keep_playing == "y":
    left_scoreboard.score = 0
    left_scoreboard.clear()
    left_scoreboard.write(f"{left_scoreboard.score}", move=False, align="center", font=("Arial", 28, "normal"))
    right_scoreboard.score = 0
    right_scoreboard.clear()
    right_scoreboard.write(f"{right_scoreboard.score}", move=False, align="center", font=("Arial", 28, "normal"))
    game()
    keep_playing = screen.textinput(title="Wan't to play again?", prompt="Press y to continue and anything else to quit.").lower()


screen.exitonclick()
