import turtle
import random

"""PUT YOUR FUNCTIONS HERE"""

# Create a turtle object
t = turtle.Turtle()

# Hide
# the turtle and set speed
t.speed(0)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
#pumpkin
def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
def draw_stem(t, x, y, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.setheading(180)
    t.right(90)  # Point upwards
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.right(90)
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.end_fill()
def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.setheading(120)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.right(-120)
        t.forward(width // 5)
        t.left(-120)
    t.end_fill()
#star
def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()
#sky

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(200, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)


draw_sky(t, 5)  # Draw 5 stars
draw_star(t, -100, 150, 30)  # Star in the sky
draw_star(t, 100, 180, 20)
draw_pumpkin(t,0, -100, 100)  # Draw the pumpkin
draw_stem(t,0, 98, 100)
draw_eye(t, -40, 20, 30)  # Left eye
draw_eye(t, 40, 20, 30)   # Right eye
draw_mouth(t, 40, -70, 100)  # Mouth

# Draw three jack-o-lanterns
draw_pumpkin(t, -150, -150, 100)
draw_eye(t, -240, -205, 30)  # Left eye
draw_eye(t, -200, -205, 30)  # Right eye
draw_mouth(t, -190, -260, 80)  # Mouth

draw_pumpkin(t, 0, -150, 80)
draw_eye(t, -80, -190, 25)
draw_eye(t, -40, -190, 25)
draw_mouth(t, -50, -230, 60)

draw_pumpkin(t, 150, -150, 100)
draw_eye(t, 40, -190, 30)
draw_eye(t, 120, -190, 30)
draw_mouth(t, 110, -250, 80)


# Close the turtle graphics window when clicked
turtle.exitonclick()