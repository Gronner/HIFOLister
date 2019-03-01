#!/usr/bin/env python
"""Tests for the ListElement."""
import sys
import os.path
import pytest
import random
sys.path.append(os.path.abspath('./hifolister'))
from Date import Date

class TestDateConstructor:
    """Tests for a dates constructor."""

    def test_CreateDateAtEpoch(self):
        """Creates a new Date at Epoch."""
        testDate = 0

        dateAtEpoch = Date.Date(testDate)

        assert dateAtEpoch.date == testDate

    def test_CreateAllowedDate(self):
        """Creates a new Date at a random allowed Date."""
        testDate = random.randint(0, sys.maxsize)

        dateAllowed = Date.Date(testDate)

        assert dateAllowed.date == testDate

    def test_CreateNonExistendDate(self):
        """Creates a new Date at a random non existend Date."""
        testDate = random.randint((-sys.maxsize -1), 0)
        
        with pytest.raises(ValueError):
            dateDisallowed = Date.Date(testDate)
