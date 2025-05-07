import turtle

def drawTree(left_angle, right_angle, starting_branch_length, recursion_depth, branch_reduction_factor):
    screen = turtle.Screen()
    ttl = turtle.Turtle()

    ttl.left(90)
    ttl.penup()
    ttl.goto(0, -250)
    ttl.pendown()

    def branch(length, depth):
        # if depth == 0:
        #     return

        # ttl.forward(length)

        # # Save position and heading before branching
        # pos = ttl.pos()
        # angle = ttl.heading()

        # # Left branch
        # ttl.penup()
        # ttl.setpos(pos)
        # ttl.setheading(angle)
        # ttl.pendown()
        # ttl.left(left_angle)
        # branch(length * branch_reduction_factor, depth - 1)

        # # Right branch
        # ttl.penup()
        # ttl.setpos(pos)
        # ttl.setheading(angle)
        # ttl.pendown()
        # ttl.right(right_angle)
        # branch(length * branch_reduction_factor, depth - 1)

        # # Return to original state (optional here)
        # ttl.penup()
        # ttl.setpos(pos)
        # ttl.setheading(angle)
        # ttl.pendown()

        if depth > 0: 
            ttl.forward(length)
    
            ttl.right(right_angle) 
    
            # recursive call for 
            # the right subtree 
            branch(branch_reduction_factor * length, depth-1) 
            
            ttl.left(right_angle+left_angle) 
    
            # recursive call for 
            # the left subtree 
            branch(branch_reduction_factor * length, depth-1) 
            
            ttl.right(right_angle) 
            ttl.forward(-length) 

    branch(starting_branch_length, recursion_depth)
    turtle.done()

def main():
    left_angle = float(input("Enter left branch angle:"))
    right_angle = float(input("\nEnter right branch angle:"))
    starting_branch_length = float(input("\nEnter the length of first branch:"))
    recursion_depth = int(input("\nEnter no of branches to draw:"))
    branch_reduction_percentage = float(input("\nEnter the percentage of child branch to parent branch:"))

    branch_reduction_factor = float(branch_reduction_percentage/100)

    drawTree(left_angle, right_angle, starting_branch_length, recursion_depth, branch_reduction_factor)


if __name__=="__main__":
    main()