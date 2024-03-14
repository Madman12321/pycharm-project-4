# Python code
########################################################
# Drone Music by <HK>
#
# References:
# 1. Clocks by Coldplay, <https://www.youtube.com/watch?v=d020hcWA_Wg>
# 2. Sheet Music of CLocks, <https://www.virtualsheetmusic.com/score/HL-18137.html>
########################################################
from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.set_drone_LED(0, 50, 50, 255)
# measure one
drone.drone_buzzer(Note.D5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.F4, 250)
drone.drone_buzzer(Note.D5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.F4, 250)
drone.drone_buzzer(Note.D5, 250)
drone.drone_buzzer(Note.A4, 250)
# measure two
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
# measure three
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
# measure four
drone.drone_buzzer(Note.B4, 250)
drone.drone_buzzer(Note.G4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.B4, 250)

drone.drone_buzzer(Note.G4, 300)
drone.drone_buzzer(Note.E4, 300)

drone.drone_buzzer(Note.B4, 400)
# measure five
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.F4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.F4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
# measure six
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
# measure seven
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.C5, 250)
drone.drone_buzzer(Note.A4, 250)
# measure eight
drone.drone_buzzer(Note.B4, 250)
drone.drone_buzzer(Note.G4, 250)
drone.drone_buzzer(Note.E4, 250)
drone.drone_buzzer(Note.B4, 250)

drone.drone_buzzer(Note.G4, 300)
drone.drone_buzzer(Note.E4, 300)

drone.drone_buzzer(Note.B4, 400)
# measure nine
drone.drone_buzzer(Note.D5, 400)
drone.drone_buzzer(Note.D5, 400)
drone.drone_buzzer(Note.D5, 400)

drone.drone_buzzer(Note.D5, 300)
drone.drone_buzzer(Note.B4, 300)
# measure ten
drone.drone_buzzer(Note.C5, 400)
drone.drone_buzzer(Note.B4, 400)
drone.drone_buzzer(Note.A4, 400)
drone.drone_buzzer(Note.A4, 800)
# measure eleven
drone.drone_buzzer(Note.C5, 400)
drone.drone_buzzer(Note.C5, 300)
drone.drone_buzzer(Note.C5, 300)
drone.drone_buzzer(Note.C5, 600)
drone.drone_buzzer(Note.A4, 400)
# measure twelve
drone.drone_buzzer(Note.B4, 400)
drone.drone_buzzer(Note.A4, 400)
drone.drone_buzzer(Note.G4, 400)
drone.drone_buzzer(Note.G4, 400)
drone.drone_buzzer(Note.D4, 400)
drone.close()
