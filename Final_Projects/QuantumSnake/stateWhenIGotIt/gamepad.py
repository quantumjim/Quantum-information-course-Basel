import board
import struct
import usb_hid
import pew


pew.init()
screen = pew.Pix()
for gamepad in usb_hid.devices:
    if gamepad.usage_page == 0x01 and gamepad.usage == 0x05:
        break
else:
    raise RuntimeError("Gamepad HID device not found")
report = bytearray(6)

while True:
    buttons = pew.keys()
    report_buttons = 0

    if buttons & pew.K_O:
        screen.pixel(6, 3, 3)
        report_buttons |= 0x01
    else:
        screen.pixel(6, 3, 1)

    if buttons & pew.K_X:
        screen.pixel(6, 5, 3)
        report_buttons |= 0x02
    else:
        screen.pixel(6, 5, 1)

    if buttons & pew.K_UP:
        y = -127
        screen.pixel(2, 3, 3)
        screen.pixel(2, 5, 1)
    elif buttons & pew.K_DOWN:
        y = 127
        screen.pixel(2, 3, 1)
        screen.pixel(2, 5, 3)
    else:
        y = 0
        screen.pixel(2, 3, 1)
        screen.pixel(2, 5, 1)

    if buttons & pew.K_LEFT:
        x = -127
        screen.pixel(1, 4, 3)
        screen.pixel(3, 4, 1)
    elif buttons & pew.K_RIGHT:
        x = 127
        screen.pixel(1, 4, 1)
        screen.pixel(3, 4, 3)
    else:
        x = 0
        screen.pixel(1, 4, 1)
        screen.pixel(3, 4, 1)

    struct.pack_into('<Hbbbb', report, 0, report_buttons, x, y, 0, 0)
    gamepad.send_report(report)
    pew.show(screen)
    pew.tick(1/12)
