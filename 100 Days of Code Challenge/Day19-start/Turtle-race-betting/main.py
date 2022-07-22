from turtle import Turtle, Screen
from random import choice


def set_starting_positions():
    """Sets shape and the starting position of each turtle in the turtles_list."""
    for turtle in range(0, len(turtles_list)):
        turtles_list[turtle].penup()
        turtles_list[turtle].shape("turtle")
        turtles_list[turtle].setposition(starting_positions[turtle]["x"], starting_positions[turtle]["y"])
        turtles_list[turtle].color(colours_list[turtle])


turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
turtle6 = Turtle()
turtle7 = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

turtles_list = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6, turtle7]

speed_list = [0, 1, 3, 6, 9, 12]

starting_positions = [
    {"x": -230, "y": -150},
    {"x": -230, "y": -100},
    {"x": -230, "y": -50},
    {"x": -230, "y": 0},
    {"x": -230, "y": 50},
    {"x": -230, "y": 100},
    {"x": -230, "y": 150},
    ]

colours_list = [
    "purple",
    "green",
    "red",
    "blue",
    "black",
    "peru",
    "gold"
]

race_is_on = True

set_starting_positions()

user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? Enter a color: \n'gold'\n'peru'\n'black'\n'blue'\n'red'\n'green'\n'purple'").lower()

while race_is_on:
    for turtle in range(0, len(turtles_list)):
        if turtles_list[turtle].xcor() >= 230:
            race_is_on = False
            if user_bet == colours_list[turtle]:
                print(f"The winner was {colours_list[turtle]}.\nYou bet {user_bet}.\nYou won!")
            else:
                print(f"The winner was {colours_list[turtle]}.\nYou bet {user_bet}.\nYou lost!")
        else:
            choice(turtles_list).forward(choice(speed_list))


screen.listen()
screen.exitonclick()
