#!/usr/bin/env python
"""Tests for the ListElement"""
import os.path
import pytest
import random
import sys
sys.path.append(os.path.abspath('./hifolister'))

from Date import ExpirationDate
from ListElements import PriorityElement

@pytest.fixture
def elementInformation():
    """Creates an ElementInformation object for a test."""
    from ListElements import ElementInformation
    return ElementInformation.ElementInformation("TestName", "TestDescription")

class TestPriorityElementConstructor:
    """Test for the PriorityElement's constructor."""

    def test_createOneElementWithPositivePriority(self, elementInformation):
        expirationDateTestElement = ExpirationDate.NoExpirationDate
        nextElementTestElement = previousElementTestElement = None
        positiveTestPriority = random.randint(1, sys.maxsize)

        testElement = PriorityElement.PriorityElement(elementInformation, positiveTestPriority)

        assert testElement.information == elementInformation
        assert testElement.expirationDate == expirationDateTestElement
        assert testElement.nextElement == nextElementTestElement
        assert testElement.previousElement == previousElementTestElement
        assert testElement.priority == positiveTestPriority

    def test_createOneElementWithNegativePriority(self, elementInformation):
        expirationDateTestElement = ExpirationDate.NoExpirationDate
        nextElementTestElement = previousElementTestElement = None
        negativeTestPriority = random.randint(-sys.maxsize, 0)

        with pytest.raises(ValueError):
            testElement = PriorityElement.PriorityElement(elementInformation, negativeTestPriority)
