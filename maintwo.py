import turtle

root = turtle.Screen()

mouse_cord = None

# Function to capture mouse click and move the turtle in 2D
def mouse_pos(x, y):
    global mouse_cord
    mouse_cord = (x, y)  # Update mouse coordinates on click
    
    print(f"Mouse clicked at: {mouse_cord}")

    # Get the current turtle position
    turtle_x = turtle.xcor()
    turtle_y = turtle.ycor()

    # Calculate the difference in the x and y directions
    x_diff = mouse_cord[0] - turtle_x
    y_diff = mouse_cord[1] - turtle_y

    # Move the turtle towards the mouse click in the x direction
    if x_diff > 0:
        turtle.setheading(0)  # Point the turtle to the right (East)
        turtle.forward(x_diff)  # Move forward in the x direction
    elif x_diff < 0:
        turtle.setheading(180)  # Point the turtle to the left (West)
        turtle.forward(-x_diff)  # Move backward in the x direction

    # Move the turtle towards the mouse click in the y direction
    if y_diff > 0:
        turtle.setheading(90)  # Point the turtle upwards (North)
        turtle.forward(y_diff)  # Move forward in the y direction
    elif y_diff < 0:
        turtle.setheading(270)  # Point the turtle downwards (South)
        turtle.forward(-y_diff)  # Move backward in the y direction

# Register the mouse click event
root.onscreenclick(mouse_pos)

# Start the turtle main event loop to listen for mouse clicks
turtle.mainloop()
