from turtle import Turtle

up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        position = [(0, 0), (-20, 0), (-40, 0)]
        for co_or in position:
            self.add_segment(co_or)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for s_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s_num - 1].xcor()
            new_y = self.segments[s_num - 1].ycor()
            self.segments[s_num].goto(new_x, new_y)
        self.segments[0].forward(15)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
