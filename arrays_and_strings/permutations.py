# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
from collections import namedtuple, Counter

import pytest


def is_perm1(str1, str2):
    """Convert both strings to counter dict and compare them."""
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


def is_perm2(str1, str2):
    """
    Convert first string to counter dict and iterate over second string checking if value of
    character is not zero, the decrement character occurrence.
    """
    if len(str1) != len(str2):
        return False
    str1_count = Counter(str1)
    for char in str2:
        if not str1_count[char]:
            return False
        str1_count[char] -= 1
    return True


def is_perm3(str1, str2):
    """Sort both strings and then compare them."""
    return sorted(str1) == sorted(str2)


# Testing:
Strings = namedtuple("Strings", ["str1", "str2", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        Strings("abcde", "edcba", True),
        Strings("abbccdd", "ccbbdda", True),
        Strings("abcde", "abc", False),
        Strings("abc", "abd", False),
        Strings("abcc", "abbc", False),
    ],
    ids=lambda s: f"Input: ({s.str1}, {s.str2}), Expected: {s.expected}",
)
def strings(request):
    return request.param


@pytest.mark.parametrize("func", [is_perm1, is_perm2, is_perm3])
def test_is_permutation(func, strings):
    result = func(strings.str1, strings.str2)
    assert result is strings.expected, (
        f"{func.__name__} with '{strings.str1}' and '{strings.str2}' as input returned {result}, "
        f"but {strings.expected} expected"
    )
