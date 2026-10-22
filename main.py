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

    robotDisplay.displayGrid(grid, start, goal)
    display.set_pixel(start[0], start[1], 9)        
    robotDisplay.showPath(path)
    position = start
    faceDir = 'd'

    while position != goal:
        # TODO: check for objects
        # TODO: update map and path
        # TODO: advance to next cell in path
        
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
