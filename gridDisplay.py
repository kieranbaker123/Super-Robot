from microbit import *

bright_open = 1
bright_wall = 2
bright_start = 3
bright_goal = 4
bright_path = 5

'''
Displays the grid, start, and goal cells on the microbit
Parameters:
    grid, a grid of 0 and 1s
    start, tuple (x, y)
    goal, tuple (x, y)
'''
def displayGrid(grid, start, goal):
    display.clear()
    for y, row in enumerate(grid):
        for x, val in enumerate(grid):
            if (x,y) == start:
                display.set_pixel(x, y, bright_start)
            elif (x,y) == goal:
                display.set_pixel(x, y, bright_goal)
            elif val == 1:
                display.set_pixel(x, y, bright_wall)
            else:
                display.set_pixel(x, y, bright_open)
    