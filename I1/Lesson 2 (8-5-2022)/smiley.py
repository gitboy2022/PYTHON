
# start

# smiley

# setup
import turtle
import time
star = 4
t = turtle.Turtle()
a = 0
t.color("red")
t.speed(1)

# star 1
t.pu()
t.goto(-100, 100)
t.pd()
while a <= star:
    t.fd(50)
    t.rt(144)
    a = a + 1
t.fd(50)
a = 0

# star 2
t.pu()
t.goto(100, 100)
t.pd()
while a <= star:
    t.fd(50)
    t.rt(144)
    a = a + 1
t.fd(50)
a = 0

# half circle
t.pu()
t.goto(-25, 0)
t.pd()
t.rt(90)
t.circle(50, 180)

# final
time.sleep(1)

# done

# end
