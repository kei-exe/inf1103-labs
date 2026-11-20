
from order import Order
from supplier import Supplier
from physical_product import PhysicalProduct
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)


def test_order_discount() -> None:
    """Test the different discounts applied to an order."""

    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    product = PhysicalProduct(
        "P001", "Keyboard", 50.0, 10, 1.0, supplier
    )

    order = Order("ORD001")
    order.add_order_line(product, 5)

    print("No Discount:", order.calculate_total())

    order.set_discount(PercentageDiscount(10))
    print("Percentage Discount:", order.calculate_total())

    order.set_discount(BulkDiscount(200, 20))
    print("Bulk Discount:", order.calculate_total())

    order.set_discount(StudentDiscount())
    print("Student Discount:", order.calculate_total())

    order.set_discount(NoDiscount())
    print("Reset Discount:", order.calculate_total())


if __name__ == "__main__":
    test_order_discount()