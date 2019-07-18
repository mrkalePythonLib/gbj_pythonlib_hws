# -*- coding: utf-8 -*-
"""Simulation of pyA20 ports."""
__version__ = "0.1.0"
__status__ = "Beta"
__author__ = "Libor Gabaj"
__copyright__ = "Copyright 2019, " + __author__
__credits__ = []
__license__ = "MIT"
__maintainer__ = __author__
__email__ = "libor.gabaj@gmail.com"

PA1 = 11
PA0 = 13
PA3 = 15
PC0 = 19
PC1 = 21
PC2 = 23
PA19 = 27
PA7 = 29
PA8 = 31
PA9 = 33
PA10 = 35
PA20 = 37
PA13 = 8
PA14 = 10
PD14 = 12
PC4 = 16
PC7 = 18
PA2 = 22
PC3 = 24
PA21 = 26
PA18 = 28
PG8 = 32
PG9 = 36
PG6 = 38
PG7 = 40

POWER_LED = 1
STATUS_LED = 2

pinlist = list({
    PA1, PA0, PA3, PC0, PC1, PC2, PA19, PA7, PA8, PA9, PA10, PA20, PA13, PA14,
    PD14, PC4, PC7, PA2, PC3, PA21, PA18, PG8, PG9, PG6, PG7,
    POWER_LED, STATUS_LED,
})
