import turtle
import time

j = turtle.Turtle()
j.speed(0)

colors = ["red", "green", "purple", "indigo", "orange"]

for c in colors:
  j.color(c)
  j.fd(50)
  j.rt(144)

time.sleep(11)
