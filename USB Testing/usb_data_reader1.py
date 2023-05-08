import usb.core
import usb.util

dev = usb.core.find(idProduct = 0x8603)

print(dev)

ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

print(dev[0].interfaces())
print(ep)

while True:
    ret = dev.read(ep, ep.wMaxPacketSize, 3000)