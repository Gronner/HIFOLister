#!/usr/bin/env python
"""Test for the ListInformation class."""
import sys
import os.path
sys.path.append(os.path.abspath('./hifolister'))
from HifoLists import ListInformation

class TestListInformationConstructor:
    """Tests for a ListInformation's constructor"""

    def test_createListInformationWithoutDescription(self):
        """Creates a new ListInformation without a description."""
        testName = 'TestName'

        elementInformationWithoutDescription = ListInformation.ListInformation(testName)

        assert elementInformationWithoutDescription.name == testName
        assert elementInformationWithoutDescription.description == ''


    def test_createListInformationWithDescription(self):
        """Creates a new ListInformation with a description."""
        testName = 'DescripedName'
        testDescription = 'This is an example of a describtion'


        elementInformationWithDescription = ListInformation.ListInformation(testName,
                                                                            testDescription)

        assert elementInformationWithDescription.name == testName
        assert elementInformationWithDescription.description == testDescription

class TestListInformationEqualTest:
    """Test the ListInformation's == operator implementation."""

    def test_compareAgainstSelf(self):
        """Compares the ListInformation object against it self."""
        testName = 'DescripedName'
        testDescription = 'This is an example of a description'

        OnlyListInformationObject = ListInformation.ListInformation(testName,
                                                                    testDescription)

        assert OnlyListInformationObject == OnlyListInformationObject

    def test_compareAgainstOtherButEqual(self):
        testName = 'DescripedName'
        testDescription = 'This is an example of a description'

        ListInformationObjectOne = ListInformation.ListInformation(testName,
                                                                   testDescription)
        ListInformationObjectTwo = ListInformation.ListInformation(testName,
                                                                   testDescription)

        assert ListInformationObjectOne == ListInformationObjectTwo

    def test_compareAgainstOtherButDifferentName(self):
        testName1 = 'DescripedName'
        testName2 = 'OtherName'
        testDescription = 'This is an example of a description'

        ListInformationObjectOne = ListInformation.ListInformation(testName1,
                                                                   testDescription)
        ListInformationObjectTwo = ListInformation.ListInformation(testName2,
                                                                   testDescription)

        assert ListInformationObjectOne != ListInformationObjectTwo

    def test_compareAgainstOtherButDifferentDescription(self):
        testName = 'DescripedName'
        testDescription1 = 'This is an example of a description'
        testDescription2 = 'This is another example of a description'

        ListInformationObjectOne = ListInformation.ListInformation(testName,
                                                                   testDescription1)
        ListInformationObjectTwo = ListInformation.ListInformation(testName,
                                                                   testDescription2)

        assert ListInformationObjectOne != ListInformationObjectTwo

    def test_compareAgainstOtherAndTotalyDifferent(self):
        testName1 = 'DescripedName'
        testName2 = 'OtherName'
        testDescription1 = 'This is an example of a description'
        testDescription2 = 'This is another example of a description'

        ListInformationObjectOne = ListInformation.ListInformation(testName1,
                                                                   testDescription1)
        ListInformationObjectTwo = ListInformation.ListInformation(testName2,
                                                                   testDescription2)

        assert ListInformationObjectOne != ListInformationObjectTwo
