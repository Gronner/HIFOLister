#!/usr/bin/env python
"""ListElements base implementation used for a simple FIFO list."""

from . import ListElement
from Date import ExpirationDate

class PriorityElement(ListElement.ListElement):
    """List elements with a priority value."""

    def __init__(self, information, priority, expirationDate=ExpirationDate.NoExpirationDate):
        self.information = information
        self.priority = priority
        self.expirationDate = expirationDate
        self.nextElement = None
        self.previousElement = None

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, new_priority):
        if new_priority < 1:
            raise ValueError("Priority can not be smaller than 1!")
        else:
            self._priority = new_priority
