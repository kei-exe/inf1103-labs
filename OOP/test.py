
from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


def test_factory() -> None:
    """Test product creation and invalid product types."""

    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    physical = ProductFactory.create(
        "physical", "P001", "Keyboard", 50.0, 10, supplier, 1.5
    )

    digital = ProductFactory.create(
        "digital", "D001", "Game", 20.0, 100, supplier, 2.0
    )

    assert isinstance(physical, PhysicalProduct)
    assert isinstance(digital, DigitalProduct)

    print("Physical product created successfully.")
    print("Digital product created successfully.")

    try:
        ProductFactory.create(
            "service", "S001", "Installation", 30.0, 5, supplier
        )
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    test_factory()