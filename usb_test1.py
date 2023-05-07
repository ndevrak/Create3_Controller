import usb.core
import usb.util

dev = usb.core.find()

dev.set_configuration()

print(dev)