# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

from collections import namedtuple

import pytest


def nullify(matrix):
    """
    Iterates over each row and over each element inside that row, then checks if the element is a
    zero. If it is zero remembers their indexes. Finally iterates over saved indexes and sets
    corresponding rows and columns to 0.  O(n^2)

    :param list matrix: MxN matrix.
    :return: Nullified matrix.
    """
    rows_with_zeros = set()
    columns_with_zeros = set()

    for row_zero_index, row in enumerate(matrix):
        for e_index, elem in enumerate(row):
            if elem == 0:
                rows_with_zeros.add(row_zero_index)
                columns_with_zeros.add(e_index)

    for r in rows_with_zeros:  # Nullify rows
        for i in range(len(matrix[r])):
            matrix[r][i] = 0

    for c in columns_with_zeros:  # Nullify columns
        for row in matrix:
            row[c] = 0

    return matrix


# Testing:
Matrix = namedtuple("Matrix", ["value", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        Matrix([[1, 2, 3], [3, 0, 5], [6, 4, 0]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
        Matrix(
            [[1, 2, 3, 9, 0], [3, 0, 5, 1, 1], [6, 0, 5, 7, 99]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
        ),
        Matrix(
            [[1, 2, 3, 9, 0], [3, 0, 5, 1, 1], [6, 9, 5, 7, 99], [5, 0, 3, 2, 3]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [6, 0, 5, 7, 0], [0, 0, 0, 0, 0]],
        ),
    ],
    ids=lambda s: f"Input: {s.value}, Expected: {s.expected}",
)
def matrix(request):
    return request.param


@pytest.mark.parametrize("func", [nullify])
def test_func_name(func, matrix):
    result = func(matrix.value)
    assert result == matrix.expected, (
        f"{func.__name__} with '{matrix.value}' as input returned {result}, "
        f"but {matrix.expected} expected"
    )
