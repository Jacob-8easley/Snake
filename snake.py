from turtle import Turtle,Screen
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake(Turtle):

    def __init__(self):
        #self.snake_length = snake_length
        super().__init__()
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]

    def generate_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for snake_seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[snake_seg-1].xcor()
            new_y = self.segments[snake_seg-1].ycor()
            self.segments[snake_seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)