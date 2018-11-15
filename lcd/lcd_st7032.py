#!/usr/bin/env python3

import time

from .buses.bus import Bus
from .controllers import ST7032 as CMD
from .lcd import LCD


class LCD_ST7032(LCD):
    """LCD using ST7032 controller"""

    def __init__(self, bus: Bus):
        self.bus = bus
        self.init()

    def init(self):
        self.bus.reset()
        time.sleep(0.04)  # wait 40ms

        self.bus.write(CMD.function_set(IS=False))
        self.bus.write(CMD.function_set(IS=True))
        self.bus.write(CMD.internal_osc_frequency(BS=False, F=0b100))
        self.bus.write(CMD.power_icon_control_contrast_set(Ion=False, Bon=True, Csh=0b10))
        self.bus.write(CMD.contrast_set(0))
        self.bus.write(CMD.follower_control(Fon=True, Rab=0b101))
        time.sleep(0.2)  # wait 200ms

        self.bus.write(CMD.function_set(IS=False))
        self.set_entry_mode()
        self.display()
        self.clear()
        self.home()

    def clear(self):
        self.bus.write(CMD.clear_display())
        time.sleep(0.001)  # wait 1ms

    def home(self):
        self.bus.write(CMD.return_home())
        time.sleep(0.001)  # wait 1ms

    def display(self, screen=True, cursor=False, cursor_blink=False):
        self.bus.write(CMD.display_on_off(D=screen, C=cursor, B=cursor_blink))

    def set_entry_mode(self, increment=True, shift=False):
        self.bus.write(CMD.entry_mode_set(ID=increment, S=shift))

    def set_cursor(self, x: int, y: int):
        assert x >= 0 and y >= 0
        self.bus.write(CMD.set_ddram_address(y * 0x40 + x))

    def print(self, text: str, wait=0):
        for c in text:
            self.bus.write(ord(c), to_data=True)
            time.sleep(wait)

    def close(self):
        self.clear()
        self.bus.close()
