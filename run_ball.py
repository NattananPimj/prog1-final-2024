import turtle
import ball
import random


# num_balls = 5
# turtle.speed(0)
# turtle.tracer(0)
# turtle.hideturtle()
# canvas_width = turtle.screensize()[0]
# canvas_height = turtle.screensize()[1]
# print(canvas_width, canvas_height)
# ball_radius = 0.05 * canvas_width
# turtle.colormode(255)
# xpos = []
# ypos = []
# vx = []
# vy = []
# ball_color = []
#
# # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
# for i in range(num_balls):
#     xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
#     ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
#     vx.append(10*random.uniform(-1.0, 1.0))
#     vy.append(10*random.uniform(-1.0, 1.0))
#     ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#
# def draw_border():
#     turtle.penup()
#     turtle.goto(-canvas_width, -canvas_height)
#     turtle.pensize(10)
#     turtle.pendown()
#     turtle.color((0, 0, 0))
#     for i in range(2):
#         turtle.forward(2*canvas_width)
#         turtle.left(90)
#         turtle.forward(2*canvas_height)
#         turtle.left(90)
#
# dt = 0.2 # time step
# while (True):
#     turtle.clear()
#     draw_border()
#     for i in range(num_balls):
#         ball.draw_ball(ball_color[i], ball_radius, xpos[i], ypos[i])
#         ball.move_ball(i, xpos, ypos, vx, vy, dt)
#         ball.update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
#     turtle.update()
#
# # hold the window; close it by clicking the window close 'x' mark
# turtle.done()

class BallSimulation:
    def __init__(self, num_balls):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.num_balls = num_balls
        self.ball_list = []
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.size = 0.05 * self.canvas_width
        for _ in range(num_balls):
            b = ball.Ball((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                          self.size, random.uniform(-1 * self.canvas_width + self.size, self.canvas_width - self.size),
                          random.uniform(-1 * self.canvas_height + self.size, self.canvas_height - self.size),
                          10*random.uniform(-1, 1), 10*random.uniform(-1, 1), self.canvas_width,
                          self.canvas_height, 0.2)
            self.ball_list.append(b)

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        while True:
            turtle.clear()
            self.draw_border()
            for b in self.ball_list:
                b.draw()
                b.move()
                b.bounce_wall()
            turtle.update()

simulation = BallSimulation(5)
simulation.run()