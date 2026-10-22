from microbit import sleep
import robotbit_library as r
from math import fabs

CM_PER_SECOND = 13.5
CM_PER_TILE = 28.0
TURN_TIME = 500

MOTOR_LEFT = 0x1
MOTOR_RIGHT = 0x3

POWER_LEFT = 50
POWER_RIGHT = 50

'''
Turns the robot left or right
Parameters:
    direction, the direction to turn. Either 'l' for left or 'r' for right.
'''
def turn(direction):
    if direction == 'l':
        r.motor(MOTOR_LEFT, POWER_LEFT)
        r.motor(MOTOR_RIGHT, POWER_RIGHT)
        sleep( TURN_TIME )
        r.all_stop()
    elif direction == 'r':
        r.motor(MOTOR_LEFT, -POWER_LEFT)
        r.motor(MOTOR_RIGHT, -POWER_RIGHT)
        sleep( TURN_TIME )
        r.all_stop()
        
        
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
        