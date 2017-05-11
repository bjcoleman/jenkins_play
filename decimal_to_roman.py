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
    elif decimal_value == 2:
        return 'II'
    return 'I'