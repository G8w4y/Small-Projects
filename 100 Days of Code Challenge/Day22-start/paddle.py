from turtle import Turtle

PADDLE_ONE_STARTING_POSITIONS_LIST = [(-300, -15), (-300, -10), (-300, -5),(-300, 0), (-300, 5), (-300, 10),(-300, 15)]

PADDLE_TWO_STARTING_POSITIONS_LIST = [(300, -15), (300, -10), (300, -5),(300, 0), (300, 5), (300, 10),(300, 15)]

MOVE_DISTANCE = 10

class Paddles():
    def __init__(self) -> None:
        self.paddle_one_list = []

        self.paddle_two_list = []

        self.set_paddles_starting_positions()

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

    
    def move_paddle_one_up(self):
        """Moves leftmost paddle up"""
        for segment in self.paddle_one_list:
            current_pos = self.paddle_one_list[segment].pos()
            self.paddle_one_list[segment].setpos(current_pos[0],current_pos[1] + MOVE_DISTANCE)


    def move_paddle_one_down(self):
        """Moves leftmost paddle up"""
        for segment in self.paddle_one_list:
            self.paddle_one_list[segment].backward(MOVE_DISTANCE)

    def move_paddle_two_up(self):
        """Moves leftmost paddle up"""
        for segment in self.paddle_two_list:
            self.paddle_two_list[segment].forward(MOVE_DISTANCE)


    def move_paddle_two_down(self):
        """Moves leftmost paddle up"""
        for segment in self.paddle_two_list:
            self.paddle_two_list[segment].backward(MOVE_DISTANCE)