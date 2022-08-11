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
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 34, "normal"))


class Wall(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.coordinate_range_list = []
        self.lesser_coordinate_range_list = []
        self.upper_coordinates_list = []
        self.lesser_upper_coordinates_list = []
        self.lesser_lower_coordinates_list = []
        self.lower_coordinates_list = []
        self.wall_coordinates_list = []
        self.walls = []
        for coor in range(-300, 301, 10):
            self.coordinate_range_list.append(coor)
        for coor in range(-300, 301, 10):
            self.upper_coordinates_list.append(310)
        for coor in range(-300, 301, 10):
            self.lower_coordinates_list.append(-310)
        
        # Create the lesser lists
        for coor in range(-300, 301, 10):
            self.lesser_coordinate_range_list.append(coor)
        for coor in range(-300, 301, 10):
            self.lesser_upper_coordinates_list.append(303)
        for coor in range(-300, 301, 10):
            self.lesser_lower_coordinates_list.append(-303)
        
        
        print(self.coordinate_range_list)
        print(self.upper_coordinates_list)
        print(self.lower_coordinates_list)
        # #Create the coordinates for the top side of screen
        # for coor in self.xcoordinates_list:
        #     self.wall_coordinates_list.append((self.xcoordinates_list[coor], 280))
        # # Create the coordinates for the bottom side of screen
        # for coor in self.xcoordinates_list:
        #     self.wall_coordinates_list.append((self.xcoordinates_list[coor], -280))
        # # Create the coordinates for the left side of screen
        # for coor in self.ycoordinates_list:
        #     self.wall_coordinates_list.append(-280), (self.ycoordinates_list[coor])
        # # Create the coordinates for the right side of screen
        # for coor in self.ycoordinates_list:
        #     self.wall_coordinates_list.append(280), (self.ycoordinates_list[coor])
        # print(self.ycoordinates_list)


        # Create and place every wall piece along the screens upper edge
        for x, y in zip(self.coordinate_range_list, self.upper_coordinates_list):
            new_wall = Turtle()
            new_wall.penup()
            new_wall.shape("square")
            new_wall.color("grey")
            new_wall.speed("fastest")
            new_wall.goto(x, y)
            self.walls.append(new_wall)

        # Create and place every wall piece along the screens lower edge
        for x, y in zip(self.coordinate_range_list, self.lesser_lower_coordinates_list):
            new_wall = Turtle()
            new_wall.penup()
            new_wall.shape("square")
            new_wall.color("grey")
            new_wall.speed("fastest")
            new_wall.goto(x, y)
            self.walls.append(new_wall)
        
        # Create and place every wall piece along the screens left edge
        for x, y in zip(self.lower_coordinates_list, self.coordinate_range_list):
            new_wall = Turtle()
            new_wall.penup()
            new_wall.shape("square")
            new_wall.color("grey")
            new_wall.speed("fastest")
            new_wall.goto(x, y)
            self.walls.append(new_wall)
        
        # Create and place every wall piece along the screens right edge
        for x, y in zip(self.lesser_upper_coordinates_list, self.coordinate_range_list):
            new_wall = Turtle()
            new_wall.penup()
            new_wall.shape("square")
            new_wall.color("grey")
            new_wall.speed("fastest")
            new_wall.goto(x, y)
            self.walls.append(new_wall)



        # for x, y in zip(self.xcoordinates_list, self.ycoordinates_list):
        #     new_wall = Turtle()
        #     new_wall = self.penup
        #     new_wall = self.shape("square")
        #     new_wall = self.color("grey")
        #     new_wall = self.goto(x, y)

        #     #new_wall = self.goto(self.wall_coordinates_list[coordinate][0], self.wall_coordinates_list[coordinate][1])
        #     #new_wall = self.goto(tuple[self.wall_coordinates_list[coordinate]])
        #     self.walls.append(new_wall)
        #     print(self.pos())


        # print(self.wall_coordinates_list[0][1])
        # print(self.walls.pos())
        # print(len(self.walls))

#wall = Wall()

