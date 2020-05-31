# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a
# palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE Input: Tact Coa, Output: True (permutations: "taco cat"; "atco cta" etc.)
from collections import namedtuple, Counter

import pytest


def has_palindrome_perm1(string):
    """
    Finds out if a given string is a permutation of a palindrome. O(n)
    1) Make a map: character - its frequency
    2) Iterate over the map and checks for odd frequencies. If odd frequency already seen -
    return False immediately

    :param str string: String to check.
    :return: Boolean True if a string is a palindrome permutation.
    """
    if not string:
        return False
    clean_string = string.replace(" ", "").lower()
    letters_counter = Counter(clean_string)

    seen_odd = False
    for occurr in letters_counter.values():
        if occurr % 2 != 0:
            if seen_odd:
                return False
            seen_odd = True
    return True


def has_palindrome_perm2(string):
    """
    Finds out if a given string is a permutation of a palindrome. O(n)
    Filter all characters that have odd occurrence in a given string and check that it's <= 1.

    :param str string: String to check.
    :return: Boolean True if a string is a palindrome permutation.
    """
    clean_str = string.replace(" ", "").lower()
    return bool(string) and len({char for char in clean_str if clean_str.count(char) % 2 != 0}) <= 1


# Testing:
String = namedtuple("String", ["value", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        String("", False),
        String("a", True),
        String("aa", True),
        String("aaa", True),
        String("aabbcc", True),
        String("AabbccC", True),
        String("aabbcccd", False),
        String("Tact Coa", True),
    ],
    ids=lambda s: f"Input: {s.value}, Expected: {s.expected}",
)
def string(request):
    return request.param


@pytest.mark.parametrize("func", [has_palindrome_perm1, has_palindrome_perm2])
def test_is_permutation(func, string):
    result = func(string.value)
    assert result is string.expected, (
        f"{func.__name__} with '{string.value}' as input returned {result}, "
        f"but {string.expected} expected"
    )
