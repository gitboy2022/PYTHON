import time
import turtle
t = turtle.Turtle()
t.color("red")
loop = 0
t.speed(0)

while loop <= 3:
    t.fd(100)
    t.rt(90)
    loop = loop + 1

time.sleep(1)
