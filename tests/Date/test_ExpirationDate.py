#!/usr/bin/env python
"""Tests for the ExpirationDate class."""
import sys
import os.path
import pytest
import random
import time
sys.path.append(os.path.abspath('./hifolister'))
from Date import ExpirationDate

class TestExpirationDateConstructor:
    """Tests for the ExpirationDate's constructor."""

    def test_CreateExpirationDateInFuture(self):
        """Creates an ExpirationDate in the future."""
        currentTime = int(time.time())
        testDate = currentTime + random.randint(1, sys.maxsize - currentTime)

        dateAllowed = ExpirationDate.ExpirationDate(testDate)
        assert dateAllowed.date == testDate

    def test_CreateExpirationDateInPast(self):
        """Creates an ExpirationDate in the past."""
        currentTime = int(time.time())
        testDate = random.randint(0, currentTime + 1)

        with pytest.raises(ValueError):
            dateDiasallowed = ExpirationDate.ExpirationDate(testDate)

    def test_CreateNonExistendExpirationDate(self):
        """Creates a new ExpirationDate at a random non existend Date."""
        testDate = random.randint((-sys.maxsize - 1), 0)

        with pytest.raises(ValueError):
            dateDiasallowed = ExpirationDate.ExpirationDate(testDate)
