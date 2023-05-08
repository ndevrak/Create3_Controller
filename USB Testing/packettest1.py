from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.packet import Packet
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
from irobot_edu_sdk.utils import bound

animation = bound(Robot.LIGHT_ON, Robot.LIGHT_OFF, Robot.LIGHT_SPIN)

payload = bytes([animation, 0, 0, 255])
print(payload)
packet = Packet(3,2, 0, payload)
print(packet.to_bytearray())
print(packet.to_bytes())
#await self._backend.write_packet(Packet(3, 2, self.inc, payload))