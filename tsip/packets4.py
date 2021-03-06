# -*- coding: utf-8 -*-

"""
TSIP packets in the 0x4? range.

* 0x41 - GPS Time report.
* 0x42 - Single-Precision Position Fix, XYZ ECEF report.
* 0x43 - Velocity Fix, XYZ ECEF report.
* 0x45 - Software Version Information report.
* 0x46 - Health of Receiver report.
* 0x47 - Signal Levels for all Satellites report.
* 0x4a - Single Precision LLA Position Fix report.
* 0x4b - Machine/Code ID and Additional Status report.
* 0x4d - Oscillator Offset report.
* 0x4e - Response to Set GPS Time report.

"""


import struct

from tsip.base import Command, Report

class Report_41(Report):
    """
    GPS Time report.

    =====   ===============================================
    Index   Description
    =====   ===============================================
    0       GPS time of week (seconds)
    1       Extended GPS week number (weeks)
    2       GPS UTC offset (seconds)
    =====   ===============================================

    """

    _format = '>fhf'
    _values = []


class Report_42(Report):
    """
    Single-Precision Position Fix, XYZ ECEF report

    """

    _format = '>ffff'
    _values = []


class Report_43(Report):
    """
    Velocity Fix, XYZ ECEF report

    """

    _format = '>fffff'
    _values = []


class Report_45(Report):
    """
    Software Version Information report

    """

    _format = '>BBBBBBBBBB'
    _values = []


class Report_46(Report):
    """
    Health of Receiver report

    =====   ===============================================
    Index   Description
    =====   ===============================================
    0       Status code 
    1       Bits in byte 1
    =====   ===============================================

    """

    _format = '>BB'
    _values = []


class Report_47(Report):
    """
    Signal Levels for all Satellites report

    """

    _format = ''
    _values = []


class Report_4a(Report):
    """
    Single Precision LLA Position Fix report

    """

    _format = '>fffff'
    _values = []


class Report_4b(Report):
    """
    Machine/Code ID and Additional Status report

    =====   ===============================================
    Index   Description
    =====   ===============================================
    0       Machine ID
    1       Status 1
    2       Status 2
    =====   ===============================================

    """

    _format = '>BBB'
    _values = []


class Report_4d(Report):
    """
    Oscillator Offset report

    """

    _format = '>f'
    _values = []


class Report_4e(Report):
    """
    Response to Set GPS Time report

    """

    _format = '>c'
    _values = []

