from microbit import sleep
import robotbit_library as r
from math import fabs
from microbit import *

CM_PER_SECOND = 25.67
CM_PER_TILE = 28.0
RIGHT_TURN_TIME = 385
LEFT_TURN_TIME = 407

MOTOR_LEFT = 0x1
MOTOR_RIGHT = 0x3

POWER_LEFT = 47
POWER_RIGHT = 50

'''
Turns the robot left or right
Parameters:
    direction, the direction to turn. Either 'l' for left, 'r' for right, or 'b' for turning around.
'''
def turn(direction):
    if direction == 'r':
        r.motor(MOTOR_LEFT, POWER_LEFT)
        r.motor(MOTOR_RIGHT, POWER_RIGHT)
        sleep( RIGHT_TURN_TIME )
        r.all_stop()
        print('(turn) Turned right')
    elif direction == 'l':
        r.motor(MOTOR_LEFT, -POWER_LEFT)
        r.motor(MOTOR_RIGHT, -POWER_RIGHT)
        sleep( LEFT_TURN_TIME )
        r.all_stop()
        print('(turn) Turned left')
    elif direction == 'b':
        r.motor(MOTOR_LEFT, -POWER_LEFT)
        r.motor(MOTOR_RIGHT, -POWER_RIGHT)
        sleep( LEFT_TURN_TIME * 2 )
        r.all_stop()
        print('(turn) Turned around')
        
'''
Advances the robot forward or backward
Parameters:
    cells, the number of cells to move. Positive denotes forward, negative denotes backward. Default 1
'''
def advance(cells=1):
    direction: tuple # direction has scope of the function
    
    if cells < 0:
        direction = (1, -1) # backwards
    elif cells > 0:
        direction = (-1, 1) # forwards
    else:
        return # cells is 0, do nothing
    
    duration = fabs(cells) * int( CM_PER_TILE / CM_PER_SECOND * 1000 )
    
    r.motor(MOTOR_LEFT, direction[0] * POWER_LEFT)
    r.motor(MOTOR_RIGHT, direction[1] * POWER_RIGHT)
    sleep(duration)
    r.all_stop()
    
    print('(advance) Advanced', cells, 'cells')
