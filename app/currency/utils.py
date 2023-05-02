from decimal import Decimal


def to_2_places_decimal(value: str) -> Decimal:
    '''Convert string to Decimal with 2 places
    example:
    '123.456' -> Decimal()'123.456'
    '''
    return round(Decimal(value), 2)
