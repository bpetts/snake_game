from turtle import Screen
from Snake_Class import Snake
from Food_Class import Food
from Scoreboard_Class import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameover = False
while not gameover:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        snake.reset()
        score.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif segment == snake.segments[1]:
            if snake.head.position() == snake.segments[1].position:
                snake.reset()
                score.reset()
        elif snake.head.distance(segment) < 5:
            snake.reset()
            score.reset()

screen.exitonclick()
