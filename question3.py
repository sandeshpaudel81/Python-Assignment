import turtle

def draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return
    # Determine color based on depth
    current_color = "brown" if depth == 5 else "green"

    # Save the previous color to restore after drawing
    previous_color = t.pencolor()
    t.color(current_color)

    t.forward(branch_length)
    old_pen_size = t.pensize()
    new_pen_size = t.pensize() * 0.7
    t.pensize(new_pen_size)
    t.left(left_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.right(left_angle + right_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.left(right_angle)
    t.backward(branch_length)

    # Restore previous color
    t.color(previous_color)
    t.pensize(old_pen_size)


def main():
    # User inputs
    left_angle = float(input("Enter left branch angle (degrees): "))
    right_angle = float(input("Enter right branch angle (degrees): "))
    start_length = float(input("Enter starting branch length: "))
    depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

    # Turtle setup
    screen = turtle.Screen()
    screen.title("Recursive Tree")
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Point the turtle upward
    t.color("brown")
    t.pensize(5)

    # Position the turtle
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_branch(t, start_length, left_angle, right_angle, depth, reduction_factor)
    t.hideturtle()

    screen.mainloop()

if __name__ == "__main__":
    main()