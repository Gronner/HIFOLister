#!/usr/bin/env python
"""Tests for the ElementInformation class."""
import sys
import os.path
sys.path.append(os.path.abspath('./hifolister'))
from ListElements import ElementInformation

class TestElementInformationConstructor:
    """Tests for a ElementInformation's constructor"""

    def test_createElementInformationWithoutDescription(self):
        """Creates a new ElementInformation without a description."""
        testName = 'TestName'

        elementInformationWithoutDescription = ElementInformation.ElementInformation(testName)

        assert elementInformationWithoutDescription.name == testName
        assert elementInformationWithoutDescription.description == ''


    def test_createElementInformationWithDescription(self):
        """Creates a new ElementInformation with a description."""
        testName = 'DescripedName'
        testDescription = 'This is an example of a describtion'


        elementInformationWithDescription = ElementInformation.ElementInformation(testName,
                                                                                  testDescription)

        assert elementInformationWithDescription.name == testName
        assert elementInformationWithDescription.description == testDescription

class TestElementInformationEqualTest:
    """Test the ElementInformation's == operator implementation."""

    def test_compareAgainstSelf(self):
        """Compares the ElementInformation object against it self."""
        testName = 'DescripedName'
        testDescription = 'This is an example of a description'

        OnlyElementInformationObject = ElementInformation.ElementInformation(testName,
                                                                             testDescription)

        assert OnlyElementInformationObject == OnlyElementInformationObject

    def test_compareAgainstOtherButEqual(self):
        testName = 'DescripedName'
        testDescription = 'This is an example of a description'

        ElementInformationObjectOne = ElementInformation.ElementInformation(testName,
                                                                            testDescription)
        ElementInformationObjectTwo = ElementInformation.ElementInformation(testName,
                                                                            testDescription)

        assert ElementInformationObjectOne == ElementInformationObjectTwo

    def test_compareAgainstOtherButDifferentName(self):
        testName1 = 'DescripedName'
        testName2 = 'OtherName'
        testDescription = 'This is an example of a description'

        ElementInformationObjectOne = ElementInformation.ElementInformation(testName1,
                                                                            testDescription)
        ElementInformationObjectTwo = ElementInformation.ElementInformation(testName2,
                                                                            testDescription)

        assert ElementInformationObjectOne != ElementInformationObjectTwo

    def test_compareAgainstOtherButDifferentDescription(self):
        testName = 'DescripedName'
        testDescription1 = 'This is an example of a description'
        testDescription2 = 'This is another example of a description'

        ElementInformationObjectOne = ElementInformation.ElementInformation(testName,
                                                                            testDescription1)
        ElementInformationObjectTwo = ElementInformation.ElementInformation(testName,
                                                                            testDescription2)

        assert ElementInformationObjectOne != ElementInformationObjectTwo

    def test_compareAgainstOtherAndTotalyDifferent(self):
        testName1 = 'DescripedName'
        testName2 = 'OtherName'
        testDescription1 = 'This is an example of a description'
        testDescription2 = 'This is another example of a description'

        ElementInformationObjectOne = ElementInformation.ElementInformation(testName1,
                                                                            testDescription1)
        ElementInformationObjectTwo = ElementInformation.ElementInformation(testName2,
                                                                            testDescription2)

        assert ElementInformationObjectOne != ElementInformationObjectTwo
