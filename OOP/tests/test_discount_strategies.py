import pytest

from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)


def test_no_discount() -> None:
    """Check that the total stays unchanged."""
    strategy = NoDiscount()
    assert strategy.apply(250.0) == 250.0


def test_percentage_discount() -> None:
    """Check a 10% discount."""
    strategy = PercentageDiscount(10)
    assert strategy.apply(250.0) == 225.0


def test_bulk_discount() -> None:
    """Check a bulk discount above the threshold."""
    strategy = BulkDiscount(200, 20)
    assert strategy.apply(250.0) == 230.0


def test_student_discount() -> None:
    """Check a 5% student discount."""
    strategy = StudentDiscount()
    assert strategy.apply(250.0) == 237.5