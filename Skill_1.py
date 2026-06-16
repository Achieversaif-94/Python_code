Lab -1:
To develop the intelligent agent robot programs in PyCharm, implement basic
programs like Variables and Data Types- Variables Used to store robot position
and goal. Lists (Used for Grid Environment - 2D Lists, Indexing, Nested lists)

# Intelligent Agent Robot Program
# Demonstrates Variables, Data Types, Lists, Indexing, and Nested Lists

# -------------------------------
# Variables and Data Types
# -------------------------------

# Robot starting position
robot_x = 0
robot_y = 0

# Goal position
goal_x = 3
goal_y = 3

# Robot name (string data type)
robot_name = "RoboAgent"

# Robot active status (boolean)
robot_active = True

# -------------------------------
# 2D Grid Environment (Nested List)
# -------------------------------

# Creating a 4x4 grid
grid = [
    ["R", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "G"]
]

# Display the grid
print("Initial Grid Environment:")
for row in grid:
    print(row)

# -------------------------------
# Accessing List Elements
# -------------------------------

print("\nRobot Position Symbol:", grid[0][0])
print("Goal Position Symbol:", grid[3][3])

# -------------------------------
# Moving the Robot
# -------------------------------

# Remove robot from old position
grid[robot_x][robot_y] = "."

# Update robot position
robot_x = 1
robot_y = 2

# Place robot in new position
grid[robot_x][robot_y] = "R"

# -------------------------------
# Display Updated Grid
# -------------------------------

print("\nUpdated Grid After Robot Movement:")
for row in grid:
    print(row)

# -------------------------------
# Checking Goal Condition
# -------------------------------

if robot_x == goal_x and robot_y == goal_y:
    print("\nGoal Reached!")
else:
    print("\nRobot has not reached the goal yet.")

# -------------------------------
# Robot Information
# -------------------------------

print("\nRobot Name:", robot_name)
print("Robot Active Status:", robot_active)
print("Current Robot Position:", (robot_x, robot_y))
print("Goal Position:", (goal_x, goal_y))

Output:

Initial Grid Environment:
['R', '.', '.', '.']
['.', '.', '.', '.']
['.', '.', '.', '.']
['.', '.', '.', 'G']

Robot Position Symbol: R
Goal Position Symbol: G

Updated Grid After Robot Movement:
['.', '.', '.', '.']
['.', '.', 'R', '.']
['.', '.', '.', '.']
['.', '.', '.', 'G']

Robot has not reached the goal yet.

Robot Name: RoboAgent
Robot Active Status: True
Current Robot Position: (1, 2)
Goal Position: (3, 3)