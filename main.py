# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:09:36 2026

@author: gagej
"""
from microbit import *
import robotDisplay
import driveRobot
import objects
import optics
import pathfinding

SECTOR_MAP = "S01000010001110000101000X"

def main():
    grid_chars = pathfinding.parseString(SECTOR_MAP, 5, 5)
    grid, start, goal = pathfinding.parseMap(grid_chars)
    for row in grid:
        print(row)
    print()
    
    path = pathfinding.findPath(grid, start, goal)

    robotDisplay.displayGrid(grid, start, goal)
    display.set_pixel(start[0], start[1], 9)        
    robotDisplay.showPath(path)
    position = start
    faceDir = 'd'

    while position != goal:
        x, y = position
        
        robotDisplay.displayGrid(grid, start, goal)

        if path != None:
            robotDisplay.showPath(path)
        display.set_pixel(x, y, 9)    
        
        sensorData = optics.scan()
        adjObjects = optics.checkObject(sensorData)
        grid, isSame = objects.remap(position, faceDir, grid, adjObjects)

        if not isSame:
            path = pathfinding.findPath(grid, position, goal)

        if path == None:
            continue

        if position == path[0]:
            path.pop(0)
        
        nextX, nextY = path[0]

        print(position)

        diffX = nextX - x
        diffY = nextY - y

        moveDir = 'x'
        
        if diffX == 1:
            moveDir = 'r'
        elif diffX == -1:
            moveDir = 'l'
        elif diffY == 1:
            moveDir = 'd'
        elif diffY == -1:
            moveDir = 'u'

        print(moveDir)
        print(path[0])
        
        moveDirDec = convertDirCharToDec(moveDir)
        faceDirDec = convertDirCharToDec(faceDir)
        
        diff = moveDirDec - faceDirDec

        if diff == 1:
            driveRobot.turn('r')
        elif diff == 2:
            driveRobot.turn('r')
            driveRobot.turn('r')
        elif diff == 3:
            driveRobot.turn('l')
        elif diff == -1:
            driveRobot.turn('l')
        elif diff == -2:
            driveRobot.turn('l')
            driveRobot.turn('l')
        elif diff == -3:
            driveRobot.turn('r')
            
        driveRobot.advance()

        position = (nextX, nextY)
        faceDir = moveDir
        
        

def convertDirCharToDec(direction):
    if direction == 'u':
        return 0
    if direction == 'r':
        return 1
    if direction == 'd':
        return 2
    if direction == 'l':
        return 3

if __name__ == '__main__':
    main()