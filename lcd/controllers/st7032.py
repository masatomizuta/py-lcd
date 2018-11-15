#!/usr/bin/env python3

from .hd44780 import HD44780


class ST7032(HD44780):
    """Sitronix Dot Matrix LCD Controller/Driver
    Ref: ST7032 datasheet v1.4 - page 20
    """

    @staticmethod
    def function_set(DL=True, N=True, DH=False, IS=False):
        """Function set
        Sets interface data length (DL), number of display lines (N), character font (DH),
        and normal/extension instruction select (IS).
        :param DL: True: 8 bits, False: 4 bits
        :param N: True: 2 lines, False: 1 line
        :param DH: True: 5 x 10 dots, False: 5 x 8 dots
        :param IS: True: extension instruction, False: normal instruction
        """
        assert not (N & DH)
        return 0x20 | DL << 4 | N << 3 | DH << 2 | IS

    # Instruction table 1(IS=1)

    @staticmethod
    def internal_osc_frequency(BS: bool, F: int):
        """Internal OSC frequency
        :param BS: bias selection. (True: 1/4 bias, False: 1/5 bias)
        :param F: Internal OSC frequency adjust.
        """
        assert F <= 0b0111
        return 0x10 | BS << 3 | F

    @staticmethod
    def set_icon_address(addr: int):
        """Set ICON address
        Set ICON address in address counter.
        """
        assert addr <= 0b1111
        return 0x40 | addr

    @staticmethod
    def power_icon_control_contrast_set(Ion: bool, Bon: bool, Csh: int):
        """Power/ICON control/Contrast set
        :param Ion: set ICON display on/off
        :param Bon: set booster circuit on/off
        :param Csh: Contrast set(high byte)
        """
        assert Csh <= 0b0011
        return 0x50 | Ion << 3 | Bon << 2 | Csh

    @staticmethod
    def follower_control(Fon: bool, Rab: int):
        """Follower control
        :param Fon: set follower circuit on/off
        :param Rab: select follower amplified ratio.
        """
        assert Rab <= 0b0111
        return 0x60 | Fon << 3 | Rab

    @staticmethod
    def contrast_set(Csl: int):
        """Contrast set
        :param Csl: Contrast set(low byte)
        """
        assert Csl <= 0b1111
        return 0x70 | Csl
