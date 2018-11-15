#!/usr/bin/env python3

import time

import pigpio

from .bus import Bus


class SPI_pigpio(Bus):
    """SPI bus with pigpio"""

    def __init__(self, pi: pigpio.pi, spi_handle: int, reset_pin: int, rs_pin: int):
        self.pi = pi
        self.spi = spi_handle
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
            self.pi.spi_xfer(self.spi, bytes([value]))
        elif type(value) is bytes:
            self.pi.spi_xfer(self.spi, value)
        else:
            raise TypeError()

    def close(self):
        self.pi.spi_close(self.spi)
