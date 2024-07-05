import turtle

# Create screen
screen = turtle.Screen()
screen.title("A Heart for You")
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.color("red")
t.speed(3)
t.pensize(3)

# Draw heart shape
def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

def write_message():
    t.penup()
    t.goto(-90, 150)
    t.color("black")
    t.write("I Love You!", font=("Arial", 24, "bold"))
    t.hideturtle()

draw_heart()
write_message()

# Keep the window open until clicked
screen.mainloop()
