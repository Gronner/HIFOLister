#!/usr/bin/env python
"""ListElements base implementation used for a simple FIFO list."""

class ElementInformation:
    """Contains printable information about an element"""

    def __init__(self, name, description=''):
        self.name = name
        self.description = description