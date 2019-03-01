#!/usr/bin/env python
"""ListInformation describing a HIFOList."""

class ListInformation:
    """Contains printable information about a list."""

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __eq__(self, other):
        """Implemetation of the == operator."""
        return (self.name == other.name) and (self.description == other.description)
