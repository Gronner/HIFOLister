#!/usr/bin/env python
"""Test for the HIFOList Class."""
from ListElements import ListElement

class FifoList:
    """Class for a FIFO List"""

    def __init__(self, information):
        """Constructor for the FifoList class."""
        self.information = information
        self.topElement = None
        self._length = 0

    def __len__(self):
        return self._length

    def insertElement(self, newElement):
        """Inserts a new element at the end of the list."""
        if self.topElement is None:
            self.topElement = newElement
        else:
            currentElement = self.topElement
            while(currentElement.nextElement):
                currentElement = currentElement.nextElement
            currentElement.nextElement = newElement
            newElement.previousElement = currentElement
        self._length += 1

    def pop(self):
        """Removes the top element in the list and returns it."""
        if self.topElement is None:
            return ListElement.NoListElement
        oldTopElement = self.topElement
        if not self.topElement.nextElement is None:
            newTopElement = self.topElement.nextElement
            newTopElement.previousElement = None
            self.topElement = newTopElement

        self._length -= 1
        return oldTopElement

    def remove(self, targetElement):
        """Removes the target element from the list and returns it."""
        currentElement = self.topElement
        while(currentElement):
            if currentElement == targetElement:
                if not currentElement.previousElement is None:
                    currentElement.previousElement.nextElement = currentElement.nextElement
                if not currentElement.nextElement is None:
                    currentElement.nextElement.previousElement = currentElement.previousElement
                self._length -= 1
                return currentElement
            currentElement = currentElement.nextElement
        return ListElement.NoListElement

    def update(self):
        """Does nothing for a FIFO list."""
        pass
