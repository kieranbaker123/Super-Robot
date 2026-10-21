from microbit import *

brightOpen = 1
brightWall = 2
brightStart = 3
brightGoal = 4
brightPath = 5

# assigns brightness value to each pixel based on cell value
def displayGrid(grid, start, goal):
    display.clear()
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if (x, y) == start:
                display.set_pixel(x, y, brightStart)
            elif (x, y) == goal:
                display.set_pixel(x, y, brightGoal)
            elif val == 1:
                display.set_pixel(x, y, brightWall)
            else:
                display.set_pixel(x, y, brightOpen)

# lights up pixels
def showPath(path):
    for x, y in path:
        display.set_pixel(x, y, brightPath)

# draws the path
def animatePath(path):
    if not path:
        return
    for x, y in path:
        # skip the start and ending of the path to preserve their specific brightness marker
        if (x, y) != path[0] and (x, y) != path[-1]:
            display.set_pixel(x, y, brightPath)
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

        