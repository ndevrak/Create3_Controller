import usb.core
import usb.util

from usb_backend import USB1

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(USB1())

@event(robot.when_play)
async def draw_square(robot):
    await robot.set_lights_rbg(0,0,255)

robot.play()