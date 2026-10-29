import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_two_positions():
    assert module.rotate_string("hello", 2) == "lohel"


def test_rotate_one_position():
    assert module.rotate_string("hello", 1) == "ohell"


def test_rotate_full_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_empty_string():
    assert module.rotate_string("", 2) == ""