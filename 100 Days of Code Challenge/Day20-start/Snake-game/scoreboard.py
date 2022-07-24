from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("grey")
        self.speed("fastest")
        self.goto(x=0, y=270)

        self.score = 0
        self.write(f"SCORE: {self.score}", move=False,align="center",font=("Arial", 20,"normal"))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", move=False,align="center",font=("Arial", 20,"normal"))

class Wall(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.xcoordinates_list = []
        self.ycoordinates_list = []
        self.wall_coordinates_list = []
        self.walls = []
        for xcoor in range(-280,281):
            self.xcoordinates_list.append(xcoor)
        for ycoor in range(-280,281):
            self.ycoordinates_list.append(ycoor)
        
        # Create the coordinates for the top side of screen
        for coor in self.xcoordinates_list:
            self.wall_coordinates_list.append((self.xcoordinates_list[coor], 280))
        # Create the coordinates for the bottom side of screen
        for coor in self.xcoordinates_list:
            self.wall_coordinates_list.append((self.xcoordinates_list[coor], -280))
        # Create the coordinates for the left side of screen
        for coor in self.ycoordinates_list:
            self.wall_coordinates_list.append(-280), (self.ycoordinates_list[coor])
        # Create the coordinates for the right side of screen
        for coor in self.ycoordinates_list:
            self.wall_coordinates_list.append(280), (self.ycoordinates_list[coor])
        
        # Create and place every wall piece along the screens edges
        for coordinate in self.wall_coordinates_list:
            new_wall = Turtle()
            new_wall = self.penup
            new_wall = self.shape("square")
            new_wall = self.color("grey")
            new_wall = self.goto(self.wall_coordinates_list[coordinate])
            self.walls.append(new_wall)


        print(self.wall_coordinates_list)

wall = Wall()
        
