# Brings in a turtle on the window screen
import turtle

wn = turtle.Screen()                        # Opens a window screen
wn.title("Happiness!")                      # Title of the window
wn.screensize(20000,2000)                  # Screensize of the window
wn.bgcolor("pink")                          # Color of the window

little_turtle = turtle.Turtle()             # Name of the first turtle
little_turtle.speed(50)                     # Speed of the turtle
little_turtle.pendown()                     # The pen is down when the turtle moves across the window
little_turtle.shape('square')               # Shape of the turtle is a square
height = 60                                 # Dimensions of the turtle
width = 60
depth = 20


big_turtle = turtle.Turtle()                # Name of the second turtle
big_turtle.speed(20)                        # Speed of the turtle
big_turtle.penup()                          # Pen is up on the window when the second turtle starts
big_turtle.shape('triangle')                # The shape of the second turtle is a triangle

# The colors I used in my code
colors = ['light blue', 'magenta', 'yellow', 'turquoise', 'HotPink1', 'PapayaWhip', 'OrangeRed2']

for row in range(7):                        # Loop for the rows of the first turtle
    little_turtle.color(colors[row])        # The turtles color for each row
    for col in range(7):                    # Loop for the columns
        for dep in range(7):                # Loop for the depth
            little_turtle.goto(col * width - 100 + dep * depth, row * height - 100 + dep * depth * 3)
            little_turtle.stamp()           # Stamps for the shape of the first turtle

for row in range(7):                        # Loop for the rows of the first turtle
    big_turtle.color(colors[row])           # The turtles color for each row
    for col in range(7):                    # Loop for the columns
        for dep in range(7):                # Loop for the depth
            big_turtle.goto(col * width - 100 + dep * depth, row * height - 100 + dep * depth * 3)
            big_turtle.stamp()              # Stamps for the shape of the second turtle


# End of the program when you click the window
wn.exitonclick()
