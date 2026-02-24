# Seil Tekinaeva
# 02/23/2025
# Module 5 Lab Activity 
# Solutions for Problems 1-5.

import turtle

# Problem 1
# Print "Hello World" 100 times

def problem1():
    # Loop runs 100 times
    for _ in range(100):
        print("Hello World")
problem1()

# Problem 2
# Given list: 12, 10, 32, 3, 66, 17, 42, 99, 20
# a) print each number on a new line
# b) print each number and its square on a new line

def problem2():
    nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

    print("Part (a): Each number on a new line")
    for n in nums:
        print(n)

    print("\nPart (b): Each number and its square")
    for n in nums:
        print(n, n * n)  
problem2()


# Problem 3
# Ask user for:
# - number of sides
# - length of side
# - line color
# - fill color
# Draw a regular polygon and fill it

def problem3():
    sides = int(input("Enter number of sides (example 3, 4, 5, 6): "))
    length = int(input("Enter length of each side (pixels): "))
    line_color = input("Enter line color (example 'burgundy', 'black', '#00FF00'): ")
    fill_color = input("Enter fill color (example 'beige', 'pink'): ")

    # Setup turtle screen and turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(6)

    # Set colors
    t.pencolor(line_color)
    t.fillcolor(fill_color)

    # Regular polygon turning angle:
    # 360 degrees divided by number of sides
    angle = 360 / sides

    # Draw and fill polygon
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()

    screen.mainloop()

problem3()

# Problem 4
# Iterate numbers 1 to 50
# - multiples of 3: print "Divisible by three"
# - multiples of 5: print "Divisible by five"
# - multiples of both 3 and 5: print "Divisible by both"
# otherwise print the number

def problem4():
    for num in range(1, 51):  # 1 through 50
        if num % 3 == 0 and num % 5 == 0:
            print("Divisible by both")
        elif num % 3 == 0:
            print("Divisible by three")
        elif num % 5 == 0:
            print("Divisible by five")
        else:
            print(num)
problem4()



# Problem 5
# Draw a picture using turtle
# Flower+ stem

import turtle

def problem5():
    screen = turtle.Screen()
    screen.title("Problem 5 - Turtle Drawing (Visible)")
    screen.setup(width=900, height=700) 
    screen.bgcolor("yellow")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    # Start in the center
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Floweer
    for i in range(60):
        t.pencolor(colors[i % len(colors)])
        t.circle(70)
        t.left(6)

    # Stem 
    t.pencolor("green")
    t.penup()
    t.goto(0, -20)
    t.setheading(-90)
    t.pendown()
    t.forward(220)

    # Leaf
    t.penup()
    t.goto(0, -150)
    t.setheading(200)
    t.pendown()

    t.fillcolor("black")
    t.begin_fill()
    t.circle(60, 80)
    t.left(100)
    t.circle(60, 80)
    t.end_fill()

    # Keep window open
    screen.mainloop()

problem5()
