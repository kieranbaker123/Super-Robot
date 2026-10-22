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
    
    iteration = 0

    while position != goal:
        iteration += 1
        print('(main.py, main)\t\t\tIteration', iteration)
        
        # TODO: test object checking
        
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
            print('(main.py, main)\t\t\tNew objects detected, Map updated')
            robotDisplay.displayGrid(grid, start, goal)
            display.set_pixel(position[0], position[1], 9)
            
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
        
        # the the robot
        if relDir != 'f':
            driveRobot.turn(relDir)
            
        # advance robot to next cell
        driveRobot.advance()
        
        # update location data
        faceDir = globalDir
        position = nextCell
        
        # remove completed cell from path
        path.pop(0)

        print('============================')
    
    print('(main.py, main)\t\t\tLoop terminated')
    if position == goal:
        print('(main.py, main)\t\t\tGoal reached')
        

if __name__ == '__main__':
    main()