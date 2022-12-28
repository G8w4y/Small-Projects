# Create the screen
from turtle import Screen, Turtle
import time
import math

from player import Player
from car import Car

screen = Screen()
screen.setup(width=600, height=600)
# screen.setworldcoordinates(llx= -390,lly= -300, urx= 302, ury=290)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

level_screen = Turtle()
level_screen.hideturtle()
level_screen.penup()
level_screen.goto(-250, 260)
player = Player()
car = Car()

level = 1
car_counter = 0
starting_time = 0.1
difficulty = 0.8
modulo_counter = 5

keep_playing = True
while keep_playing:
    real_time = starting_time*(difficulty)**level
    time.sleep(real_time)
    print(real_time)
    level_screen.clear()
    level_screen.write(f"Level: {level}", move=False, align="center", font=("Arial", 20, "normal"))
    screen.update()
    # Create new car if there has been 5 updates of the screen
    if car_counter % 5 == 0:
        #could also solve this by chance. Like rolling a dice
        car.spawn_new_car()
    car.move_cars()
    car_counter += 1
    car.delete_car()


    screen.listen()
    screen.onkeypress(fun=player.move_forward, key="w")

    # Check if turtle survived
    if player.ycor() >= 300:
        pop_up = Turtle()
        pop_up.hideturtle()
        pop_up.write("YOU SURVIVED! increasing difficulty!", move=False, align="center", font=("Arial", 20, "normal"))
        time.sleep(2)
        level += 1
        pop_up.clear()
        player.goto(0, -290)

    # Detect collission between turtle and car
    for element in car.cars_list:
        # if car.cars_list[car.cars_list.index(element)].distance(player) <= 15:
        if math.sqrt((player.ycor() - car.cars_list[car.cars_list.index(element)].ycor())**2) <= 19 and math.sqrt((((player.xcor()) - (car.cars_list[car.cars_list.index(element)].xcor()))**2)) <= 10:
            keep_playing = False
            pop_up = Turtle()
            pop_up.hideturtle()
            pop_up.write("YOU DIED!", move=False, align="center", font=("Arial", 20, "normal"))


screen.exitonclick()