# wave project
from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()
power = 30
for count in range(4):
    drone.set_throttle(power)
    drone.set_pitch(power)
    drone.move(1)
    drone.set_pitch(0)
    drone.set_throttle(-power)
    drone.set_pitch(power)
    drone.move(1)
    drone.set_pitch(0)
drone.land()
drone.close()