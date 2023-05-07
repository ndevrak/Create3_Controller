from binascii import hexlify, unhexlify

from irobot_edu_sdk.backend.backend import Backend
from irobot_edu_sdk.packet import Packet

class USB1(Backend):
    def __init__(self):
        self._usb = False
    
    async def connect(self):
        """Connect to robot"""
        raise NotImplementedError()

    async def is_connected(self) -> bool:
        """Returns True if robot is connected"""
        raise NotImplementedError()

    async def disconnect(self):
        """Disconnect from robot"""
        raise NotImplementedError()

    async def write_packet(self, packet: Packet):
        """Write one packet to the robot"""
        raise NotImplementedError()

    async def read_packet(self) -> Packet:
        """Read one packet from the robot"""
        raise NotImplementedError()