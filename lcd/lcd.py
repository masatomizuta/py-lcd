#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


class LCD(object, metaclass=ABCMeta):
    """Abstract LCD"""

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def home(self):
        pass

    @abstractmethod
    def display(self, screen=True, cursor=False, cursor_blink=False):
        pass

    @abstractmethod
    def set_entry_mode(self, increment=True, shift=False):
        pass

    @abstractmethod
    def set_cursor(self, x: int, y: int):
        pass

    @abstractmethod
    def print(self, text: str, wait=0):
        pass

    @abstractmethod
    def close(self):
        pass
