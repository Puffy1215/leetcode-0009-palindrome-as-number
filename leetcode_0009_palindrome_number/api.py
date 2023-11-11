"""API for solving problem Palindrome Number"""

import math
from typing import cast

X_MAX = 2**31 - 1
X_MIN = -(2**31)


def _check_preconditions(x: int) -> bool:
    return X_MIN <= x <= X_MAX


def _digits(x: int) -> int:
    return math.floor(math.log10(abs(x)) + 1) if x else 1


def _get_digit(x: int, i: int) -> int:
    return cast(int, abs(x // 10**i)) % 10


def palindrome_number(x: int) -> bool:
    """Solves problem Palindrome Number"""

    assert _check_preconditions(x)

    pass
