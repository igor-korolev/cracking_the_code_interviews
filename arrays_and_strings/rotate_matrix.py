# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

from collections import namedtuple

import pytest

# [1,2,3,4]     [13,9,5,1]
# [5,6,7,8]  -> [14,10,6,2]
# [9,10,11,12]  [15,11,7,3]
# [13,14,15,16] [16,12,8,4]

# [1, 2, 3, 4, 5]           [21,16,11,6,1]
# [6, 7, 8, 9, 10]          [22,17,12,7,2]
# [11, 12, 13, 14, 15]  ->  [23,18,13,8,3]
# [16, 17, 18, 19, 20]      [24,19,14,9,4]
# [21, 22, 23, 24, 25]      [25,20,15,10,5]


def rotate(matrix):
    """
    Rotate the matrix in place by 90 degrees.

    :param list matrix: Matrix represented by two-dimensional list.
    :return: Rotated matrix.
    :raises ValueError: In case of empty or non-NxN matrix.
    """
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("NxN matrix is required")

    swapped_elems_in_layer = len(matrix) - 1  # Iterate over layer elements, except the last one
    for layer in range(len(matrix) // 2):
        for i in range(layer, swapped_elems_in_layer):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-1 - i][layer]  # left -> top
            matrix[-1 - i][layer] = matrix[-1 - layer][-1 - i]  # bottom -> left
            matrix[-1 - layer][-1 - i] = matrix[i][-1 - layer]  # right -> bottom
            matrix[i][-1 - layer] = top  # top -> right
        swapped_elems_in_layer -= 1

    print(*matrix, sep="\n")
    return matrix


def gen_matrix(n):
    """
    Helper function that generates NxN matrix by the given number.

    :param int n: Number to make a matrix.
    :return: Matrix, represented as a two-dimensional list.
    """
    return [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]


# Testing:
Matrix = namedtuple("Matrix", ["value", "expected"])


@pytest.fixture(
    scope="module",
    params=[
        Matrix(gen_matrix(4), [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]),
        Matrix(
            gen_matrix(5),
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ],
    ids=lambda s: f"Input: {s.value}, Expected: {s.expected}",
)
def matrix(request):
    return request.param


@pytest.mark.parametrize("func", [rotate])
def test_rotate_matrix(func, matrix):
    result = func(matrix.value)
    assert result == matrix.expected, (
        f"{func.__name__} with '{matrix.value}' as input returned {result}, "
        f"but {matrix.expected} expected"
    )
