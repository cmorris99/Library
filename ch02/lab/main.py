import turtle  # 1. import modules
import random

# Part A
window = turtle.Screen()  # 2. Create a screen
window.bgcolor("black")

michelangelo = turtle.Turtle()  # 3. Create two turtles
leonardo = turtle.Turtle()

michelangelo.color("orange")
leonardo.color("blue")

michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don't get lines
leonardo.up()

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)


# Race 1
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.forward(random.randrange(1, 101))
leonardo.forward(random.randrange(1, 101))

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)


# Race 2
for count in range(10):
    michelangelo.forward(random.randrange(1, 11))
    leonardo.forward(random.randrange(1, 11))

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)


# PART B - complete part B here

michelangelo.down()


# Triangle
number_of_sides = 3
turning_angle = 360 / number_of_sides
side_length = 50

for count in range(number_of_sides):
    michelangelo.forward(side_length)
    michelangelo.right(turning_angle)

michelangelo.clear()


# square
number_of_sides = 4
turning_angle = 360 / number_of_sides
side_length = 50

for count in range(number_of_sides):
    michelangelo.forward(side_length)
    michelangelo.right(turning_angle)

michelangelo.clear()


# hexagon
number_of_sides = 6
turning_angle = 360 / number_of_sides
side_length = 50

for count in range(number_of_sides):
    michelangelo.forward(side_length)
    michelangelo.right(turning_angle)

michelangelo.clear()

michelangelo.speed(4)
leonardo.speed(4)

# icosagon
number_of_sides = 20
turning_angle = 360 / number_of_sides
side_length = 20

for count in range(number_of_sides):
    michelangelo.forward(side_length)
    michelangelo.right(turning_angle)

michelangelo.clear()


# hectagon
number_of_sides = 100
turning_angle = 360 / number_of_sides
side_length = 5

for count in range(number_of_sides):
    michelangelo.forward(side_length)
    michelangelo.right(turning_angle)

michelangelo.clear()


# Circle
number_of_sides = 360
turning_angle = 360 / number_of_sides
side_length = 2

for count in range(number_of_sides):
    michelangelo.forward(side_length)
    michelangelo.right(turning_angle)

michelangelo.clear()


window.exitonclick()