#!/usr/bin/env python3

import time

import pigpio

from .bus import Bus


class SPI_pigpio(Bus):
    """SPI bus with pigpio"""

    def __init__(self, pi: pigpio.pi, ch: int, baud: int, reset_pin: int, rs_pin: int):
        self.pi = pi
        self.ch = ch
        self.baud = baud
        self.reset_pin = reset_pin
        self.rs_pin = rs_pin

        pi.set_mode(reset_pin, pigpio.OUTPUT)
        pi.set_mode(rs_pin, pigpio.OUTPUT)
        pi.write(reset_pin, 1)
        pi.write(rs_pin, 0)

    def reset(self):
        self.pi.write(self.reset_pin, 0)
        time.sleep(0.0001)
        self.pi.write(self.reset_pin, 1)

    def write(self, value, to_data=False):
        self.pi.write(self.rs_pin, to_data)

        if type(value) is int:
            assert value <= 0xFF
            buf = bytes([value])
        elif type(value) is bytes:
            buf = value
        else:
            raise TypeError()

        spi = self.pi.spi_open(self.ch, self.baud)
        self.pi.spi_xfer(spi, buf)
        self.pi.spi_close(spi)

    def close(self):
        pass
