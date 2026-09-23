
import turtle
import time
import math
# Create screen
wn = turtle.Screen()
wn.title("Analog Clock")
wn.bgcolor("black")
wn.setup(width=600, height=600)
# Main clock turtle
clock = turtle.Turtle()
clock.hideturtle()
clock.speed(0)
# Draw clock face
def draw_clock_face():
    # Outer circle
    clock.color("white")
    clock.penup()
    clock.goto(0, -200)
    clock.pendown()
    clock.circle(200)
    # Numbers 1 to 12
    clock.penup()
    for number in range(1, 13):
        angle = math.radians(90 - number * 30)
        x = 175 * math.cos(angle)
        y = 175 * math.sin(angle)
        clock.goto(x, y - 10)
        clock.write(
            number,
            align="center",
            font=("Arial", 14, "bold")
        )
    # Tick marks
    for i in range(60):
        angle = math.radians(90 - i * 6)
        outer_x = 195 * math.cos(angle)
        outer_y = 195 * math.sin(angle)
        if i % 5 == 0:
            inner_x = 180 * math.cos(angle)
            inner_y = 180 * math.sin(angle)
            width = 3
        else:
            inner_x = 187 * math.cos(angle)
            inner_y = 187 * math.sin(angle)
            width = 1
        clock.penup()
        clock.goto(outer_x, outer_y)
        clock.pendown()
        clock.pensize(width)
        clock.goto(inner_x, inner_y)
# Draw clock hands
def draw_hand(angle, length, color, width):
    hand = turtle.Turtle()
    hand.hideturtle()
    hand.speed(0)
    hand.color(color)
    hand.pensize(width)
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(90 - angle)
    hand.pendown()
    hand.forward(length)
# Main clock
while True:
    # Clear old clock
    clock.clear()
    # Draw face
    draw_clock_face()
    # Get current time
    now = time.localtime()
    sec = now.tm_sec
    minute = now.tm_min
    hour = now.tm_hour % 12
    # Calculate angles
    sec_angle = sec * 6
    min_angle = minute * 6 + sec * 0.1
    hour_angle = hour * 30 + minute * 0.5
    # Draw hands
    draw_hand(sec_angle, 175, "red", 1)
    draw_hand(min_angle, 145, "green", 3)
    draw_hand(hour_angle, 100, "blue", 5)
    # Center dot
    center = turtle.Turtle()
    center.hideturtle()
    center.penup()
    center.goto(0, -5)
    center.dot(10, "white")
    # Update every second
    time.sleep(1)