from typing import Union


def validate_int(value) -> Union[int, None]:
    """
    Returns positive int value else None
    :param value: str
    :return: int or None
    :raises: ValueError
    """
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        if value < 1:
            return False
        return value


def validate_float(value) -> Union[float, None]:
    """
    Returns positive int value else None
    :param value: str
    :return: float or None
    :raises: ValueError
    """
    try:
        value = float(value)
    except ValueError:
        return False
    else:
        if value < 1:
            return False
        return value
