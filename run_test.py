
from decimal_to_roman import decimal_to_roman

def testConvertZero():
    assert decimal_to_roman(0) is ''

def testConvertOne():
    assert decimal_to_roman(1) == "I"

def testConvertTwo():
    assert decimal_to_roman(2) == "II"
