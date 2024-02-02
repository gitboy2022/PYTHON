# - Rainbow
import turtle as t
import time
rainbow = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
size = [50, 60, 70, 80, 90, 100, 110]
t.speed(0)

t.pu()
t.goto(25, 0)
t.pd()
t.rt(270)

for i in range(7):
    t.color(rainbow[i])
    t.circle(size[i], 180)
    t.pu()
    t.circle(size[i], 180)
    t.rt(90)
    t.fd(10)
    t.lt(90)
    t.pd()

time.sleep(10)
