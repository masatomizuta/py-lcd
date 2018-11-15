#!/usr/bin/env python3

import time

import pigpio

import lcd

pi = pigpio.pi()
spi = pi.spi_open(1, 5000000)

bus = lcd.SPI_pigpio(pi, spi, reset_pin=6, rs_pin=5)
lc = lcd.LCD_ST7032(bus)

lc.print("Hello")
lc.set_cursor(2, 1)
lc.print("World")

time.sleep(1)

lc.clear()
lc.set_cursor(15, 0)
lc.set_entry_mode(shift=True)
lc.print("Scrolling long text.", 0.5)

lc.close()
pi.stop()
