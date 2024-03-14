from codrone_edu.drone import Drone

drone: Drone = Drone()
drone.pair()
drone.takeoff()
# Drone goes right for 1 second with 50 power
b = 1
drone.set_roll(-30)
drone.move(b)
drone.set_roll(0)

drone.set_pitch(30)
drone.move(b)
drone.set_pitch(0)

drone.set_roll(30)
drone.move(b)
drone.set_roll(0)

drone.set_pitch(30)
drone.move(b)
drone.set_pitch(0)

drone.set_roll(30)
drone.move(b)
drone.set_roll(0)

drone.set_pitch(-30)
drone.move(b)
drone.set_pitch(0)

drone.set_roll(30)
drone.move(b)
drone.set_roll(0)

drone.set_pitch(-30)
drone.move(b)
drone.set_pitch(0)

drone.set_roll(-30)
drone.move(b)
drone.set_roll(0)

drone.set_pitch(-30)
drone.move(b)
drone.set_pitch(0)

drone.set_roll(-30)
drone.move(b)
drone.set_roll(0)

drone.set_pitch(30)
drone.move(b)
drone.set_pitch(0)

drone.land()
drone.close()
