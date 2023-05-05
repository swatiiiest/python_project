import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("pong game")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.reflect()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_ball()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_ball()

    screen.update()

screen.exitonclick()
