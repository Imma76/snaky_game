from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(snake.up, key="Up")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.down, key="Down")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
        print("nom")

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
       #detect collision with tail

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()


screen.exitonclick()