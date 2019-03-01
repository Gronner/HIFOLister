#!/usr/bin/env python
"""Tests for the ElementInformation class."""
import sys
sys.path.append(r'/home/felix/Documents/Projekte/HIFOLister/hifolister')
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
