from microbit import sleep
import robotbit_library as r

def driveRobot( a ):
    
    CM_PER_SECOND = 13.5
    CM_PER_TILE = 28.0
    TURN_TIME = 100
    
    leftMotor = 0x1
    rightMotor = 0x3
    
    leftPower = 50
    rightPower = 50
    
    if a == 'left':
        r.motor(leftMotor, -1 * leftPower)
        r.motor(rightMotor, 1 * rightPower)
        driveRobot("foreward")
        r.motor(leftMotor, 0)
        r.motor(rightMotor, 0)
    elif a == 'right':
        r.motor(leftMotor, 1 * leftPower)
        r.motor(rightMotor, -1 * rightPower)
        sleep( TURN_TIME )
        r.motor(leftMotor, 0)
        r.motor(rightMotor, 0)
        driveRobot("foreward")
    else:
        directions = {
            "forward": (1, 1),
            "backward": (-1, -1),
        }

        leftDirection, rightDirection = directions[a]
    
        r.motor(leftMotor, leftDirection * leftPower)
        r.motor(rightMotor, rightDirection * rightPower)
        sleep(int( CM_PER_TILE / CM_PER_SECOND ))
        r.motor(leftMotor, 0)
        r.motor(rightMotor, 0)