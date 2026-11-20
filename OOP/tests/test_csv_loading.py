from main import load_products
from inventory import Inventory
from supplier import Supplier


def test_valid_csv(tmp_path, capsys) -> None:
    """Check that valid products are loaded."""
    csv_file = tmp_path / "products.csv"
    csv_file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,P001,Desk Lamp,25.00,10\n"
        "digital,D001,Photo Editor,49.90,100\n"
    )

    inventory = Inventory()
    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    load_products(str(csv_file), inventory, supplier)

    output = capsys.readouterr().out

    assert len(inventory.get_all_products()) == 2
    assert "Loaded: Desk Lamp" in output
    assert "Loaded: Photo Editor" in output
    assert "Load attempt finished." in output

def test_invalid_csv_rows(tmp_path, capsys) -> None:
    """Check that invalid rows are skipped."""
    csv_file = tmp_path / "products.csv"
    csv_file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,P001,Desk Lamp,25.00,10\n"
        "service,S001,Installation,30.00,5\n"
        "physical,P002,Office Chair,abc,3\n"
        "digital,D001,Photo Editor,49.90,100\n"
    )

    inventory = Inventory()
    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    load_products(str(csv_file), inventory, supplier)

    output = capsys.readouterr().out

    assert len(inventory.get_all_products()) == 2
    assert "Loaded: Desk Lamp" in output
    assert "Loaded: Photo Editor" in output
    assert "Skipping invalid product: Unknown product type: service" in output
    assert "Skipping invalid product: could not convert string to float" in output
    assert "Load attempt finished." in output

def test_missing_csv(tmp_path, capsys) -> None:
    """Check that a missing file is handled gracefully."""
    csv_file = tmp_path / "missing.csv"

    inventory = Inventory()
    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    load_products(str(csv_file), inventory, supplier)

    output = capsys.readouterr().out

    assert len(inventory.get_all_products()) == 0
    assert "File not found:" in output
    assert "Load attempt finished." in output