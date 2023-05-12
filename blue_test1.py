from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
from asyncio import sleep

# this is a basic control using the code irobot provides
# just turns robot in place

robot = Create3(Bluetooth())

@event(robot.when_play)
async def play(robot):
    print("Battery Level : " + str((await robot.get_battery_level())[1]) + "%") # Print Battery Level
    await robot.turn_left(90)
    await robot.turn_right(90)

    # Same result as the previous 2 commands.
    await robot.turn_left(90)
    await robot.turn_left(-90)

robot.play()