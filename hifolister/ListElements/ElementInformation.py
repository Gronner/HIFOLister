#!/usr/bin/env python
"""ElementInformation describing a ListElement."""

class ElementInformation:
    """Contains printable information about an element."""

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __eq__(self, other):
        """Implemetation of the == operator."""
        return (self.name == other.name) and (self.description == other.description)
