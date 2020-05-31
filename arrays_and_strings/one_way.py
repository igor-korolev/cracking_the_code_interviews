# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if
# they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

from collections import namedtuple

import pytest


def is_edited_once_or_zero(str1, str2):
    """
    Checks if two strings are one or zero edits away.

    :param str str1: First string.
    :param str str2: Second string.
    :return: Boolean True if strings has less or equal to one edits.
    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        return _is_one_edit_or_replace(str1, str2)
    elif len(str1) < len(str2):
        return _is_one_edit_or_insert(str1, str2)
    return _is_one_edit_or_insert(str2, str1)


def _is_one_edit_or_replace(str1, str2):
    """
    Helper function checks if two length equal strings are one or zero edits away.

    :param str str1: First string.
    :param str str2: Second string.
    :return: Boolean True if strings has less or equal to one edits.
    """
    is_edited = False
    for i, char in enumerate(str1):
        if char != str2[i] and is_edited:
            return False
        else:
            is_edited = True
    return True


def _is_one_edit_or_insert(str1, str2):
    """
    Helper function checks if two strings of different lengths are one or zero edits away.

    :param str str1: First string.
    :param str str2: Second string.
    :return: Boolean True if strings has less or equal to one edits.
    """
    edited = False
    bigger_str_index = 0
    for char in str1:
        if char != str2[bigger_str_index]:
            if edited:
                return False
            edited = True
            bigger_str_index += 2
            continue
        bigger_str_index += 1
    return True



# Testing:
Strings = namedtuple("Strings", ["original", "edited", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        Strings("pale", "ple", True),
        Strings("pales", "pale", True),
        Strings("pale", "bale", True),
        Strings("pale", "bake", False),
        Strings("pales", "pal", False),  # orig > edited
        Strings("pale", "paresis", False),  # orig < edited
        Strings("apple", "aple", True),  # orig < edited
        Strings("poool", "pppol", False),
        Strings("poool", "ppolop", False),
    ],
    ids=lambda s: f"Input: {s.original}-{s.edited}, Expected: {s.expected}",
)
def strings(request):
    return request.param


@pytest.mark.parametrize("func", [is_edited_once_or_zero])
def test_is_permutation(func, strings):
    result = func(strings.original, strings.edited)
    assert result is strings.expected, (
        f"{func.__name__} with '{strings.original}'-'{strings.edited}' as input returned {result}, "
        f"but {strings.expected} expected"
    )
