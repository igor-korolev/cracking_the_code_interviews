# String Compression: Implement a method to perform basic string compression using the counts of
# repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should
# return the original string. You can assume the string has only uppercase and lowercase letters
# (a - z).
from collections import namedtuple

import pytest


def compress(string):
    if not string:
        return ""

    current = string[0]
    count = 1
    result = []
    for char in string[1:]:
        if char == current:
            count += 1
            continue
        else:
            result.append(f"{current}{count}")
            current = char
            count = 1
    result.append(f"{current}{count}")
    compressed = "".join(result)
    return compressed if len(compressed) < len(string) else string


print(compress("aabcccccaaa"))
print(compress("aabccaaa"))
