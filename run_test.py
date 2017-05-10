
from decimalToRoman import toRomanNumeral

def testConvertZero():
    assert toRomanNumeral(0) is ''

def testConvertOne():
    assert toRomanNumeral(1) is "I"
