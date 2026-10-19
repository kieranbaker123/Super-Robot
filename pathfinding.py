# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:09:31 2026

@author: gagej
"""

def parse_map(grid):
    width = len(grid[0])
    height = len(grid)
    parsed = [[0] * width for _ in range(height)]
    start = (0, 0)
    goal = (0, 0)
        
    for y in range(height):
        for x in range(width):
            match grid[y][x]:
                case '0':
                    parsed[y][x] = 0
                case '1':
                    parsed[y][x] = 1
                case 'S':
                    parsed[y][x] = 0
                    start = (x, y)
                case 'X':
                    parsed[y][x] = 0
                    goal = (x, y)
                
    return parsed, start, goal


'''
    returns list of tuples that backtracks from an end point on the grid to a 0 value following consecutive decreasing values
'''
def backtrack(grid, end):
    width = len(grid[0])
    height = len(grid)
    x, y = end
    path = [end]
    
    while True:
        if grid[y][x] == 0:
            return path
        
        for neighborX, neighborY in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            if neighborX < width and neighborX >= 0 and neighborY < height and neighborY >= 0 and grid[neighborY][neighborX] == grid[y][x] - 1:
                x = neighborX
                y = neighborY
                path.append((x, y))
                break
            
    return path

'''
returns path from start to goal in list of position tuples

grid in format:
    '0' - open
    '1' - blocked
    'S' - start
    'X' - goal
start:
    tuple (x, y)
goal:
    tuple (x, y)
'''
def find_path(grid, start, goal):
    width = len(grid[0])
    height = len(grid)
    startX, startY = start
    goalX, goalY = goal
    
    # -1 corresponds to unmapped cell
    distMap = [[-1] * width for _ in range(height)]
    distMap[startX][startY] = 0
    queueX = [startX]
    queueY = [startY]
    head = 0
    
    while head < len(queueX):
        x = queueX[head]
        y = queueY[head]
        head += 1
        
        if x == goalX and y == goalY:
            break
        
        for neighborX, neighborY in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            if neighborX < width and neighborX >= 0 and neighborY < height and neighborY >= 0 and grid[neighborY][neighborX] == 0 and distMap[neighborY][neighborX] == -1:
                distMap[neighborY][neighborX] = distMap[y][x] + 1
                queueX.append(neighborX)
                queueY.append(neighborY)

    # if no path exists
    if distMap[goalY][goalX] == -1:
        return None

    path = backtrack(distMap, goal)
    path.reverse()
    return path