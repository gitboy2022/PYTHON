import time
import turtle
t = turtle.Turtle()
loop = 0
t.speed(0)

while loop <= 3:
    t.circle(100)
    t.rt(90)
    loop = loop + 1

t.circle(100)

time.sleep(1)
