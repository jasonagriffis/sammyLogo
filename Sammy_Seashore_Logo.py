# -------------------------------------------------------------------------------
# Program:     Sammy_Seashore_Logo.py
# Project:     Creating a logo with turtle
# Name:        Jason Griffis
# Use Turtle graphics to create a logo for Sammy's Seashore Supplies
# -------------------------------------------------------------------------------

# Import the function we need for the turtle and also random for some flair
import turtle
import random

# Create our turtle and set some parameters and initially have the turtle be the classic pointer
sammy = turtle.Turtle()
sammy.shape("classic")
sammy.speed(30)

# Set up our screen, color, and size
wn = turtle.Screen()
wn.bgcolor("#825AC3")  # "Royal Purple"
wn.setup(800, 600)


# Defining a function for the turtle to make corners
def corner(this):
    for i in range(0, 6):
        this.left(15)
        this.forward(2)


# Defining another function that utilizes the above function to create a filled box with lettering inside it.
# The first argument is passed as the turtle, in our case this becomes sammy
# x1, y1, x2, y2 all refer to the coordinates of our turtle on the screen as defined in the function call
def box(this, x1, y1, x2, y2, letter):
    this.showturtle()
    this.penup()
    this.goto(x1, y1)
    this.pendown()
    this.color("#290628")  # "Dark Purple" for the pointer color
    this.fillcolor("#290628")  # "Dark Purple" for the fill color
    this.begin_fill()  # This has to be called just before drawing a shape that has to be filled
    for i in range(0, 4):
        this.forward(40)  # Drawing our little boxes by calling the "corner" function at 40px
        corner(this)
    this.end_fill()
    this.penup()
    this.goto(x2, y2)
    this.color("#F1DEDE")  # Set the letter fill color to "Misty Rose"
    this.write(letter, font=('Stencil', 28, 'bold'))  # Handy little call to actually write text
    # It uses a variable, and font defined by name, size, and type.
    this.hideturtle()


# Here we have the calls to the function "box" to make a box with the letter S in each one
box(sammy, -60, 30, -50, 35, "S")  # The first box
box(sammy, 5, 30, 14, 35, "S")  # The second box
box(sammy, 70, 30, 79, 35, "S")  # The third and final box

sammy.hideturtle()
sammy.color("#290628")  # "Dark Purple" for a slight reduction of the importance of this text
sammy.goto(15, -30)  # Manually centering the text
sammy.write("Beach Equipment Rentals", align="center", font=('Arial', 24, "bold"))
sammy.goto(15, -90)  # Reentering
sammy.write("By", align="center", font=('Arial', 24, "bold"))
sammy.color("#6CD4FF")  # "Baby Blue" for the full name of the rental store to make it pop
sammy.goto(15, -150)  # Final centering of the text
sammy.write("Sammy's Seashore Supplies", align="center", font=('Arial Rounded MT Bold', 24, "bold"))

# Setting up another turtle and using it as an icon
icon = turtle.Turtle()
icon.penup()
icon.left(90)
icon.goto(26, 105)
icon.shape("turtle")

# Display the turtle and make it flash until it settles on the final color
for x in range(0, 100):
    icon.color("#%06x" % random.randint(0, 2 ** 24 - 1))  # Uses random to flash through 100 random colors
icon.color("#6CD4FF")  # Set icon turtle color to "Baby Blue" to tie into the company name

wn.mainloop()
