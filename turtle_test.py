from turtle import Turtle, Screen
import random

COLORS = ["yellow", "blue", "purple", "green", "orange"]

screen = Screen()
screen.setup(width=500, height=500)
tim = Turtle()
print(dir(tim))
tim.shape("turtle")
tim.pu()
tim.fd(20)
tim.speed(10)
while tim.xcor() < 239:
    tim.fd(10)
    tim.color(random.choice(COLORS))

screen.exitonclick()