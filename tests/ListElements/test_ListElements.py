#!/usr/bin/env python
"""Tests for the ListElement"""
import pytest
import os.path
import sys
sys.path.append(os.path.abspath('./hifolister'))

from Date import ExpirationDate
from ListElements import ListElement

@pytest.fixture
def elementInformation():
    """Creates an ElementInformation object for a test."""
    from ListElements import ElementInformation
    return ElementInformation.ElementInformation("TestName", "TestDescription")

@pytest.fixture
def expirationDate():
    import time
    return ExpirationDate.ExpirationDate(int(time.time()))


class TestListConstructor:
    """Tests for a ListElement's constructor."""

    def test_createOneElementWithoutExpirationDate(self, elementInformation):
        """Creates a new ListElement without an expiration date."""
        expirationDateTestElement = ExpirationDate.NoExpirationDate
        nextElementTestElement = previousElementTestElement = None

        elementWithoutExpirationDate = ListElement.ListElement(elementInformation);

        assert elementWithoutExpirationDate.information == elementInformation
        assert elementWithoutExpirationDate.expirationDate == expirationDateTestElement
        assert elementWithoutExpirationDate.nextElement == nextElementTestElement
        assert elementWithoutExpirationDate.previousElement == previousElementTestElement

    def test_createOneElementWithoutExpirationDate(self, elementInformation, expirationDate):
        """Creates a new ListElement with an expiration date."""
        nextElementTestElement = previousElementTestElement = None

        elementWithExpirationDate = ListElement.ListElement(elementInformation,
                                                            expirationDate)

        assert elementWithExpirationDate.information is elementInformation
        assert elementWithExpirationDate.expirationDate is expirationDate
        assert elementWithExpirationDate.nextElement == nextElementTestElement
        assert elementWithExpirationDate.previousElement == previousElementTestElement
