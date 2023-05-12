from irobot_edu_sdk.backend import bluetooth
from irobot_edu_sdk.robots import Create3
import numpy as np

from collections import deque

from time import sleep
    
# the base class of the create3 with the bluetooth controller added
# inherits the "Create3" class from the irobot_edu_sdk
# needs a backend 
class C3C(Create3):

    # associates the create3 with the bluetooth backend
    def __init__(self, backend):
        super().__init__(backend=backend)

        # stores current wheel speeds
        self._wheel_speeds = {"left" : 0, "right" : 0}
        self._wheel_spacing = 23.5 #cm

        # using a queue now to hopefully make multithreading easier later
        # compute path on one thread, execute on another
        # I have little experience with this so may be better to have another structure
        self._action_que = deque()
    
    def speeds(self):
        return self._wheel_speeds

    async def set_speeds(self, sp):

        # if either speed is greater than the max speed
        # the arc of the path will be off
        # internally the robot bounds the given speed values
        # an error is thrown here to prevent this
        # a previous catcher that scales down wheel speeds may be better
        if np.abs(sp["left"]) > self.MAX_SPEED or np.abs(sp["right"]) > self.MAX_SPEED:
            raise ValueError("too high speed")
        
        # the robot doens't like driving backwards
        if (sp["left"] + sp["right"]) < 0:
            raise ValueError("robot cannot move backward")
        
        await self.set_wheel_speeds(sp["left"], sp["right"])
        self._wheel_speeds = sp
        
    
    def calc_arc_path(self, speed, rad, ang):
        # a positive radius is a left turn
        # negative radius gives a right turn
        # angle in radians

        # find the speeds of the left and right wheels
        left_speed = speed * (1 - self._wheel_spacing/2/rad)
        right_speed = speed * (1 + self._wheel_spacing/2/rad)

        speeds = {"left" : left_speed, "right" : right_speed}
        
        # the expected drive time for arc path segment
        # seems to work ok for large radius, but is very wrong for smaller radius
        # I think wheel slipping is a proble, might wanna use the robot's location information to help control for this
        time = np.abs(( rad*ang )/speed)
        
        # might wanna make an "action" class or something to handle different things
        return {"type" : "arc", "speeds" : speeds, "rad" : rad, "time" : time}
    
    def add_action(self, action):
        self._action_que.append(action)

    async def command_loop(self):
        while True:
            if len(self._action_que) == 0:
                await self.set_speeds({"left" : 0, "right" : 0})
                continue
            
            action = self._action_que.pop()
            
            if action == None:
                return

            await self.set_speeds(action["speeds"])
            sleep(action["time"])

        
