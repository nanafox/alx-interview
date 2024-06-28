#!/usr/bin/python3

from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Generate a Pascal's triangle with n rows.

    Args:
        n: An integer representing the number of rows in the Pascal's triangle.

    Returns:
        A list of lists representing the Pascal's triangle with n rows.

    Tests:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

        >>> pascal_triangle(0)
        []

        >>> pascal_triangle(1)
        [[1]]

        >>> pascal_triangle(2)
        [[1], [1, 1]]

        >>> pascal_triangle("not an integer")
        Traceback (most recent call last):
            ...
        TypeError: n must be an integer
    """

    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        row.extend(
            triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i)
        )
        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle: List[List[int]]):
    """
    Print the triangle

    Tests:
        >>> print_triangle(pascal_triangle(5))
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]

        >>> print_triangle(pascal_triangle(0))  # nothing is printed for this
        >>> print_triangle(pascal_triangle(2))
        [1]
        [1,1]
        >>> print_triangle(pascal_triangle(1))
        [1]
    """
    for row in triangle:
        print(f'[{",".join([str(x) for x in row])}]')


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
