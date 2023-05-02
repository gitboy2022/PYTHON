import turtle as t


def up():
    t.seth(90)
    t.fd(100)


def down():
    t.seth(270)
    t.fd(100)


def left():
    t.seth(180)
    t.fd(100)


def right():
    t.seth(0)
    t.fd(100)


t.listen()

t.onkey(up, "Up")
t.onkey(left, "Left")
t.onkey(down, "Down")
t.onkey(right, "Right")

t.mainloop()
