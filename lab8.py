from codrone_edu.drone import *
import time

THROTTLE_POWER = 30
def set_altitude(altitude):
    print(THROTTLE_POWER)
    print(altitude)
    height = drone.get_height()
    print(height)
    if altitude <= height:
        sign = -1
    else:
        sign = 1

    drone.set_throttle(sign * THROTTLE_POWER)

    drone.move(1)

    while sign * altitude > sign * height:
        height = drone.get_height()
        print(height)
        time.sleep(0.1)


drone = Drone()
drone.pair()
drone.set_initial_pressure()

try:
    drone.takeoff()
    drone.hover(2)
    set_altitude(40)
    print('Final Height =',drone.height_from_pressure())
    drone.hover(2)
    set_altitude(150)
    print('Final Height =',drone.height_from_pressure())
    drone.hover(3)
except Exception as e:
    print(e)
drone.land()
drone.close()