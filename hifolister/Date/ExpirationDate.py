#!/usr/bin/env python
"""Class to represent an ExpirationDate."""
import time
from . import Date

class ExpirationDate(Date.Date):
    """Class representin an expiration date."""

    def __init__(self, date):
        """Constructor for the ExpirationDate class."""
        _ThrowErrorDateEarlierThanNow(date)
        super().__init__(date)


def  _ThrowErrorDateEarlierThanNow(dateToCheck):
    if dateToCheck < int(time.time()):
        raise ValueError("Expiration date can only be in the future!")
