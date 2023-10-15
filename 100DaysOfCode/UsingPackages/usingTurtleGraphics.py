# import turtle
# natasha = turtle.Turtle()

from turtle import Turtle, Screen

natasha = Turtle()
print(natasha.pencolor)
natasha.shape("turtle")
natasha.color("green")

natasha.forward(100)

screen = Screen()
print(screen.canvheight)
screen.exitonclick()