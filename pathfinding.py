# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:09:31 2026

@author: gagej
"""

import math

'''
takes in a map string, map width, and map height and converts it to a 2d array
'''
def parseString(gridString, width, height):
    grid = [[] for _ in range(height)]
    index = 0
    
    for i in range(height):
        for j in range(width):
            grid[i].append(gridString[index])
            index += 1
    return grid

'''
takes in a grid and returns a converted grid with open (0) and closed (1) cells
'0' = 0
'S' = 0
'X' = 0
'1' = 1
'''
def parseMap(grid):
    width = len(grid[0])
    height = len(grid)
    parsed = [[0] * width for _ in range(height)]
    start = None
    goal = None
        
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '0':
                parsed[y][x] = 0
            elif grid[y][x] == '1':
                parsed[y][x] = 1
            elif grid[y][x] == 'S':
                parsed[y][x] = 0
                start = (x, y)
            elif grid[y][x] == 'X':
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
    
    if grid[y][x] == -1:
        return None
    
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
    0 - open
    1 - blocked
start:
    tuple (x, y)
goal:
    tuple (x, y)
'''
def findPath(grid, start, goal):
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

    path = backtrack(distMap, goal)
                     
    if path == None:
        return None
    
    path.reverse()
    return path


'''
Gets the relative direction to an adjacent cell
Parameters:
    cellPosition, (x, y) of the adjacent cell
    robotPosition, (x, y) of the robot
    faceDir, facing direction of the robot, 'u', 'r', 'd', or 'l'
Returns:
    the direction of the cell, 'f', 'r', 'l', 'b' for forward, right, left, and back
'''
def relativeDirToCell(cellPosition, robotPosition, faceDir):
    cellX, cellY = cellPosition
    robotX, robotY = robotPosition
    
    faceX, faceY = faceDirToFaceCoords(faceDir)
    
    dirX = cellX - robotX
    dirY = cellY - robotY
    
    dot = faceX * dirX + faceY * dirY
    det = faceX * dirY - faceY * dirX
    
    ccwRot = math.atan2(-det, dot) * 2 / math.pi # linear algebra stuff that i googled <3
    
    
    if ccwRot == -2 or ccwRot == 2:
        relDir = 'b'
    elif ccwRot == -1:
        relDir = 'r'
    elif ccwRot == 0:
        relDir = 'f'
    elif ccwRot == 1:
        relDir = 'l'
    
    return relDir
    
'''
Converts a character faceDir to an (x,y) tuple
Parameters:
    faceDir, 'u', 'r', 'd', or 'l'
Returns:
    (faceX, faceY) tuple of the relative coordinates of the adjacent cell that the robot is facing
'''
def faceDirToFaceCoords(faceDir):
    if faceDir == 'u':
        faceX = 0
        faceY = -1
    elif faceDir == 'r':
        faceX = 1
        faceY = 0
    elif faceDir == 'd':
        faceX = 0
        faceY = 1
    elif faceDir == 'l':
        faceX = -1
        faceY = 0
    
    return (faceX, faceY)

    
    