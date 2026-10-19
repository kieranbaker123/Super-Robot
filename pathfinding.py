# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:09:31 2026

@author: gagej
"""

grid = [
       ['X', '1', '1', '0', '0'],
       ['0', '1', '0', '0', '1'],
       ['0', '0', '1', '0', '0'],
       ['1', '0', '0', '1', '0'],
       ['1', '1', '0', '0', 'S']
       ]

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


def backtrack(grid, backtrack_start):
    pass

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
    start_x, start_y = start
    goal_x, goal_y = goal
    
    # -1 corresponds to unmapped cell
    dist_map = [[-1] * width for _ in range(height)]
    dist_map[start_x][start_y] = 0
    queue_x = [start_x]
    queue_y = [start_y]
    head = 0
    
    while head < len(queue_x):
        x = queue_x[head]
        y = queue_y[head]
        head += 1
        
        if x == goal_x and y == goal_y:
            break
        
        for neighbor_x, neighbor_y in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            if neighbor_x < width and neighbor_x >= 0 and neighbor_y < height and neighbor_y >= 0 and grid[neighbor_y][neighbor_x] == 0 and dist_map[neighbor_y][neighbor_x] == -1:
                dist_map[neighbor_y][neighbor_x] = dist_map[y][x] + 1
                queue_x.append(neighbor_x)
                queue_y.append(neighbor_y)

    
    

def main():
    print('hi')
    parsed, start, goal = parse_map(grid)
    print(start)
    path = find_path(parsed, start, goal)
    
    
if __name__ == "__main__":
    main()