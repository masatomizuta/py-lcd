#!/usr/bin/env python3


class HD44780(object):
    """Hitachi dot-matrix liquid crystal display controller
    Ref: HD44780 datasheet Rev. 0.0 - Table 6 page 24
    """

    @staticmethod
    def clear_display():
        """Clear display
        Clears entire display and sets DDRAM address 0 in address counter.
        """
        return 0x01

    @staticmethod
    def return_home():
        """Return home
        Sets DDRAM address 0 in address counter. Also returns display from being shifted to original position.
        DDRAM contents remain unchanged.
        """
        return 0x02

    @staticmethod
    def entry_mode_set(ID: bool, S: bool):
        """Entry mode set
        Sets cursor move direction and specifies display shift.
        These operations are performed during data write and read.
        :param ID: True: Increment, False: Decrement
        :param S: Accompanies display shift
        """
        return 0x04 | ID << 1 | S

    @staticmethod
    def display_on_off(D: bool, C: bool, B: bool):
        """Display on/off control
        Sets entire display (D) on/off, cursor on/off (C), and blinking of cursor position character (B).
        :param D: Display ON/OFF control bit
        :param C: Cursor ON/OFF control bit
        :param B: Cursor Blink ON/OFF control bit
        """
        return 0x08 | D << 2 | C << 1 | B

    @staticmethod
    def cursor_or_display_shift(SC: bool, RL: bool):
        """Cursor of display shift
        Moves cursor and shifts display without changing DDRAM contents.
        :param SC: True: Display shift, False: Cursor move
        :param RL: True: Shift to the right, False: Shift to the left
        """
        return 0x10 | SC << 3 | RL << 2

    @staticmethod
    def function_set(DL=True, N=True, F=False):
        """Function set
        Sets interface data length (DL), number of display lines (N), and character font (F).
        :param DL: True: 8 bits, False: 4 bits
        :param N: True: 2 lines, False: 1 line
        :param F: True: 5 x 10 dots, False: 5 x 8 dots
        """
        return 0x20 | DL << 4 | N << 3 | F << 2

    @staticmethod
    def set_cgram_address(addr: int):
        """Set CGRAM address
        Sets CGRAM address. CGRAM data is sent and received after this setting.
        """
        assert addr <= 0b00111111
        return 0x40 | addr

    @staticmethod
    def set_ddram_address(addr: int):
        """Set DDRAM address
        Sets DDRAM address. DDRAM data is sent and received after this setting.
        """
        assert addr <= 0b01111111
        return 0x80 | addr
