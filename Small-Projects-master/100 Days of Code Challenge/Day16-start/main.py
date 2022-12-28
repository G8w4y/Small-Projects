from turtle import Turtle, Screen
from pokedex_data import pokemon
# print(another_module.another_variable)

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# my_screen = Screen()
# timmy.forward(100)

# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"], "l")
print(table)
