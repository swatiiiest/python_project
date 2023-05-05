from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("snake game")
screen.tracer(0)

# seg1 = Turtle("square")
# seg1.color("black")
#
# seg2 = Turtle("square")
# seg2.color("black")
# seg2.goto(-20,0)
#
# seg3 = Turtle("square")
# seg3.color("black")
# seg3.goto(-40,0)
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.update_score()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280\
            or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    for seg in my_snake.segments[1:]:
        if my_snake.head.distance(seg) < 5:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
