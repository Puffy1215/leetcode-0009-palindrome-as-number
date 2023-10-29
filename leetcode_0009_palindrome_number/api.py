"""API for solving problem Palindrome Number"""

X_MAX = 2**31 - 1
X_MIN = -(2**31)


def _check_preconditions(x: int) -> bool:
    return X_MIN <= x <= X_MAX


def palindrome_number(x: int) -> bool:
    """Solves problem Palindrome Number"""

    assert _check_preconditions(x)

    pass
