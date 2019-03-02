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

@pytest.fixture
def listWithOneElement(emptyList, listElement):
    emptyList.insertElement(listElement)
    return emptyList

@pytest.fixture
def listWithMoreThanOneElement(emptyList, elementInformation):
    targetListSize = random.randint(3, 16)
    elementList = []
    for i in range(1, targetListSize):
        new_element = ListElement.ListElement(elementInformation)
        emptyList.insertElement(new_element)
        elementList.append(new_element)
    return emptyList, elementList, targetListSize


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
    
    def test_InsertMoreThanOneElement(self, listWithMoreThanOneElement):
        """Inserts multiple (2 up to 15) elements into the list."""
        testFifoList, elementList, targetListSize = listWithMoreThanOneElement

        assert len(testFifoList) == targetListSize - 1 # Off-by-one behaviour of Python's range()!

        checkElement = testFifoList.topElement
        assert checkElement.previousElement is None
        for i in range(1, targetListSize - 1):
            assert checkElement.nextElement is elementList[i]
            checkElement = checkElement.nextElement

        assert checkElement.nextElement is None

class TestPopTopListElement:
    """Tests to remove elements from the top of the list."""

    def test_PopFromEmptyList(self, emptyList):
        """Test to remove element from an empty list."""
        assert len(emptyList) == 0
        removedElement = emptyList.pop()
        assert removedElement == ListElement.NoListElement
        assert len(emptyList) == 0
        assert emptyList.topElement is None

    def test_PopFromListWithOneElement(self, listElement, listWithOneElement):
        """Test to remove the only element from a list."""
        assert len(listWithOneElement) == 1
        removedElement = listWithOneElement.pop()
        assert removedElement is listElement
        assert len(listWithOneElement) == 0

    def test_PopFromListWithMultipleElements(self, listWithMoreThanOneElement):
        testFifoList, elementList, targetListSize = listWithMoreThanOneElement

        assert len(testFifoList) == targetListSize - 1

        for i in range(0, targetListSize - 1):
            removedElement = testFifoList.pop()
            assert len(testFifoList) == targetListSize - 2 - i
            assert removedElement is elementList[i]
