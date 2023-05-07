import usb.core
import usb.util

dev = usb.core.find()

if dev is None:
    raise ValueError("Our device is not connected")

cfg = usb.util.find_descriptor(dev, )