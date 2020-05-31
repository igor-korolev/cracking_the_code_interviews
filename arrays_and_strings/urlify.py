# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the
# string has sufficient space at the end to hold the additional characters,and that you are given
# the "true" length of the string. (Note: If implementing in Java,please use a character array so
# that you can perform this operation in place.)
# EXAMPLE:
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"
from collections import namedtuple

import pytest


def urlify1(string, length):
    return string[:length].replace(" ", "%20")


def urlify2(string, length):
    return "".join(char if char != " " else "%20" for char in string[:length])


# Testing:
String = namedtuple("String", ["string", "length", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        String("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        String("Mr John Smith    ", 14, "Mr%20John%20Smith%20"),
        String(" Mr John Smith ", 15, "%20Mr%20John%20Smith%20"),
    ],
    ids=lambda string: string[0]
)
def string(request):
    return request.param


@pytest.mark.parametrize("func", [urlify1, urlify2])
def test_urlify(func, string):
    result = func(string.string, string.length)
    assert result == string.expected, (
        f"{func.__name__} with '{string.string}' as input returned {result}, "
        f"but {string.expected} expected"
    )
