import turtle
import time
l1 = 0

t = turtle.Turtle()

t.color("red")

while l1 <= 5:
  t.fd(100)
  t.rt(72)
  l1 = l1 + 1

time.sleep(1)
