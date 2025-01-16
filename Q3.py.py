import turtle

def draw_branch(t, branch_length, angle_left, angle_right, depth, reduction_factor):
    """
    Draws a fractal-like tree using turtle graphics.

    :param t: Turtle object
    :param branch_length: Current branch length
    :param angle_left: Angle for the left branch
    :param angle_right: Angle for the right branch
    :param depth: Remaining recursion depth
    :param reduction_factor: Factor to reduce branch length
    """
    if depth == 0:
        return

    # Set color for the trunk and branches
    if depth > 3:  # Trunk
        t.color("red")
    else:  # Branches
        t.color("green")

    # Draw the main branch
    t.forward(branch_length)

    # Draw the left branch
    t.left(angle_left)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Return to the main branch
    t.right(angle_left + angle_right)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Return to the original position and angle
    t.left(angle_right)
    t.backward(branch_length)

def fractal_tree():
    """
    Main function to generate the fractal tree pattern.
    """
    # Create the turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Fractal Tree")

    # Create the turtle object
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.left(90)  # Point the turtle upwards
    t.penup()
    t.goto(0, -250)  # Start at the bottom-center
    t.pendown()

    # Get user inputs
    print("Enter the parameters for the fractal tree:")
    angle_left = int(input("Left branch angle (degrees): "))
    angle_right = int(input("Right branch angle (degrees): "))
    starting_length = int(input("Starting branch length: "))
    depth = int(input("Recursion depth: "))
    reduction_factor = float(input("Branch length reduction factor (e.g., 0.7): "))

    # Draw the tree
    draw_branch(t, starting_length, angle_left, angle_right, depth, reduction_factor)

    # Close the window on click
    screen.mainloop()

# Run the program
if __name__ == "__main__":
    fractal_tree()
