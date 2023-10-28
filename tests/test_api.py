"""Tests API for solving problem Palindrome Number"""

import pytest

from leetcode_0009_palindrome_number import api


@pytest.mark.parametrize(
    ["result", "x"],
    (
        [True, 121],
        [False, -121],
        [False, 10],
    ),
)
def test_palindrome_number(result: bool, x: int) -> None:
    """Tests solution for problem Palindrome Number"""

    assert api.palindrome_number(x) == result
