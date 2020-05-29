# 1.1 Is Unique: Implement an algorithm to determine if a string_for_test has all unique characters. What if
# you cannot use additional data structures?

from collections import namedtuple

import pytest


def is_unique1(string):
    """Use set to get unique chars and compare its len to the len of the given string. O(n)."""
    return len(string) == len(set(string))


def is_unique2(string):
    """Compare every character of the string to every other character of the string. O( n^2)."""
    for i, letter1 in enumerate(string):
        for letter2 in string[i + 1 :]:
            if letter1 == letter2:
                return False
    return True


def is_unique3(string):
    """
    This solution assumes only ASCII characters. We create an array of boolean values, where the
    flag at index i indicates whether character i in the alphabet is contained in the string.
    """
    if len(string) > 128:
        return False
    char_set = [False] * 128
    for char in string:
        ascii_code = ord(char)
        if char_set[ascii_code]:
            return False
        char_set[ascii_code] = True
    return True


# Testing:
String = namedtuple("String", ["string", "expected"])


@pytest.fixture(scope="module", params=[String("abcde", True), String("abcdea", False)])
def string_for_test(request):
    return request.param


@pytest.mark.parametrize("func", [is_unique1, is_unique2, is_unique3])
def test_is_unique(func, string_for_test):
    result = func(string_for_test.string)
    assert result is string_for_test.expected, (
        f"{func.__name__} with '{string_for_test.string}' as input returned {result}, "
        f"but {string_for_test.expected} expected"
    )
