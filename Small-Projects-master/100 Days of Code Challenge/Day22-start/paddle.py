from turtle import Turtle

PADDLE_ONE_STARTING_POSITIONS_LIST = [(-350, -25), (-350, -20), (-350, -15), (-350, -10), (-350, -5),(-350, 0), (-350, 5), (-350, 10),(-350, 15), (-350, 20), (-350, 25)]

PADDLE_TWO_STARTING_POSITIONS_LIST = [(350, -25), (350, -20), (350, -15), (350, -10), (350, -5),(350, 0), (350, 5), (350, 10),(350, 15), (350, 20), (350, 25)]

MOVE_DISTANCE = 20


class Paddles():
    def __init__(self) -> None:
        self.paddle_one_list = []

        self.paddle_two_list = []

        self.set_paddles_starting_positions()
        #print(self.paddle_one_list[0].xcor() <= -300)
        #print(self.paddle_one_list[0].heading())

    def set_paddles_starting_positions(self):
        for position in range(0, len(PADDLE_ONE_STARTING_POSITIONS_LIST)):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed("fastest")
            new_segment.setposition(PADDLE_ONE_STARTING_POSITIONS_LIST[position])
            new_segment.setheading(90)
            self.paddle_one_list.append(new_segment)
        for position in range(0, len(PADDLE_TWO_STARTING_POSITIONS_LIST)):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed("fastest")
            new_segment.setposition(PADDLE_TWO_STARTING_POSITIONS_LIST[position])
            new_segment.setheading(90)
            self.paddle_two_list.append(new_segment)
    # def move_snake_forward(self):
    #     move_counter = 0
    #     self.snakes_list[0].forward(MOVE_DISTANCE)
    #     for segment in range(1, len(self.snakes_list)):
    #         self.snakes_list[segment].setposition(self.positions_list[move_counter])
    #         move_counter += 1
    #     for segment in range(0, len(self.snakes_list)):
    #         self.positions_list[segment] = self.snakes_list[segment].position()
    #     #print(self.positions_list)
    def move_paddle_one_turn_on_toggle_or_wall(self):
        """Moves the paddle, changing direction when toggled or collission with wall."""
        if self.paddle_one_list[-1].ycor() >= 300:
            for segment in range(0, len(self.paddle_one_list)):
                self.paddle_one_list[segment].setheading(270)
            for segment in range(0, len(self.paddle_one_list)):
                self.paddle_one_list[segment].forward(MOVE_DISTANCE)
        elif self.paddle_one_list[0].ycor() <= -300:
            for segment in range(0, len(self.paddle_one_list)):
                self.paddle_one_list[segment].setheading(90)
            for segment in range(0, len(self.paddle_one_list)):
                self.paddle_one_list[segment].forward(MOVE_DISTANCE)
        else:
            for segment in range(0, len(self.paddle_one_list)):
                self.paddle_one_list[segment].forward(MOVE_DISTANCE)

    def move_paddle_two_turn_on_toggle_or_wall(self):
        """Moves the paddle, changing direction when toggled or collission with wall."""
        if self.paddle_two_list[-1].ycor() >= 300:
            for segment in range(0, len(self.paddle_two_list)):
                self.paddle_two_list[segment].setheading(270)
            for segment in range(0, len(self.paddle_two_list)):
                self.paddle_two_list[segment].forward(MOVE_DISTANCE)
        elif self.paddle_two_list[0].ycor() <= -300:
            for segment in range(0, len(self.paddle_two_list)):
                self.paddle_two_list[segment].setheading(90)
            for segment in range(0, len(self.paddle_two_list)):
                self.paddle_two_list[segment].forward(MOVE_DISTANCE)
        else:
            for segment in range(0, len(self.paddle_two_list)):
                self.paddle_two_list[segment].forward(MOVE_DISTANCE)



    def toggle_paddle_one(self):
        """toggles the leftmost paddles heading"""
        if self.paddle_one_list[0].heading() == 90:
            for segment in range(0, len(self.paddle_one_list)):
                self.paddle_one_list[segment].setheading(270)
        else:
            for segment in range(0, len(self.paddle_one_list)):
                self.paddle_one_list[segment].setheading(90)


    def toggle_paddle_two(self):
        """toggles the leftmost paddles heading"""
        if self.paddle_two_list[0].heading() == 90:
            for segment in range(0, len(self.paddle_two_list)):
                self.paddle_two_list[segment].setheading(270)
        else:
            for segment in range(0, len(self.paddle_two_list)):
                self.paddle_two_list[segment].setheading(90)

                


    # def move_paddle_one_up(self):
    #     """Moves leftmost paddle up"""
    #     for segment in self.paddle_one_list:
    #         self.paddle_one_list[segment].forward(MOVE_DISTANCE)

    # def move_paddle_one_down(self):
    #     """Moves leftmost paddle down"""
    #     for segment in self.paddle_one_list:
    #         self.paddle_one_list[segment].backward(MOVE_DISTANCE)

    # def move_paddle_two_up(self):
    #     """Moves rightmost paddle up"""
    #     for segment in self.paddle_two_list:
    #         self.paddle_two_list[segment].forward(MOVE_DISTANCE)


    # def move_paddle_two_down(self):
    #     """Moves rightmost paddle up"""
    #     for segment in self.paddle_two_list:
    #         self.paddle_two_list[segment].backward(MOVE_DISTANCE)

#Paddles()
