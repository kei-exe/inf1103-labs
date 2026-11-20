import pytest

from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


@pytest.fixture
def supplier() -> Supplier:
    """Create a supplier for testing."""
    return Supplier("S001", "Test Supplier", "test@example.com")


def test_create_physical_product(supplier: Supplier) -> None:
    """Check that the factory creates a physical product."""
    product = ProductFactory.create(
        "physical", "P001", "Desk Lamp", 25.0, 10, supplier, 2.5
    )

    assert isinstance(product, PhysicalProduct)


def test_create_digital_product(supplier: Supplier) -> None:
    """Check that the factory creates a digital product."""
    product = ProductFactory.create(
        "digital", "D001", "Photo Editor", 49.90, 100, supplier, 500.0
    )

    assert isinstance(product, DigitalProduct)


def test_unknown_product_type(supplier: Supplier) -> None:
    """Check that an unknown product type raises ValueError."""
    with pytest.raises(ValueError, match="Unknown product type"):
        ProductFactory.create(
            "service", "S001", "Installation", 30.0, 5, supplier
        )