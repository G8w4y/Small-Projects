from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Wall
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-305, -305, 305, 305)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

wall = Wall()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

print(snake.snakes_list[0].pos())

def game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.13)
        snake.move_snake_forward()

        # Detect collision with food
        if snake.snakes_list[0].distance(food) < 15:
            print("Nom nom nom")
            food.reset_food_placement()
            snake.extend_snake()
            scoreboard.increase_score()

        
        # Detect collision with tail
        for segment in range(1, len(snake.snakes_list)):
            if snake.snakes_list[0].distance(snake.snakes_list[segment]) < 15:
                scoreboard.game_over()
                game_is_on = False
                break



        if snake.snakes_list[0].xcor() == 300 or snake.snakes_list[0].xcor() == -300 or snake.snakes_list[0].ycor() == 300 or snake.snakes_list[0].ycor() == -300:
            scoreboard.game_over()
            game_is_on = False
            break
        # if snake.snakes_list[0].distance(wall.walls) < 10:
        #     print("You DEAD!")
        #     print(scoreboard.score)
        #     break
        #     #screen.bye()

        screen.listen()
        screen.onkeypress(fun=snake.turn_left, key="a")
        screen.onkeypress(fun=snake.turn_right, key="d")

game()
keep_playing = screen.textinput(title="Wan't to play again?", prompt="Press y to continue and anything else to quit.").lower()
if keep_playing == "y":
    game()

print(snake.snakes_list[0].pos())
screen.exitonclick()
