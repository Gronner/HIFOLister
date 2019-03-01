#!/usr/bin/env python
"""Test for the HIFOList Class."""

class FifoList:
    """Class for a FIFO List"""

    def __init__(self, information):
        """Constructor for the FifoList class."""
        self.information = information
        self.topElement = None
        self._length = 0

    def __len__(self):
        return self._length

    def insertElement(self, new_element):
        """Inserts a new element into the list."""
        if self.topElement is None:
            self.topElement = new_element
        else:
            currentElement = self.topElement
            while(currentElement.nextElement):
                currentElement = currentElement.nextElement
            currentElement.nextElement = new_element
            new_element.previousElement = currentElement
        self._length += 1
