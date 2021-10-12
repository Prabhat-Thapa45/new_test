""" this module tests validate_input.py """

import pytest
from src.utility.validate_input import validate_int, validate_float


@pytest.fixture
def test_data():
    return [1, 3], [-1, "as", 0]


def test_validate_int(test_data):
    for i in test_data[0]:
        assert validate_int(i) == i


def test_validate_int_negative(test_data):
    for i in test_data[1]:
        assert not validate_int(i)


def test_validate_float(test_data):
    for i in test_data[0]:
        assert validate_float(i) == i


def test_validate_float_negative(test_data):
    for i in test_data[1]:
        assert not validate_float(i)
