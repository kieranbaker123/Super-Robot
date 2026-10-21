from microbit import *

# brightness values for each type of cell
BRIGHT_OPEN = 1
BRIGHT_WALL = 2
BRIGHT_START = 3
BRIGHT_GOAL = 4
BRIGHT_PATH = 5

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
            if val == 1:
                display.set_pixel(x, y, BRIGHT_WALL)
            else:
                display.set_pixel(x, y, BRIGHT_OPEN)
    
    display.set_pixel(*start, BRIGHT_START)
    display.set_pixel(*goal, BRIGHT_GOAL)