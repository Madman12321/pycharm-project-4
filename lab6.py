from codrone_edu.drone import *

drone = Drone()
drone.pair()

def play_five_notes(duration):
    drone.drone_buzzer(Note.D5, duration)
    drone.drone_buzzer(Note.E5, duration)
    drone.drone_buzzer(Note.C5, duration * 1)
    drone.drone_buzzer(Note.C4, duration)
    drone.drone_buzzer(Note.G4, duration * 2)


play_five_notes(545)

drone.takeoff()

def pentagon(length):
    power = 25
    for side in range(5):
        drone.set_pitch(power)
        drone.move(length)
        drone.set_pitch(0)
        drone.turn_right(72)



pentagon(1)
drone.turn_right(90)
drone.move(1)
drone.land()
play_five_notes(545)

drone.close()
