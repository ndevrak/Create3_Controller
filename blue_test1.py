from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

import usb

bluetooth = Bluetooth()
robot = Create3(bluetooth)

@event(robot.when_play)
async def draw_square(robot):
    print("Battery Level : " + str(await robot.get_battery_level())) # Print Battery Level

    await robot.reset_navigation() # reset internal track of location

    #await robot.set_wheel_speeds(left = 100, right = 100) # sets wheel speeds in cms

    for i in range(3):
        await robot.move(20)  # cm
        await robot.turn_left(120)  # deg

robot.play()