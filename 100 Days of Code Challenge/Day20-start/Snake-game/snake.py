from turtle import Turtle

SNAKE_STARTING_POSITIONS_LIST = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake():
    def __init__(self) -> None:
        self.positions_list = []

        self.snakes_list = []

        self.snake_heading = []

        self.set_snake_head_starting_position()

    def set_snake_head_starting_position(self):
        for position in range(0, len(SNAKE_STARTING_POSITIONS_LIST)):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed("fastest")
            new_segment.setposition(SNAKE_STARTING_POSITIONS_LIST[position])
            self.snakes_list.append(new_segment)
        for segment in range(0, len(self.snakes_list)):
            self.positions_list.append(self.snakes_list[segment].position())
        self.snake_heading.append(self.snakes_list[0].heading())


    def move_snake_forward(self):
        move_counter = 0
        self.snakes_list[0].forward(MOVE_DISTANCE)
        for segment in range(1, len(self.snakes_list)):
            self.snakes_list[segment].setposition(self.positions_list[move_counter])
            move_counter += 1
        for segment in range(0, len(self.snakes_list)):
            self.positions_list[segment] = self.snakes_list[segment].position()
        #print(self.positions_list)


    def turn_left(self):
        """Turns the head of the snake by 90 degrees leftwards in relation to the heads current heading"""
        self.snake_heading[0] += 90.0
        self.snakes_list[0].setheading(self.snake_heading[0])


    def turn_right(self):
        """Turns the head of the snake by 90 degrees rightwards in relation to the heads current heading"""
        self.snake_heading[0] -= 90.0
        self.snakes_list[0].setheading(self.snake_heading[0])
