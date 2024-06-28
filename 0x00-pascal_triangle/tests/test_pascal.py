import os
import sys
from contextlib import redirect_stdout
from io import StringIO

import pytest

sys.path.append(os.path.abspath(os.path.join("0x00-pascal_triangle")))

pascal_triangle = __import__("0-pascal_triangle").pascal_triangle
print_triangle = __import__("0-pascal_triangle").print_triangle


@pytest.mark.parametrize(
    "n, expected",
    [
        (
            5,
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        ),  # Happy path
        (0, []),  # Edge case: zero rows
        (1, [[1]]),  # Edge case: one row
        (2, [[1], [1, 1]]),  # Edge case: two rows
    ],
    ids=[
        "five_rows",
        "zero_rows",
        "one_row",
        "two_rows",
    ],
)
def test_pascal_triangle_happy_path(n, expected):
    """Test valid inputs for the pascal_triangle function."""
    result = pascal_triangle(n)

    assert result == expected


@pytest.mark.parametrize(
    "n, expected_exception, expected_message",
    [
        (
            "not an integer",
            TypeError,
            "n must be an integer",
        ),  # Error case: non-integer input
        (-1, None, []),  # Edge case: negative input
    ],
    ids=[
        "non_integer_input",
        "negative_input",
    ],
)
def test_pascal_triangle_error_cases(n, expected_exception, expected_message):
    """Test function for the pascal_triangle function with error cases."""
    if expected_exception:
        with pytest.raises(expected_exception) as exc_info:
            pascal_triangle(n)
        assert str(exc_info.value) == expected_message
    else:
        result = pascal_triangle(n)

        assert result == expected_message


@pytest.mark.parametrize(
    "n, expected",
    [
        (
            10,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1],
                [1, 7, 21, 35, 35, 21, 7, 1],
                [1, 8, 28, 56, 70, 56, 28, 8, 1],
                [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
            ],
        ),  # Larger number of rows
    ],
    ids=[
        "ten_rows",
    ],
)
def test_pascal_triangle_bigger_numbers(n, expected):
    """Test function for the pascal_triangle function with larger numbers."""
    result = pascal_triangle(n)
    assert result == expected


@pytest.mark.parametrize(
    "triangle, expected_output",
    [
        (
            pascal_triangle(5),
            "[1]\n[1,1]\n[1,2,1]\n[1,3,3,1]\n[1,4,6,4,1]\n",
        ),  # happy path
        (pascal_triangle(0), ""),  # edge case: zero rows
        (pascal_triangle(2), "[1]\n[1,1]\n"),  # small triangle
        (pascal_triangle(1), "[1]\n"),  # single row
    ],
    ids=[
        "happy_path_5_rows",
        "edge_case_zero_rows",
        "small_triangle_2_rows",
        "single_row",
    ],
)
def test_print_triangle(triangle, expected_output):
    """
    Test function for the print_triangle function.
    """
    # Act
    f = StringIO()
    with redirect_stdout(f):
        print_triangle(triangle)
    output = f.getvalue()

    # Assert
    assert output == expected_output
