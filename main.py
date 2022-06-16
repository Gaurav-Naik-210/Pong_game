from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=1000, height=700)
screen.tracer(0)

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    # Detect r_paddle miss ball
    if ball.xcor() > 450:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect r_paddle miss ball
    if ball.xcor() < -450:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
