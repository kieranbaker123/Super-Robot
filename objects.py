'''
Gets the coordinates for adjacent cells, excluding behind the robot
Parameters:
    position, a tuple (x, y)
    faceDir, the facing direction 'l', 'r', 'u'
Returns:
    Dictionary of 'l', 'f', and 'r', with an (x, y) tuple for each
'''
def getAdjacentCoords(position, faceDir):
    coords = {'l': (0,0), 'f': (0,0), 'r': (0,0)}
    x, y = position
    if faceDir == 'd':
        coords['l'] = (x+1, y  )
        coords['f'] = (x  , y+1)
        coords['r'] = (x-1, y  )
    elif faceDir == 'r':
        coords['l'] = (x  , y-1)
        coords['f'] = (x+1, y  )
        coords['r'] = (x  , y+1)
    elif faceDir == 'u':
        coords['l'] = (x-1, y  )
        coords['f'] = (x  , y-1)
        coords['r'] = (x+1, y  )
    elif faceDir == 'l':
        coords['l'] = (x  , y+1)
        coords['f'] = (x-1, y  )
        coords['r'] = (x  , y-1)
    return coords

'''
Updates the grid with objects from the scan
Parameters:
    position, a tuple (x, y)
    faceDir, the facing direction 'l', 'r', 'u', 'd'
    grid, the grid representing open and blocked cells
    objects, the dictionary of 'l', 'f', and 'r', with 0 and 1s for open and blocked
Returns:
    Updated grid, if the grid is the same
'''
def remap(position, faceDir, grid, objects):
    cGrid = grid
    objectCoords = getAdjacentCoords(position, faceDir)
    same = True
    for direction in objectCoords.keys():
        coord = objectCoords[direction]
        if 0 <= coord[0] <= 4 and 0 <= coord[1] <= 4:
            cGrid[coord[1]][coord[0]] = objects[direction]
            if cGrid[coord[1]][coord[0]] == grid[coord[1]][coord[0]]:
                same = False
            
    return cGrid, same
    