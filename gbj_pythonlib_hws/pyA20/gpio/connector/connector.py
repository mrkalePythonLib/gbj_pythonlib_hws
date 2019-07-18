# -*- coding: utf-8 -*-
"""Simulation of pyA20 connectors."""
__version__ = "0.1.0"
__status__ = "Beta"
__author__ = "Libor Gabaj"
__copyright__ = "Copyright 2019, " + __author__
__credits__ = []
__license__ = "MIT"
__maintainer__ = __author__
__email__ = "libor.gabaj@gmail.com"

gpio1p11 = 11
gpio1p13 = 13
gpio1p15 = 15
gpio1p19 = 19
gpio1p21 = 21
gpio1p23 = 23
gpio1p27 = 27
gpio1p29 = 29
gpio1p31 = 31
gpio1p33 = 33
gpio1p35 = 35
gpio1p37 = 37
gpio1p8 = 8
gpio1p10 = 10
gpio1p12 = 12
gpio1p16 = 16
gpio1p18 = 18
gpio1p22 = 22
gpio1p24 = 24
gpio1p26 = 26
gpio1p28 = 28
gpio1p32 = 32
gpio1p36 = 36
gpio1p38 = 38
gpio1p40 = 40

LEDp1 = 1
LEDp2 = 2

pinlist = list({
    gpio1p11, gpio1p13, gpio1p15, gpio1p19, gpio1p21, gpio1p23, gpio1p27,
    gpio1p29, gpio1p31, gpio1p33, gpio1p35, gpio1p37, gpio1p8, gpio1p10,
    gpio1p12, gpio1p16, gpio1p18, gpio1p22, gpio1p24, gpio1p26, gpio1p28,
    gpio1p32, gpio1p36, gpio1p38, gpio1p40,
    LEDp1, LEDp2,
})
