import turtle
turtle.speed(0)

def circle(x, y):
    r = 10
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)

turtle.onscreenclick(circle)

turtle.mainloop()