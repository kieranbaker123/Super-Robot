from microbit import *

# brightness values for each type of cell
BRIGHT_OPEN = 0
BRIGHT_WALL = 4
BRIGHT_START = 4
BRIGHT_GOAL = 4
BRIGHT_PATH = 6

'''
Displays the grid, start, and goal cells on the microbit
Parameters:
    grid, a grid of 0 and 1s
    start, tuple (x, y)
    goal, tuple (x, y)
'''
def displayGrid(grid, start, goal):
    display.clear()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                display.set_pixel(x, y, BRIGHT_WALL)
            if grid[y][x] == 0:
                display.set_pixel(x, y, BRIGHT_OPEN)

    sx, sy = start
    gx, gy = goal
    display.set_pixel(sx, sy, BRIGHT_START)
    display.set_pixel(gx, gy, BRIGHT_GOAL)

# lights up pixels
def showPath(path):
    for x, y in path:
        display.set_pixel(x, y, BRIGHT_PATH)

# draws the path
def animatePath(path):
    if not path:
        return
    for x, y in path:
        # skip the start and ending of the path to preserve their specific brightness marker
        if (x, y) != path[0] and (x, y) != path[-1]:
            display.set_pixel(x, y, BRIGHT_PATH)
            sleep(130)

# blinks the path 2 times  
def blinkPath(path, times=2, grid=None, start=None, goal=None):
    if not path:
        return
    for _ in range(times):
        showPath(path)
        sleep(350)
        if grid != None and start != None and goal != None:
            displayGrid(grid, start, goal)
        sleep(250)

        