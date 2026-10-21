def getCoords(location):
    coords = {'l': [0,0], 'f': [0,0], 'r': [0,0]}
    if location[2] == 'd':
        coords['l'] = [location[0]+1, location[1]]
        coords['f'] = [location[0], location[1]+1]
        coords['r'] = [location[0]-1, location[1]]
    elif location[2] == 'r':
        coords['l'] = [location[0], location[1]-1]
        coords['f'] = [location[0]+1, location[1]]
        coords['r'] = [location[0], location[1]+1]
    elif location[2] == 'u':
        coords['l'] = [location[0]-1, location[1]]
        coords['f'] = [location[0], location[1]-1]
        coords['r'] = [location[0]+1, location[1]]
    elif location[2] == 'l':
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
            
    return cGrid, cGrid == grid
    


        

