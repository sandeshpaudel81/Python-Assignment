import turtle

# Function to draw branch recursively
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
    # Getting an user inputs and handling exceptions

    # Left branch angle
    left_angle = input("Enter left branch angle (degrees): ")
    try:
        float_lt_ang = float(left_angle)
    except ValueError:
        ascii_values = [ord(char) for char in left_angle]
        float_lt_ang = float(sum(ascii_values))
        print("Your input is converted to float number", float_lt_ang)
        if type(float_lt_ang) != float:
            float_lt_ang = 0.0
            print("Your input is set as defalut value: ", float_lt_ang)

    # Right branch angle
    right_angle = input("Enter right branch angle (degrees): ")
    try:
        float_rt_ang = float(right_angle)
    except ValueError:
        ascii_values = [ord(char) for char in right_angle]
        float_rt_ang = float(sum(ascii_values))
        print("Your input is converted to float number: ", float_rt_ang)
        if type(float_rt_ang) != float:
            float_rt_ang = 0.0
            print("Your input is set as defalut value: ", float_rt_ang)

    # Branch Starting Length
    start_length = input("Enter starting branch length: ")
    try:
        int_starting_length = int(start_length)
    except ValueError:
        try:
            float_starting_length = float(start_length)
            int_starting_length= int(round(float_starting_length,0))
            print("Your input is rounded to ", int_starting_length)
        except ValueError:
            ascii_values = [ord(char) for char in start_length]
            int_starting_length = round(sum(ascii_values),0)
            print("Your input is converted to integer number: ", int_starting_length)
            if type(int_starting_length) != int:
                int_starting_length = 0
                print("Your input is set as defalut value: ", int_starting_length)

    # Recursion depth for number of branches
    depth = input("Enter recursion depth: ")
    try:
        int_recursion_depth = int(depth)
    except ValueError:
        try:
            float_recursion_depth = float(depth)
            int_recursion_depth= int(round(float_recursion_depth,0))
            print("Your input is rounded to ", int_recursion_depth)
        except ValueError:
            ascii_values = [ord(char) for char in depth]
            int_recursion_depth = round(sum(ascii_values),0)
            print("Your input is converted to integer number: ", int_recursion_depth)
            if type(int_recursion_depth) != int:
                int_recursion_depth = 0
                print("Your input is set as defalut value: ", int_recursion_depth)

    # Branch reduction factor with respect to parent branch
    reduction_factor = input("Enter branch length reduction factor (e.g., 0.7): ")
    try:
        float_branch_percent = float(reduction_factor)
    except ValueError:
        ascii_values = [ord(char) for char in reduction_factor]
        float_branch_percent = float(sum(ascii_values))
        print("Your input is converted to float number: ", float_branch_percent)
        if type(float_branch_percent) != float:
            float_branch_percent = 0.0
            print("Your input is set as defalut value: ", float_branch_percent)

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

    draw_branch(t, int_starting_length, float_lt_ang, float_rt_ang, int_recursion_depth, float_branch_percent)
    t.hideturtle()

    screen.mainloop()

if __name__ == "__main__":
    main()