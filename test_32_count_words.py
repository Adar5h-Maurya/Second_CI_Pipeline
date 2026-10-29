import importlib

module = importlib.import_module("32_count_words")


def test_count_words():
    assert module.count_words("Python is easy") == 3


def test_extra_spaces():
    assert module.count_words("  Python   is easy  ") == 3


def test_empty_sentence():
    assert module.count_words("") == 0