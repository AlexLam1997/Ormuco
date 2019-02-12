from Q2Version import VersionCompare
from Q2Version import EnumResponse
from unittest import TestCase

class VersionCompareTest(TestCase):

    def test_SimpleVersionLesser(self):
        result = VersionCompare.compareVersion("1.1","1.2")
        self.assertEqual(result, EnumResponse.Response.LESSER)

    def test_MediumVersionLesser(self):
        result = VersionCompare.compareVersion("2", "3")
        self.assertEqual(result, EnumResponse.Response.LESSER)

    def test_HardVersionLesser(self):
        result = VersionCompare.compareVersion("0.000", "1.0")
        self.assertEqual(result, EnumResponse.Response.LESSER)

    def test_HarderVersionGreater(self):
        result = VersionCompare.compareVersion("10.11", "9.2412")
        self.assertEqual(result, EnumResponse.Response.GREATER)

    def test_MedVersionGreater(self):
        result = VersionCompare.compareVersion("15", "10")
        self.assertEqual(result, EnumResponse.Response.GREATER)

    def test_HardVersionGreater(self):
        result = VersionCompare.compareVersion("15", "10.000")
        self.assertEqual(result, EnumResponse.Response.GREATER)

    def test_SimpleVersionEqual(self):
        result = VersionCompare.compareVersion("20.2", "20.2")
        self.assertEqual(result, EnumResponse.Response.EQUAL)

    def test_MedVersionEqual(self):
        result = VersionCompare.compareVersion("0", "0")
        self.assertEqual(result, EnumResponse.Response.EQUAL)

    def test_HarderVersionEqual(self):
        result = VersionCompare.compareVersion("0", "0.00")
        self.assertEqual(result, EnumResponse.Response.EQUAL)


