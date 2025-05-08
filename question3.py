import turtle

def drawTree(left_angle, right_angle, starting_branch_length, recursion_depth, branch_reduction_factor):
    ttl = turtle.Turtle()
    ttl.left(90)
    ttl.penup()
    ttl.goto(0, -250)
    ttl.pendown()
    def branch(length, depth):
        if depth > 0: 
            ttl.forward(length)    
            ttl.right(right_angle)    
            # recursive call for 
            # the right subtree 
            branch(int(branch_reduction_factor * length), depth-1)            
            ttl.left(right_angle+left_angle)    
            # recursive call for 
            # the left subtree 
            branch(int(branch_reduction_factor * length), depth-1)            
            ttl.right(right_angle) 
            ttl.forward(-length) 

    branch(starting_branch_length, recursion_depth)
    turtle.done()

def main():
    # get an input and handle left branch angle
    left_angle = input("Enter left branch angle:")
    try:
        float_lt_ang = float(left_angle)
    except ValueError:
        ascii_values = [ord(char) for char in left_angle]
        float_lt_ang = float(sum(ascii_values))
        print("Your input is converted to float number", float_lt_ang)
        if type(float_lt_ang) != float:
            float_lt_ang = 0.0
            print("Your input is set as defalut value: ", float_lt_ang)

    # get an input and handle right branch angle
    right_angle = input("\nEnter right branch angle:")
    try:
        float_rt_ang = float(right_angle)
    except ValueError:
        ascii_values = [ord(char) for char in right_angle]
        float_rt_ang = float(sum(ascii_values))
        print("Your input is converted to float number: ", float_rt_ang)
        if type(float_rt_ang) != float:
            float_rt_ang = 0.0
            print("Your input is set as defalut value: ", float_rt_ang)

    # get an input and handle starting branch length
    starting_branch_length = input("\nEnter the length of first branch:")
    try:
        int_starting_length = int(starting_branch_length)
    except ValueError:
        try:
            float_starting_length = float(starting_branch_length)
            int_starting_length= int(round(float_starting_length,0))
            print("Your input is rounded to ", int_starting_length)
        except ValueError:
            ascii_values = [ord(char) for char in starting_branch_length]
            int_starting_length = round(sum(ascii_values),0)
            print("Your input is converted to integer number: ", int_starting_length)
            if type(int_starting_length) != int:
                int_starting_length = 0
                print("Your input is set as defalut value: ", int_starting_length)

    # get an input and handle depth of tree
    recursion_depth = input("\nEnter no of branches to draw:")
    try:
        int_recursion_depth = int(recursion_depth)
    except ValueError:
        try:
            float_recursion_depth = float(recursion_depth)
            int_recursion_depth= int(round(float_recursion_depth,0))
            print("Your input is rounded to ", int_recursion_depth)
        except ValueError:
            ascii_values = [ord(char) for char in recursion_depth]
            int_recursion_depth = round(sum(ascii_values),0)
            print("Your input is converted to integer number: ", int_recursion_depth)
            if type(int_recursion_depth) != int:
                int_recursion_depth = 0
                print("Your input is set as defalut value: ", int_recursion_depth)

    # get an input and handle branch reduction percentage
    branch_reduction_percentage = input("\nEnter the percentage of child branch with respect to parent branch:")
    try:
        float_branch_percent = float(branch_reduction_percentage)
    except ValueError:
        ascii_values = [ord(char) for char in branch_reduction_percentage]
        float_branch_percent = float(sum(ascii_values))
        print("Your input is converted to float number: ", float_branch_percent)
        if type(float_branch_percent) != float:
            float_branch_percent = 0.0
            print("Your input is set as defalut value: ", float_branch_percent)
            
    branch_reduction_factor = float(float_branch_percent/100)
    drawTree(float_lt_ang, float_rt_ang, int_starting_length, int_recursion_depth, branch_reduction_factor)


if __name__=="__main__":
    main()