from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order_line import OrderLine


def test_validation() -> None:
    """Check that invalid product values raise errors."""
    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    product = PhysicalProduct(
        "P001", "Keyboard", 50.0, 10, 1.0, supplier
    )

    # Test invalid price
    try:
        PhysicalProduct("P002", "Mouse", -10.0, 5, 0.5, supplier)
        raise AssertionError("Negative price was accepted")
    except ValueError:
        print("Invalid price rejected.")

    # Test invalid stock
    try:
        DigitalProduct("D001", "Game", 20.0, -5, 2.0, supplier)
        raise AssertionError("Negative stock was accepted")
    except ValueError:
        print("Invalid stock rejected.")

    # Test invalid order quantity
    try:
        OrderLine(product, 0)
        raise AssertionError("Zero quantity was accepted")
    except ValueError:
        print("Invalid order quantity rejected.")

    # Test stock update
    try:
        product.update_stock(-3)
        raise AssertionError("Negative stock update was accepted")
    except ValueError:
        print("Invalid stock update rejected.")


if __name__ == "__main__":
    test_validation()