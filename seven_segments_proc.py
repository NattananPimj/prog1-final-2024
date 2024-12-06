import turtle
import time


#
# def init(my_turtle, color):
#     turtle.speed(0)
#     turtle.tracer(0)
#     turtle.hideturtle()
#     turtle.colormode(255)
#
#     my_turtle.color(color)
#     my_turtle.penup()
#     my_turtle.setheading(0)
#     my_turtle.goto(0, 0)
#     my_turtle.pensize(10)
#
#
# def draw(my_turtle, digit):
#     if digit == 0:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.penup()
#
#     if digit == 1:
#         my_turtle.goto(50, 100)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 2:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.penup()
#
#     if digit == 3:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 4:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         my_turtle.forward(-100)
#         my_turtle.right(90)
#         my_turtle.penup()
#
#     if digit == 5:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 6:
#         draw(my_turtle, 5)
#         my_turtle.goto(-50, 0)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 7:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         draw(my_turtle, 1)
#
#     if digit == 8:
#         draw(my_turtle, 0)
#         my_turtle.goto(-50, 0)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.penup()
#
#     if digit == 9:
#         draw(my_turtle, 5)
#         my_turtle.goto(50, 100)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.penup()
#
# def clear(my_turtle):
#     my_turtle.clear()
#
# def my_delay(dt):
#     import time
#     start =  time.time()
#     while time.time() - start < dt:
#         pass
#
# Tom = turtle.Turtle()
# tom_color = (255, 0, 0)
# init(Tom, tom_color)
# delay_in_seconds = 0.2
# while True:
#     for i in range(0, 10):
#         clear(Tom)
#         draw(Tom, i)
#         my_delay(delay_in_seconds)
#         turtle.update()
#
# turtle.done()

class Number:
    def __init__(self, my_turtle: turtle.Turtle(), color, dt):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.my_turtle = my_turtle
        self.my_turtle.hideturtle()
        self.my_turtle.color(color)
        self.my_turtle.penup()
        self.my_turtle.setheading(0)
        self.my_turtle.goto(0, 0)
        self.my_turtle.pensize(10)
        self.digit = 10
        self.dt = dt

    def clear(self):
        self.my_turtle.clear()

    def delay(self):
        start = time.time()
        while time.time() - start < self.dt:
            pass

    def draw(self, digit):
        if digit == 0:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 1:
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 2:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 3:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 4:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 5:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 6:
            self.draw(5)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 7:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.draw(1)

        if digit == 8:
            self.draw(0)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 9:
            self.draw(5)
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

    def run(self):
        for i in range(self.digit):
            self.clear()
            self.draw(i)
            self.delay()
            turtle.update()
        turtle.done()

r = Number(turtle.Turtle(), (255, 0, 0), 0.2)
r.run()

