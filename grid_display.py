from microbit import *

bright_open = 1
bright_wall = 2
bright_start = 3
bright_goal = 4
bright_path = 5

def display_grid(grid, start, goal):
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
    