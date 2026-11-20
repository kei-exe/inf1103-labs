import pytest

from physical_product import PhysicalProduct
from order_line import OrderLine
from supplier import Supplier


@pytest.fixture
def supplier() -> Supplier:
    """Create a supplier for testing."""
    return Supplier("S001", "Test Supplier", "test@example.com")


@pytest.fixture
def product(supplier: Supplier) -> PhysicalProduct:
    """Create a valid product for testing."""
    return PhysicalProduct("P001", "Desk Lamp", 25.0, 10, 2.5, supplier)


def test_valid_product(product: PhysicalProduct) -> None:
    """Check that a valid product can be created."""
    assert isinstance(product, PhysicalProduct)


def test_zero_price(supplier: Supplier) -> None:
    """Check that a product cannot have a zero price."""
    with pytest.raises(ValueError):
        PhysicalProduct("P001", "Desk Lamp", 0, 10, 2.5, supplier)


def test_negative_price(supplier: Supplier) -> None:
    """Check that a product cannot have a negative price."""
    with pytest.raises(ValueError):
        PhysicalProduct("P001", "Desk Lamp", -25.0, 10, 2.5, supplier)


def test_negative_stock(supplier: Supplier) -> None:
    """Check that a product cannot have negative stock."""
    with pytest.raises(ValueError):
        PhysicalProduct("P001", "Desk Lamp", 25.0, -5, 2.5, supplier)


def test_negative_stock_update(product: PhysicalProduct) -> None:
    """Check that stock cannot be updated to a negative value."""
    with pytest.raises(ValueError):
        product.update_stock(-5)


def test_zero_order_quantity(product: PhysicalProduct) -> None:
    """Check that an order quantity cannot be zero."""
    with pytest.raises(ValueError):
        OrderLine(product, 0)


def test_negative_order_quantity(product: PhysicalProduct) -> None:
    """Check that an order quantity cannot be negative."""
    with pytest.raises(ValueError):
        OrderLine(product, -3)


def test_valid_order_quantity(product: PhysicalProduct) -> None:
    """Check that a valid order quantity is accepted."""
    order_line = OrderLine(product, 3)

    assert order_line.calculate_subtotal() == 75.0