from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce(self):
        self.y *= -1
        
    def reflect(self):
        self.x *= -1
        self.move_speed *= 0.9
        
    def reset_ball(self):
        self.goto(0,0)
        self.reflect()
        self.move_speed = 0.1
        