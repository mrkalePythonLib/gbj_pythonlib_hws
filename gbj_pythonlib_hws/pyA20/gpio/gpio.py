# -*- coding: utf-8 -*-
"""Simulation of pyA20 GPIO."""
__version__ = "0.1.0"
__status__ = "Beta"
__author__ = "Libor Gabaj"
__copyright__ = "Copyright 2019, " + __author__
__credits__ = []
__license__ = "MIT"
__maintainer__ = __author__
__email__ = "libor.gabaj@gmail.com"


import logging

from .port import port
from .connector import connector

###############################################################################
# Constants
###############################################################################
HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1
PULLNONE = 0
PULLUP = 1
PULLDOWN = 2


###############################################################################
# Enumeration and parameter classes
###############################################################################
class Feature:
    """Indices of a pin features."""

    (MODE, PULL, VALUE,) = range(3)


###############################################################################
# Internal parameters
###############################################################################
_logger = None
_pins = {}


###############################################################################
# Internal functions
###############################################################################
def _check_pin(pin):
    """Check port pin and register it.

    Arguments
    ---------
    pin : int
        Pin identification from the module `port`, e.g., 'port.PA13',
        or module 'connector', e.g., 'connector.gpio1p8'.

    Raises
    ------
    NameError
        Pin name is not defined among ports.

    """
    global _pins
    if pin in port.pinlist or pin in connector.pinlist:
        if pin not in _pins.keys():
            _pins[pin] = {}
    else:
        errmsg = "Unknown pin {}".format(pin)
        raise NameError(errmsg)


def _check_mode(mode):
    """Check pin mode.

    Arguments
    ---------
    mode : int
        Mode identification from this module, e.g., OUTPUT.

    Raises
    ------
    ValueError
        Pin mode is not defined in this module.

    """
    if mode not in [PULLNONE, PULLUP, PULLDOWN]:
        errmsg = "Unknown pin mode {}".format(mode)
        raise ValueError(errmsg)


def _check_pull(pull):
    """Check pin pull action.

    Arguments
    ---------
    pull : int
        Pull action identification from this module, e.g., PULLUP.

    Raises
    ------
    ValueError
        Pin pull action is not defined in this module.

    """
    if pull not in [INPUT, OUTPUT]:
        errmsg = "Unknown pin pull {}".format(pull)
        raise ValueError(errmsg)


def _check_value(value):
    """Check available pin values.

    Arguments
    ---------
    value : int
        Binary value from this module, e.g., HIGH.

    Raises
    ------
    ValueError
        Pin value is not defined in this module.

    """
    if value not in [LOW, HIGH]:
        errmsg = "Unknown pin value {}".format(value)
        raise ValueError(errmsg)


###############################################################################
# Functions
###############################################################################
def init():
    """Initialize simulator."""
    global _logger
    # Initalize all pins for INPUT and HIGH
    for pin in port.pinlist:
        setcfg(pin, INPUT)
        output(pin, HIGH)
    # Logging
    _logger = logging.getLogger(' '.join([__name__, __version__]))
    _logger.debug(
        'Instance of %s created: %s',
        __name__,
        'GPIO simulator'
        )


def setcfg(pin, mode):
    """Configure pin.

    Arguments
    ---------
    pin : int
        Pin identification from the module `port`, e.g., 'port.PA13',
        or module 'connector', e.g., 'connector.gpio1p8'.

    """
    global _pins
    try:
        _check_pin(pin)
        _check_mode(mode)
        _pins[pin][Feature.MODE] = mode
    except NameError or ValueError as errmsg:
        _logger.error(errmsg)


def getcfg(pin):
    """Return current mode of the pin.

    Arguments
    ---------
    pin : int
        Pin identification from the module `port`, e.g., 'port.PA13',
        or module 'connector', e.g., 'connector.gpio1p8'.

    Returns
    -------
    int
        Registered pin mode or None.

    """
    global _logger
    try:
        _check_pin(pin)
        return _pins[pin][Feature.MODE]
    except NameError or TypeError as errmsg:
        _logger.error(errmsg)
    except KeyError:
        pass
    return None


def pullup(pin, pull):
    """Enable pullup/pulldown or disable all of them.

    Arguments
    ---------
    pin : int
        Pin identification from the module `port`, e.g., 'port.PA13',
        or module 'connector', e.g., 'connector.gpio1p8'.
    pull : int
        Enumerated pull action.

    """
    global _logger, _pins
    try:
        _check_pin(pin)
        _check_pull(pull)
        _pins[pin][Feature.PULL] = pull
    except NameError or ValueError as errmsg:
        _logger.error(errmsg)


def output(pin, value):
    """Set value to the pin.

    Arguments
    ---------
    pin : int
        Pin identification from the module `port`, e.g., 'port.PA13',
        or module 'connector', e.g., 'connector.gpio1p8'.
    value : int
        Desired value of the pin.

    """
    global _logger, _pins
    try:
        _check_pin(pin)
        _check_value(value)
        _pins[pin][Feature.VALUE] = value
    except NameError or ValueError as errmsg:
        _logger.error(errmsg)


def input(pin):
    """Return current pin value.

    Arguments
    ---------
    pin : int
        Pin identification from the module `port`, e.g., 'port.PA13',
        or module 'connector', e.g., 'connector.gpio1p8'.

    Returns
    -------
    int
        Current pin value or None.

    """
    global _logger
    try:
        _check_pin(pin)
        return _pins[pin][Feature.VALUE]
    except NameError or TypeError as errmsg:
        _logger.error(errmsg)
    except KeyError:
        pass
    return None
