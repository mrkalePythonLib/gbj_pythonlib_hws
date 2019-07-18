# -*- coding: utf-8 -*-
"""Module for controlling GPIOs of Orange Pi microcomputers."""
__version__ = "0.1.0"
__status__ = "Beta"
__author__ = "Libor Gabaj"
__copyright__ = "Copyright 2019, " + __author__
__credits__ = []
__license__ = "MIT"
__maintainer__ = __author__
__email__ = "libor.gabaj@gmail.com"


import logging

from . import gpio, port, connector


###############################################################################
# Classes
###############################################################################
class OrangePiOne(object):
    """Creating a GPIO manager for microcomputer ``Orange Pi One``.

    Notes
    -----
    - GPIO pins including system LEDs are identified for the sake of this class
      by name of its attributes defined in the library.
    - Each pin can be named in the form as a ``port`` or as a ``connector``.
      Each form has its own list of available pin names, which can be obtained
      with commands::

          dir(port)
          dir(connector)

    - List of available ports for GPIO pins:
      ``PA0``, ``PA1``, ``PA10``, ``PA11``, ``PA12``, ``PA13``, ``PA14``,
      ``PA18``, ``PA19``, ``PA2``, ``PA20``, ``PA21``, ``PA3``, ``PA6``,
      ``PA7``, ``PA8``, ``PA9``, ``PC0``, ``PC1``, ``PC2``, ``PC3``, ``PC4``,
      ``PC7``, ``PD14``, ``PG6``, ``PG7``, ``PG8``, ``PG9``

    - List of available ports for system LEDS:
      ``POWER_LED``, ``STATUS_LED``

    - List of available connectors for GPIO pins:
      ``gpio1p10``, ``gpio1p11``, ``gpio1p12``, ``gpio1p13``, ``gpio1p15``,
      ``gpio1p16``, ``gpio1p18``, ``gpio1p19``, ``gpio1p21``, ``gpio1p22``,
      ``gpio1p23``, ``gpio1p24``, ``gpio1p26``, ``gpio1p27``, ``gpio1p28``,
      ``gpio1p29``, ``gpio1p3``, ``gpio1p31``, ``gpio1p32``, ``gpio1p33``,
      ``gpio1p35``, ``gpio1p36``, ``gpio1p37``, ``gpio1p38``, ``gpio1p40``,
      ``gpio1p5``, ``gpio1p7``, ``gpio1p8``

    - List of available connectors for system LEDS:
      ``LEDp1``, ``LEDp2``

    """

    def __init__(self):
        """Create the class instance - constructor."""
        # Hardware initialization
        gpio.init()
        # Logging
        self._logger = logging.getLogger(' '.join([__name__, __version__]))
        self._logger.debug(
            'Instance of %s created: %s',
            self.__class__.__name__,
            str(self)
            )

    def __str__(self):
        """Represent instance object as a string."""
        return self.__class__.__name__

    def _convert_pin_port(self, pin):
        """Convert pin name to port number.

        Arguments
        ---------
        pin : str
            Name of a pin in form of either ``port`` or ``connector``.

        Returns
        -------
        portnum : int
            SoC port number (offset) of the pin or 0.

        """
        if pin in dir(port):
            port_num = getattr(port, pin)
        elif pin in dir(connector):
            port_num = getattr(connector, pin)
        else:
            errmsg = "Unknown pin {}".format(pin)
            self._logger.error(errmsg)
            return 0
        return port_num

    def pin_on(self, pin):
        """Set pin as OUTPUT and to HIGH.

        Arguments
        ---------
        pin : str
            Name of a pin in form either `port` or `connector`.

        Raises
        ------
        NameError
            Pin name is defined neither among ports nor connectors.
            Error message included to the exception.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            gpio.setcfg(port_num, gpio.OUTPUT)
            gpio.output(port_num, gpio.HIGH)

    def pin_off(self, pin):
        """Set pin as OUTPUT and to LOW.

        See Also
        --------
        pin_on : Arguments, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            gpio.setcfg(port_num, gpio.OUTPUT)
            gpio.output(port_num, gpio.LOW)

    def pin_toggle(self, pin):
        """Set pin as OUTPUT and invert its state.

        See Also
        --------
        pin_on : Arguments, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            port_state = gpio.HIGH
            if gpio.input(port_num) == gpio.HIGH:
                port_state = gpio.LOW
            gpio.setcfg(port_num, gpio.OUTPUT)
            gpio.output(port_num, port_state)

    def pin_pullup(self, pin):
        """Set PULLUP of pin.

        See Also
        --------
        pin_on : Arguments, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            gpio.pullup(port_num, gpio.PULLUP)

    def pin_pulldown(self, pin):
        """Set PULLDOWN of pin.

        See Also
        --------
        pin_on : Arguments, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        gpio.pullup(port_num, gpio.PULLDOWN)

    def pin_pullclear(self, pin):
        """Reset PULLUP or PULLDOWN of pin.

        See Also
        --------
        pin_on : Arguments, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            gpio.pullup(port_num, gpio.PULLNONE)

    def pin_read(self, pin, mode=gpio.INPUT):
        """Set pin as INPUT and read its state.

        Returns
        -------
        pin_state : {gpio.HIGH, gpio.LOW}
            Current state of the pin or None

        See Also
        --------
        pin_on : Arguments, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            gpio.setcfg(port_num, gpio.INTPUT)
            value = gpio.input(port_num)
            return value

    def pin_state(self, pin):
        """Return pin state without changing its mode.

        Returns
        -------
        pin_state : {gpio.HIGH, gpio.LOW}
            Current state of the pin or None

        See Also
        --------
        pin_on : Arguments, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            value = gpio.input(port_num)
            return value

    def is_pin_on(self, pin):
        """Return flag about pin state HIGH.

        Arguments
        ---------
        pin : str
            Name of a pin in form either `port` or `connector`.
            *The argument is mandatory and has no default value.*

        Returns
        -------
        flag_high : bool
            Logical flag about pin state HIGH or None.
            True if HIGH or False for LOW.

        Raises
        ------
        NameError
            Pin name is defined neither among ports nor connectors.
            Error message included to the exception.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            return gpio.input(port_num) == gpio.HIGH

    def is_pin_off(self, pin):
        """Return flag about pin state LOW.

        See Also
        --------
        is_pin_on : Arguments, Returns, Raises are the same, see docstrings.

        """
        return not self.is_pin_on(pin)

    def is_pin_output(self, pin):
        """Return flag about pin mode OUTPUT.

        See Also
        --------
        is_pin_on : Arguments, Returns, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            return gpio.getcfg(port_num) == gpio.OUTPUT

    def is_pin_input(self, pin):
        """Return flag about pin mode INPUT.

        See Also
        --------
        is_pin_on : Arguments, Returns, Raises are the same, see docstrings.

        """
        port_num = self._convert_pin_port(pin)
        if port_num:
            return gpio.getcfg(port_num) == gpio.INPUT
