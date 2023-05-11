from decimal import Decimal


def to_2_point_decimal(value: str):
    '''Convert string to Decimal with 2 places
    example:
    '123.456' -> Decimal()'123.456'
    '''
    return round(Decimal(value), 2)
