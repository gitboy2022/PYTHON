import turtle
import time
t = turtle.Turtle()
variable = 0
t.speed(0)

colors = ["red", "orange", "green"]

while variable <= 2:
    t.color(colors[variable])
    t.circle(50)
    t.rt(120)
    variable = variable + 1

time.sleep(1)
