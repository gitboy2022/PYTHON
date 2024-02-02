# 1. Preparation
import turtle
import time
t = turtle.Turtle()
t.speed(0)

radius = 50
color1 = "blue"
color2 = "black"
color3 = "red"
color4 = "orange"
color5 = "green"

circle1Position = (-100, 0)
circle2Position = (10, 0)
circle3Position = (120, 0)
circle4Position = (-45, -60)
circle5Position = (65, -60)

# 2. Creating the circles

# 2a. Creating Circle 1
t.pu()
t.goto(circle1Position)
t.pd()
t.color(color1)
t.circle(radius)

# 2b. Creating Circle 2
t.pu()
t.goto(circle2Position)
t.pd()
t.color(color2)
t.circle(radius)

# 2c. Creating Circle 3
t.pu()
t.goto(circle3Position)
t.pd()
t.color(color3)
t.circle(radius)

# 2d. Creating Circle 4
t.pu()
t.goto(circle4Position)
t.pd()
t.color(color4)
t.circle(radius)

# 2e. Creating Circle 5
t.pu()
t.goto(circle5Position)
t.pd()
t.color(color5)
t.circle(radius)

# Finished
time.sleep(11)
