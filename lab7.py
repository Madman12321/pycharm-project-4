from codrone_edu.drone import *


def test_obstacle_sensor():
    """
    Tests the obstacle sensor by continuously printing out
    the object distance detected.
    """
    drone = Drone  # define drone
    try:
        drone = Drone()
        drone.pair()
        while True:
            print('Object distance:', drone.get_front_range(), "cm")
    finally:
        print('Test Ended!')
        if drone:  # make sure drone object was created
            drone.close()


DISTANCE_THRESHOLD = 60
FORWARD_POWER = 10


drone = Drone()
drone.pair()
look_left = drone.turn_right(90)
look_right = drone.turn_left(90)


def is_object_detected(within_a_distance):
    """
    Returns a True if an object is less than or equal to
    the value passed to within_a_distance; otherwise False.
    """
    if drone.get_front_range() <= within_a_distance:
        return True
    else:
        return False


def avoid_object():
    drone.set_pitch(0)

    look_left()
    left_blocked = is_object_detected(150)

    look_right()
    right_blocked = is_object_detected(150)
    if left_blocked:
        look_right()
        drone.set_pitch(FORWARD_POWER)
    if right_blocked:
        look_left()
        drone.set_pitch(FORWARD_POWER)
    else:
        if left_blocked and right_blocked:
            drone.set_pitch(FORWARD_POWER)


def fly_drone():
    drone.takeoff()
    drone.set_pitch(FORWARD_POWER)
    try:
        while True:
            drone.move()
            if is_object_detected(DISTANCE_THRESHOLD):
                avoid_object()
    finally:
        drone.set_pitch(0)
        drone.land()
        drone.close()


fly_drone()