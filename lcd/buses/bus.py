#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


class Bus(object, metaclass=ABCMeta):
    """
    Abstract Bus Interface
    """

    @abstractmethod
    def reset(self) -> None:
        """Hardware reset"""
        pass

    @abstractmethod
    def write(self, value, to_data=False) -> None:
        """Write instruction or data
        :param value: int or bytes data
        :param to_data: True: write data, False: write instruction
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """Close bus"""
        pass
