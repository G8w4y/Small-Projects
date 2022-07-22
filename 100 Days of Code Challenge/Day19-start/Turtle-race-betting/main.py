from turtle import Turtle, Screen

turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
turtle6 = Turtle()
turtle7 = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

turtles_list = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6, turtle7]

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

for turtle in range(0, len(turtles_list)):
    turtles_list[turtle].penup()
    turtles_list[turtle].shape("turtle")
    turtles_list[turtle].setposition(starting_positions[turtle]["x"], starting_positions[turtle]["y"])
    turtles_list[turtle].color(colours_list[turtle])

screen.listen()
screen.exitonclick()
