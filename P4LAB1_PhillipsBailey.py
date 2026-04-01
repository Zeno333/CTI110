# Bailey Phillips
# P4LAB1_PhillipsBailey
# Draw a square and a triangle using turtle graphics,
# a while loop, and a for loop.

import turtle

# Set up screen
wn = turtle.Screen()
wn.bgcolor("lightblue")

# Set up turtle
t = turtle.Turtle()
t.pensize(3)
t.pencolor("green")
t.shape("turtle")
t.speed(3)

# Move turtle to starting position for square
t.penup()
t.goto(-50, -50)
t.pendown()

# Draw square with a while loop
count = 0
while count < 4:
    t.forward(100)
    t.left(90)
    count += 1

# Move to top-left corner of square for triangle
t.goto(-50, 50)

# Draw triangle with a for loop
for x in range(3):
    t.forward(100)
    t.left(120)

wn.mainloop()