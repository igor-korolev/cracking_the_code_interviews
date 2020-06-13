# StringRotation:Assume you have a method isSubstring which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
# one call to isSubstring (e.g., "waterbottle" is a rotation of" erbottlewat").

from collections import namedtuple

import pytest


def is_substring(s1, s2):
    return s2 in s1


def is_rotation(s1, s2):
    """
    Checks if s1 string is a rotation of s2 string. The logic is: rotation means that we cut s1 into
    two parts, swap them and concatenate to get s2. To check this we can check that s2 is a
    substring of s1 + s1.

    :param s1: First original string.
    :param s2: Second string to check is it rotated.
    :return: True if s2 is a rotation of s1.
    """
    return len(s1) == len(s2) and is_substring(s1 + s1, s2)


# Testing:
Strings = namedtuple("Strings", ["s1", "s2", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        Strings("one", "two", False),
        Strings("one", "two", False),
        Strings("waterbottle", "erbottlewat", True),
    ],
    ids=lambda s: f"Input: {s.s1},{s.s2}, Expected: {s.expected}",
)
def strings(request):
    return request.param


@pytest.mark.parametrize("func", [is_rotation])
def test_is_rotation(func, strings):
    result = is_rotation(strings.s1, strings.s2)
    assert result is strings.expected, (
        f"{func.__name__} with '{strings.s1}', '{strings.s2}' as input returned {result}, "
        f"but {strings.expected} expected"
    )
