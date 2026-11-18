"""Standalone check (no pytest) for lilavati.safe_exec allowing try/except.

Run directly: python3 tests/test_safe_exec_try_except.py
"""
from lilavati.safe_exec import check_program, run


def test_try_except_zero_division_accepted():
    code = """
def solution():
    a, b = 10, 0
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0
"""
    ok, reason = check_program(code)
    assert ok, f"expected accepted, got rejected: {reason}"
    assert run(code) == 0.0


def test_assert_inside_try_except_accepted():
    code = """
def solution():
    x = 5
    try:
        assert x > 10
        return 1.0
    except AssertionError:
        return 2.0
"""
    ok, reason = check_program(code)
    assert ok, f"expected accepted, got rejected: {reason}"
    assert run(code) == 2.0


def test_dangerous_import_inside_try_still_rejected():
    code = """
def solution():
    try:
        import os
        return 1
    except ZeroDivisionError:
        return 2
"""
    ok, reason = check_program(code)
    assert not ok
    assert "import" in reason


if __name__ == "__main__":
    test_try_except_zero_division_accepted()
    test_assert_inside_try_except_accepted()
    test_dangerous_import_inside_try_still_rejected()
    print("OK")
