import turtle
my_turtle_obj = turtle.Turtle()
window=turtle.Screen()
turtle.shape("turtle")
my_turtle_obj.speed(50)
my_turtle_obj.color("green")
i=1800
col=0
color_list = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
turtle.bgcolor("black")
my_turtle_obj.penup()
my_turtle_obj.goto(-855, 750)
my_turtle_obj.pendown()

while i > 0:
    my_turtle_obj.forward(i)
    my_turtle_obj.right(90)
    i-=10
    col+=1
    while col >=7:
        col=0
    my_turtle_obj.color(color_list[col])

my_turtle_obj.penup()
my_turtle_obj.color("white")
my_turtle_obj.goto(-865, 760)
my_turtle_obj.pendown()
i=1800
while i > 0:
    my_turtle_obj.forward(i)
    my_turtle_obj.right(90)
    i-=10

my_turtle_obj.penup()
my_turtle_obj.color("blue")
my_turtle_obj.goto(-860, 755)
my_turtle_obj.pendown()
i=1800
while i > 0:
    my_turtle_obj.forward(i)
    my_turtle_obj.right(90)
    i-=10

window.exitonclick()