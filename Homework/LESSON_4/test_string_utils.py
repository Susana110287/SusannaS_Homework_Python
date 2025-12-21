import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Тесты для метода capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
    ("123abc", "123abc"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("\t", "\t"),
    ("\n", "\n"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Тесты для метода trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("    hello", "hello"),
    (" python ", "python "),
    ("  тест  ", "тест  "),
    (" 123abc ", "123abc "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("\t", "\t"),
    ("\n", "\n"),
    ("no_spaces", "no_spaces"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Тесты для метода contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("Hello World", "o", True),
    ("Python", "y", True),
    ("тест", "е", True),
    ("123abc", "3", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("   ", "x", False),
    ("123", "a", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Тесты для метода delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Hello World", "l", "Heo Word"),
    ("Python", "th", "Pyon"),
    ("тест", "е", "тст"),
    ("123abc", "12", "3abc"),
    ("aabbcc", "bb", "aacc"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),
    ("test", "", "test"),
    ("abc", "xyz", "abc"),
    ("   ", "x", "   "),
    ("123", "abc", "123"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
