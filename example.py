#!/usr/bin/env python3

import time

import pigpio

from lcd import LCD_ST7032, SPI_pigpio

LCD_SPI_CH = 1
LCD_SPI_BAUD = 1000000
LCD_RESET_PIN = 6
LCD_RS_PIN = 5

pi = pigpio.pi()

bus = SPI_pigpio(pi, LCD_SPI_CH, LCD_SPI_BAUD, LCD_RESET_PIN, LCD_RS_PIN)
lcd = LCD_ST7032(bus)

lcd.print("Hello")
lcd.set_cursor(2, 1)
lcd.print("World")

time.sleep(1)

lcd.clear()
lcd.set_cursor(15, 0)
lcd.set_entry_mode(shift=True)
lcd.print("Scrolling long text.", 0.5)

lcd.close()
pi.stop()
