#!/usr/bin/env python
"""ListElements base implementation used for a simple FIFO list."""

from Date import ExpirationDate

class ListElement:
    """Base Class for list Elements"""

    def __init__(self, information, expirationDate=ExpirationDate.NoExpirationDate):
        self.information = information
        self.expirationDate = expirationDate
        self.nextElement = None
        self.previousElement = None
