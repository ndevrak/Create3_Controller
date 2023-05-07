from binascii import hexlify, unhexlify

from irobot_edu_sdk.backend.backend import Backend
from irobot_edu_sdk.packet import Packet

from asyncio import sleep

import usb.core
import usb.util

class USB1(Backend):
    def __init__(self):
        self._usb_dev = usb.core.find()
        self._usb_ep = self._usb_dev[0].interfaces()[0].endpoints()[0]
        self._usb_i = self._usb_dev[0].interfaces()[0].bInterfaceNumber

        if self._usb_dev.is_kernel_driver_dactive(self._usb_i):
            self._usb_dev.detach_ketnel_driver(self._usb_i)
        
    
    async def connect(self):
        """Connect to robot"""
        raise NotImplementedError()

    async def is_connected(self) -> bool:
        """Returns True if robot is connected"""
        raise NotImplementedError()

    async def disconnect(self):
        """Disconnect from robot"""
        raise NotImplementedError()

    async def read_packet(self) -> Packet:
        string = b''
        while not (string.endswith(b'\n') and len(string) > 40):
            await sleep(0)
            while not self._usb.any():
                await sleep(0)
            string += self._usb.read(1)
        return Packet.from_bytes(unhexlify(string[-41:-1]))

    async def write_packet(self, packet: Packet):
        string = hexlify(packet.to_bytes()) + b'\n'
        self._usb_dev.write(self._usb_ep, string, timeout = 2500)