import time
import turtle
t = turtle.Turtle()
circle = 50
high = 100
low = -100
t.speed(0)

t.color("red")
t.pu()
t.goto(high, high)
t.pd()
t.circle(circle)

t.color("blue")
t.pu()
t.goto(low, high)
t.pd()
t.circle(circle)

t.color("green")
t.pu()
t.goto(high, low)
t.pd()
t.circle(circle)

t.color("purple")
t.pu()
t.goto(low, low)
t.pd()
t.circle(circle)

time.sleep(1)
