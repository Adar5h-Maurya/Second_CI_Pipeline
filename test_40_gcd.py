import importlib

module = importlib.import_module("40_gcd")


def test_gcd():
    assert module.gcd(12, 8) == 4


def test_coprime_numbers():
    assert module.gcd(7, 5) == 1


def test_one_number_is_zero():
    assert module.gcd(10, 0) == 10


def test_negative_numbers():
    assert module.gcd(-12, 8) == 4