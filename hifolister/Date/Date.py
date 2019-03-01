#!/usr/bin/env python
"""Class to represent a Date."""

class Date:
    """Class representing a date"""

    def __init__(self, date):
        """Constructor for the Date class."""
        _ThrowErorrDateEarlierThanEpoch(date)
        self.date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        _ThrowErorrDateEarlierThanEpoch(new_date)
        self._date = new_date


def _ThrowErorrDateEarlierThanEpoch(dateToCheck):
    """Throws an error if the dateToCheck is smaller than zero/earlier than the epoch."""
    if dateToCheck < 0:
        raise ValueError("Dates before the Epoch (1970-01-01) are not possible!")
