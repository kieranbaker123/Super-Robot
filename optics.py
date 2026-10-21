from microbit import *
import robotbit_library as r
from machine import time_pulse_us
from time import sleep_us

S1 = 0x1

r.setup()
TIME_OUT = 100000

'''
Gets data from the ultrasonic sensor
Parameters:
    tp, the trigger pin of the sensor
    ep, the echo pin of the sensor
Return:
    Ultrasonic sensor data
'''
def getUltrasonicSensorData(tp, ep):
    # tp is the trigger pin and ep is the echo pin
    ep.read_digital()  # clear echo
    tp.write_digital(1)  # Send a 10 microSec pulse
    sleep_us(10)  # wait 10 microSec
    tp.write_digital(0)  # Send pulse low
    ep.read_digital()  # clear echo signal - This is needed for a
    # pingSensor
    ts = time_pulse_us(ep, 1, TIME_OUT)  # Wait for echo or time out
    if ts > 0:
        ts = ts * 17 // 100  # if system did not timeout, then send
        # back a scaled value
    return ts  # Return timeout error as a negative number (-1)

'''
Gets ultrasonic sensor data for adjacent cells
Returns:
    Dictionary of 'l', 'f', and 'r', with corresponding ultrasonic sensor data
'''
def scan():
    angleSetting = {0: 0, 220: 0, 105: 0}
    for angle in angleSetting.keys():
        r.servo(S1, angle)
        sleep(1000)
        angleSetting[angle] = getUltrasonicSensorData(pin1, pin1)
    return {"l": angleSetting[220], "f": angleSetting[105], "r": angleSetting[0]}

'''
Checks for objects in the adjacent cells given sensor data
Parameters:
    sensorData, dictionary of 'l', 'f', and 'r', with 1 as blocked and 0 as open
'''
def checkObject(sensorData):
    objects = {"l": -1, "f": -1, "r": -1}
    for direction in sensorData.keys():
        if 100 < sensorData[direction] < 300:
            objects[direction] = 1
        else:
            objects[direction] = 0
    return objects
    