"""
Question A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, 
LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 
RIGHT 2 ¡­ The numbers after the direction are steps. Please write a program to compute the distance from current 
position after a sequence of movement and original point. If the distance is a float, then just print the nearest 
integer. Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the 
output of the program should be: 2
"""

import math

# Initialize starting coordinates
x, y = 0, 0

while True:
    try:
        move = input().strip()
        if not move:
            break  # Stop when no input is given

        direction, steps = move.split()
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    except:
        break

# Calculate the Euclidean distance from the origin
distance = math.sqrt(x**2 + y**2)

# Print the nearest integer
print(round(distance))
