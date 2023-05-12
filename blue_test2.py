from Create3_Controller.core import C3C
from irobot_edu_sdk.robots import event
from irobot_edu_sdk.backend.bluetooth import Bluetooth
import numpy as np

# this is a basic controller using the code I (sam) wrote
# it just makes a figure 8, turning a full circle left, then right

robot = C3C(Bluetooth())

robot.add_action(robot.calc_arc_path(10, 25, 2*np.pi))
robot.add_action({"speeds":{"left" : 0, "right" : 0}, "time": 0.5})
robot.add_action(robot.calc_arc_path(10, -25, 2*np.pi))

for q in robot._action_que:
    print(q)

@event(robot.when_play)
async def play(robot):
    print("Battery Level : " + str((await robot.get_battery_level())[1]) + "%")
    await robot.command_loop()

robot.play()