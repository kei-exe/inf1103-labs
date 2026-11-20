import pytest

from order import Order
from physical_product import PhysicalProduct
from supplier import Supplier
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)


@pytest.fixture
def product() -> PhysicalProduct:
    """Create a product for testing."""
    supplier = Supplier("S001", "Test Supplier", "test@example.com")
    return PhysicalProduct("P001", "Desk Lamp", 100.0, 10, 2.5, supplier)


def test_order_without_discount(product: PhysicalProduct) -> None:
    """Check that an order has no discount by default."""
    order = Order("O001")
    order.add_order_line(product, 2)

    assert order.calculate_total() == 200.0


def test_order_percentage_discount(product: PhysicalProduct) -> None:
    """Check that a percentage discount is applied."""
    order = Order("O001", PercentageDiscount(10))
    order.add_order_line(product, 2)

    assert order.calculate_total() == 180.0


def test_order_bulk_discount(product: PhysicalProduct) -> None:
    """Check that a bulk discount is applied."""
    order = Order("O001", BulkDiscount(150, 20))
    order.add_order_line(product, 2)

    assert order.calculate_total() == 180.0


def test_order_student_discount(product: PhysicalProduct) -> None:
    """Check that a student discount is applied."""
    order = Order("O001", StudentDiscount())
    order.add_order_line(product, 2)

    assert order.calculate_total() == 190.0


def test_change_discount(product: PhysicalProduct) -> None:
    """Check that an order's discount can be changed."""
    order = Order("O001")
    order.add_order_line(product, 2)

    assert order.calculate_total() == 200.0

    order.set_discount(PercentageDiscount(10))
    assert order.calculate_total() == 180.0

    order.set_discount(NoDiscount())
    assert order.calculate_total() == 200.0


def test_multiple_order_lines(product: PhysicalProduct) -> None:
    """Check that multiple order lines are calculated correctly."""
    order = Order("O001", PercentageDiscount(10))

    order.add_order_line(product, 2)
    order.add_order_line(product, 1)

    assert order.calculate_total() == 270.0


def test_empty_order() -> None:
    """Check that an empty order has a total of zero."""
    order = Order("O001")

    assert order.calculate_total() == 0.0


def test_invalid_order_quantity(product: PhysicalProduct) -> None:
    """Check that invalid quantities are rejected."""
    order = Order("O001")

    with pytest.raises(ValueError):
        order.add_order_line(product, 0)

    with pytest.raises(ValueError):
        order.add_order_line(product, -2)