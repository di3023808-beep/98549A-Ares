# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       david                                                        #
# 	Created:      9/25/2026, 2:08:02 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()

#drivetrain motors
left_motor_A = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
left_motor_B = Motor(Ports.PORT14, GearSetting.RATIO_6_1, True)
left_drive_smart = MotorGroup(left_motor_A, left_motor_B)
right_motor_A = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
right_motor_B = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
right_drive_smart = MotorGroup(right_motor_A, right_motor_B)
controller_1 = Controller(PRIMARY)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 292.1, 40, MM, 1.66667)

#sensor
inert = Inertial(Ports.PORT1,True)

#cascade motors
cascade_left = Motor(Ports.PORT15, GearSetting.RATIO_36_1, False)
cascade_right = Motor(Ports.PORT20, GearSetting.RATIO_36_1, True)
cascade = MotorGroup(cascade_left, cascade_right)

#intake motor
intake = Motor(Ports.PORT16, GearSetting.RATIO_6_1, False)

#claw
claw = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        # drive control variables
        foward = controller_1.axis3.position()
        turn = controller_1.axis1.position()

        #drive control math
        left_speed = foward + turn
        right_speed = foward - turn

        #drive control commands
        left_drive_smart.spin(FORWARD, left_speed, PERCENT)
        right_drive_smart.spin(FORWARD, right_speed, PERCENT)

        #cascade control variables
        cascade_up = controller_1.buttonR1.pressing()
        cascade_down = controller_1.buttonR2.pressing()

        #cascade control commands
        if cascade_up:
            cascade.spin(FORWARD, 100, PERCENT)
        elif cascade_down:
            cascade.spin(REVERSE, 100, PERCENT)
        else:
            cascade.stop(HOLD)

        #intake control variables
        intake_in = controller_1.buttonL1.pressing()
        intake_out = controller_1.buttonL2.pressing()

        #intake control commands
        if intake_in:   
            intake.spin(FORWARD, 100, PERCENT)
        elif intake_out:
            intake.spin(REVERSE, 100, PERCENT)
        else:
            intake.stop(HOLD)

        #claw control variables
        claw_open = controller_1.buttonUp.pressing()
        claw_close = controller_1.buttonDown.pressing()

        #claw control commands
        if claw_open:
            claw.spin(FORWARD, 100, PERCENT)
        elif claw_close:
            claw.spin(REVERSE, 100, PERCENT)
        else:
            claw.stop(HOLD)

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()