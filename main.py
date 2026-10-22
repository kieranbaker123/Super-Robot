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
        if start in path:
            path.remove(start)
        robotDisplay.blinkPath(path, 2, grid, start, goal)

    robotDisplay.displayGrid(grid, start, goal)
    display.set_pixel(start[0], start[1], 9)
    
    position = start
    faceDir = 'd'
    
    iteration = 0

    while position != goal:
        if button_b.was_pressed():
            break
        
        iteration += 1
        print('(main.py, main)\t\t\tIteration', iteration)
        
        robotDisplay.displayGrid(grid, start, goal)
        display.set_pixel(position[0], position[1], 9)
        
        sensorData = optics.scan()
        print('(main.py, main)\t\t\tSensor Data:', sensorData)
        newObjects = optics.checkObject(sensorData)
        print('(main.py, main)\t\t\tObjects:', newObjects)
        
        grid, isSame = objects.remap(position, faceDir, grid, newObjects)
        
        if not isSame:
            print('(main.py, main)\t\t\tNew objects detected, Map updated')
            robotDisplay.displayGrid(grid, start, goal)
            display.set_pixel(position[0], position[1], 9)
            
            path = pathfinding.findPath(grid, position, goal)
            
            if path != None:
                if position in path:
                    path.remove(position)
                robotDisplay.blinkPath(path, 2, grid, position, goal)

        if path == None:
            print('(main.py, main)\t\t\tPath does not exist')
            sleep(500)
            print('============================')  
            continue
        robotDisplay.showPath(path)
        
        nextCell = path[0]
        
        print('(main.py, main)\t\t\tCurrent cell:', position, 'Next Cell:', nextCell)
        
        relDir, globalDir = pathfinding.dirToCell(nextCell, position, faceDir)

        print('(main.py, main)\t\t\tFacing:', faceDir, 'To face:', globalDir, 'Turn:', relDir)
        
        if relDir != 'f':
            driveRobot.turn(relDir)
            
        driveRobot.advance()
        
        faceDir = globalDir
        position = nextCell
        
        path.pop(0)

        print('============================')

    print('(main.py, main)\t\t\tLoop terminated')

    if position == goal:
        print('(main.py, main)\t\t\tGoal reached')

if __name__ == '__main__':
    while True:
        if button_a.was_pressed():
            main()