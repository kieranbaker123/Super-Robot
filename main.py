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
    
    path = pathfinding.findPath(grid, start, goal)
    
    if path != None:
        path.pop(0) # remove start position
        robotDisplay.blinkPath(path, 2, grid, start, goal)

    robotDisplay.displayGrid(grid, start, goal)
    display.set_pixel(start[0], start[1], 9)        
    position = start
    faceDir = 'd'

    while position != goal:
        
        # update display
        robotDisplay.displayGrid(grid, start, goal)
        display.set_pixel(position[0], position[1], 9)
        
        # get new objects
        sensorData = optics.scan()
        newObjects = optics.checkObject(sensorData)
        
        # update map
        grid, isSame = objects.remap(position, faceDir, grid, newObjects)
        
        # if the grid changed, calculate new path
        if not isSame:
            path = pathfinding.findPath(grid, position, goal)
            
            # if the path exists, display it
            if path != None:
                path.pop(0)
                robotDisplay.blinkPath(path, 2, grid, position, goal)

        # check if path exists, if not skip rest of iteration
        if path == None:
            sleep(500)
            continue
        robotDisplay.showPath(path)
        
        # movement logic
        nextCell = path[0]
        relDir, globalDir = pathfinding.dirToCell(nextCell, position, faceDir)

        print('(main.py, main)\t\t\tCurrent cell:', position, 'Next Cell:', nextCell)
        print('(main.py, main)\t\t\tFacing:', faceDir, 'To face:', globalDir, 'Turn:', relDir)
        
        if relDir != 'f':
            driveRobot.turn(relDir)
        driveRobot.advance()
        
        faceDir = globalDir
        position = nextCell
        path.pop(0)

        print('===================================================================================')
        

if __name__ == '__main__':
    main()