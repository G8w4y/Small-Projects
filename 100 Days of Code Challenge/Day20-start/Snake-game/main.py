from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Wall
import time

screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

wall = Wall()
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# snake_head1 = Turtle()
# snake_head2 = Turtle()
# snake_head3 = Turtle()

# snake_head_list = [snake_head1, snake_head2, snake_head3]

# In snake class
# snake_starting_positions_list = [(0, 0), (-20, 0), (-40, 0)]
# positions_list = []
# snakes_list = []
# snake_heading = []

# In snake class
# def set_snake_head_starting_position():
#     for position in range(0, len(snake_starting_positions_list)):
#         new_segment = Turtle()
#         new_segment.shape("square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.speed("fastest")
#         new_segment.setposition(snake_starting_positions_list[position])
#         snakes_list.append(new_segment)
#     for segment in range(0, len(snakes_list)):
#         positions_list.append(snakes_list[segment].position())
#     screen.update()

# In snake class
# def move_snake_forward():
#     move_counter = 0
#     snakes_list[0].forward(20)
#     for segment in range(1, len(snakes_list)):
#         snakes_list[segment].setposition(positions_list[move_counter])
#         move_counter += 1
#     for segment in range(0, len(snakes_list)):
#         positions_list[segment] = snakes_list[segment].position()
#     print(positions_list)

# In snake class
# def turn_left():
#     snake_heading[0] += 90.0
#     snakes_list[0].setheading(snake_heading[0])

# In snake class
# def turn_right():
#     snake_heading[0] -= 90.0
#     snakes_list[0].setheading(snake_heading[0])


#Snake().set_snake_head_starting_position()
#Snake().snake_heading.append(Snake().snakes_list[0].heading())
# print(positions_list)
# print(snakes_list[0].heading())
# snakes_list[0].setheading(snakes_list[0].heading() - 90.0)
# print(snakes_list[0].heading())

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.13)
    snake.move_snake_forward()

    # Detect collision with food
    if snake.snakes_list[0].distance(food) < 15:
        print("Nom nom nom")
        food.reset_food_placement()
        scoreboard.increase_score()

    # Detect collission with walls
    if snake.snakes_list[0].distance(wall.walls) < 5:
        print("You DEAD!")
        print(scoreboard.score)
        break
        #screen.bye()

    screen.listen()
    screen.onkeypress(fun=snake.turn_left, key="a")
    screen.onkeypress(fun=snake.turn_right, key="d")

screen.exitonclick()
