"""
This program is a kata on decimal to roman numeral
conversion.
"""


def decimal_to_roman(decimal_value):
    """
    Convert a number from decimal to roman numeral
    """
    if decimal_value == 0:
        return ''
    elif decimal_value < 4:
        return 'I' + decimal_to_roman(decimal_value - 1)
    elif decimal_value == 4:
        return 'IV'
    elif decimal_value == 5:
        return 'V'
    elif decimal_value < 9:
        return 'V' + decimal_to_roman(decimal_value - 5)
    elif decimal_value == 9:
        return 'IX'
