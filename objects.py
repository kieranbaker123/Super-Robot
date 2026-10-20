def getCoords(location):
    coords = {'l': [0,0], 'f': [0,0], 'r': [0,0]}
    match location[2]:
        case 'down':
            coords['l'] = [location[0]+1, location[1]]
            coords['f'] = [location[0], location[1]+1]
            coords['r'] = [location[0]-1, location[1]]
        case 'right':
            coords['l'] = [location[0], location[1]-1]
            coords['f'] = [location[0]+1, location[1]]
            coords['r'] = [location[0], location[1]+1]
        case 'up':
            coords['l'] = [location[0]-1, location[1]]
            coords['f'] = [location[0], location[1]-1]
            coords['r'] = [location[0]+1, location[1]]
        case 'left':
            coords['l'] = [location[0], location[1]+1]
            coords['f'] = [location[0]-1, location[1]]
            coords['r'] = [location[0], location[1]-1]
    return coords


def remap(location, grid, objects):
    cGrid = grid
    objectCoords = getCoords(location)
    for d in objectCoords.keys():
        c = objectCoords[d]
        if 0 <= c[0] <= 4 and 0 <= c[1] <= 4:
            cGrid[c[0]][c[1]] = objects[c[0]][c[1]]
            
    if cGrid != grid:
        return cGrid, False
    else:
        return cGrid, True


        

