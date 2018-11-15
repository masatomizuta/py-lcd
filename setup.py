#!/usr/bin/env python

from setuptools import setup

setup(
    name='py-lcd',
    version='0.1.0',
    description='Python library for LCD',
    author='Masato Mizuta',
    author_email='mst.mizuta@gmail.com',
    url='https://github.com/masatomizuta/py-lcd/',
    packages=['lcd', 'lcd.buses', 'lcd.controllers'],
    install_requires=[
        'pigpio'
    ],
    keywords='LCD, HD44780, ST7032'
)
