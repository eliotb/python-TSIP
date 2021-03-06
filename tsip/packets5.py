# -*- coding: utf-8 -*-

"""
TSIP packets in the 0x5? range.

* 0x55 - I/O Options report.
* 0x56 - Velocity Fix, East-North-Up (ENU) report.
* 0x57 - Information About Last Computed Fix report.
* 0x58 - Satellite System Data/Acknowledge from Receiver.
* 0x5a - Raw Measurement Data report.
* 0x5c - Satellite Tracking Status report.

"""


import struct

from tsip.base import Command, Report


class Report_55(Report):
    """
    I/O Options report.

    """

    _format = '>BBBB'
    _values = []


class Report_56(Report):
    """
    Velocity Fix, East-North-Up (ENU) report

    """

    _format = '>fffff'
    _values = []


class Report_57(Report):
    """
     Information About Last Computed Fix

    """

    _format = '>BBfh'
    _values = []


class Report_58(Report):
    """
    Satellite System Data/Acknowledge from Receiver

    """

    _format = '>?????'
    _values = []


class Report_5a(Report):
    """
    Raw Measurement Data

    """

    _format = '>BBBBBfffd'
    _values = []


class Report_5c(Report):
    """
    Satellite Tracking Status report

    """

    _format = '>BBBBffffB'
    _values = []
