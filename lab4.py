from codrone_edu.drone import Drone

drone: Drone = Drone()
drone.pair()
drone.takeoff()

# Drone goes right for 1 second with 50 power
a = -30
b = 1
c = 30

drone.set_roll(a)
drone.move(b)
drone.set_roll(0)

for count in range(2):
    drone.set_pitch(c)
    drone.move(b)
    drone.set_pitch(0)

    drone.set_roll(c)
    drone.move(b)
    drone.set_roll(0)

drone.set_pitch(a)
drone.move(b)
drone.set_pitch(0)

drone.set_roll(c)
drone.move(b)
drone.set_roll(0)

for count in range(2):
    drone.set_pitch(a)
    drone.move(b)
    drone.set_pitch(0)

    drone.set_roll(a)
    drone.move(b)
    drone.set_roll(0)

drone.set_pitch(c)
drone.move(b)
drone.set_pitch(0)

drone.land()
drone.close()
