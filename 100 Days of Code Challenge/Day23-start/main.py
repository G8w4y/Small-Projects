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

player = Player()
car = Car()

keep_playing = True
while keep_playing:
    time.sleep(0.2)
    screen.update()
    car.spawn_new_car()
    car.move_cars()
    car.delete_car()


    screen.listen()
    screen.onkeypress(fun=player.move_forward, key="w")

    if player.ycor() >= 300:
        keep_playing = False
        pop_up = Turtle()
        pop_up.hideturtle()
        pop_up.write("YOU SURVIVED! YOU WON!", move=False, align="center", font=("Arial", 20, "normal"))

    for element in car.cars_list:
        #if car.cars_list[car.cars_list.index(element)].distance(player) <= 15:
        if math.sqrt((player.ycor() - car.cars_list[car.cars_list.index(element)].ycor())**2) <= 19 and math.sqrt((((player.xcor()) - (car.cars_list[car.cars_list.index(element)].xcor()))**2)) <= 10:
            keep_playing = False
            pop_up = Turtle()
            pop_up.hideturtle()
            pop_up.write("YOU DIED!", move=False, align="center", font=("Arial", 20, "normal"))


screen.exitonclick()