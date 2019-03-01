#!/usr/bin/env python
"""Test for the HIFOList Class."""
import pytest
import random
import os.path
import sys
sys.path.append(os.path.abspath('./hifolister'))

from HifoLists import FifoList
from ListElements import ListElement

@pytest.fixture
def listInformation():
    from HifoLists import ListInformation
    return ListInformation.ListInformation('TestList', 'TestListDescription')

@pytest.fixture
def emptyList(listInformation):
    return FifoList.FifoList(listInformation)

@pytest.fixture
def elementInformation():
    from ListElements import ElementInformation
    return ElementInformation.ElementInformation('TestElement', 'TestElementDescription')

@pytest.fixture
def listElement(elementInformation):
    return ListElement.ListElement(elementInformation)


class TestFifoListConstructor:
    """Tests for the FifoLists Constructor."""

    def test_CreateFifoList(self, listInformation):
        """Creates an empty FIFO list."""
        newList = FifoList.FifoList(listInformation)

        assert newList.information is listInformation
        assert newList.topElement is None
        assert len(newList) == 0

class TestInsertListElement:
    """Tests the insertion of list elements into the List."""

    def test_InsertFirstElement(self, emptyList, listElement):
        """Inserts the first Element into the list."""
        emptyList.insertElement(listElement)

        assert len(emptyList) == 1
        assert emptyList.topElement is listElement
    
    def test_InsertMoreThanOneElement(self, emptyList, elementInformation):
        """Inserts multiple (2 up to 15) elements into the list."""
        targetListSize = random.randint(3, 16)
        elementList = []
        for i in range(1, targetListSize):
            new_element = ListElement.ListElement(elementInformation)
            emptyList.insertElement(new_element)
            elementList.append(new_element)

        assert len(emptyList) == targetListSize - 1 # Off-by-one behaviour of Python's range()!

        checkElement = emptyList.topElement
        assert checkElement.previousElement is None
        for i in range(1, targetListSize - 1):
            assert checkElement.nextElement is elementList[i]
            checkElement = checkElement.nextElement

        assert checkElement.nextElement is None
