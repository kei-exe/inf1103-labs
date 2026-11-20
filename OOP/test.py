from inventory import Inventory
from supplier import Supplier
from main import get_positive_float, load_products


def test_csv_loading() -> None:
    """Test loading products from a CSV file."""
    inventory = Inventory()
    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    load_products("products.csv", inventory, supplier)
    print(f"Products loaded: {len(inventory.get_all_products())}")


if __name__ == "__main__":
    test_csv_loading()