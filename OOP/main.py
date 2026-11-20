# external
import os
import json
import csv

# classes
from inventory import Inventory
from supplier import Supplier
from product import Product
from product_factory import ProductFactory

def display_menu() -> None:
    """Display the inventory menu."""
    print("\n------------- MENU -------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------------")

def display_input() -> int | None:
    """Read and validate the selected menu option."""
    displayInput: str = input("\nEnter option: ").strip()

    # check if -ve
    if displayInput.startswith("-") and displayInput[1:].isdigit() or not displayInput.isdigit():
        print("Please enter a valid menu option.")
        return None

    return int(displayInput)

def get_positive_float(prompt: str) -> float:
    """Keep asking until a valid positive number is entered."""
    while True:
        try:
            value: float = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def get_valid_input() -> tuple[str, str, float, int, float] | None:
    """Collect and validate details for a new product."""
    # select product type
    print("Select Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type: str = input("Enter product type: ").strip()

    match product_type:
        case "1":
            print("Physical Product selected.")
            extra_value: str = input("Enter weight (kg): ").strip()
        case "2":
            print("Digital Product selected.")
            extra_value: str = input("Enter download size (MB): ").strip()
        case _:
            print("Invalid product type.")
            return None

    # validation for extra value
    try:
        extra_value = float(extra_value)

        if extra_value < 0:
            print("Value cannot be negative.")
            return None

    except ValueError:
        print("Please input a valid number.")
        return None
    
    # name input
    stockName: str = input("Product Name: ").strip()
    
    #check empty
    if not stockName:
        print("Product name cannot be empty.")
        return None
    # check if name contains only letters and spaces
    elif not stockName.replace(" ", "").isalpha():
        print("Product name must contain only letters.")
        return None

    # Price input
    stockPrice: float = get_positive_float("Product Price: $")

    # qty input    
    stockQty: str = input("Stock Quantity: ")

    # check if -ve
    if stockQty.startswith("-") and stockQty[1:].isdigit():
        print("Stock quantity cannot be negative.")
        return None
    #check if not digit
    elif not stockQty.isdigit():
        print("Please enter a valid number for stock quantity.")
        return None

    return product_type, stockName, stockPrice, int(stockQty), extra_value

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    """Load valid products from a CSV file into the inventory."""
    try:
        file = open(path, "r", newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"File not found: {path}")

    else:
        with file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    product_type: str = row["product_type"]
                    product_id: str = row["product_id"]
                    name: str = row["name"]
                    price: float = float(row["price"])
                    stock: int = int(row["stock_quantity"])

                    product: Product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        price,
                        stock,
                        supplier
                    )

                    inventory.add_product(product)
                    print(f"Loaded: {name}")

                except (ValueError, KeyError, TypeError) as error:
                    print(f"Skipping invalid product: {error}")

    finally:
        print("Load attempt finished.")

def load_inventory(inventory: Inventory) -> None:
    """Load saved products from inventory.json."""
    if not os.path.exists("inventory.json"):
        return

    try:
        with open("inventory.json", "r", encoding="utf-8") as file:
            data: list[dict] = json.load(file)

        for item in data:
            supplier_data = item.get("supplier")

            if supplier_data is None:
                supplier = Supplier(
                    "S000",
                    "Legacy Supplier",
                    "unknown@example.com"
                )
            else:
                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

            product_type: str = item["product_type"]

            if product_type == "physical":
                extra_value: float = float(item["weight"])
            elif product_type == "digital":
                extra_value = float(item["download_size"])
            else:
                print("Unknown product type. Skipping product.")
                continue

            product: Product = ProductFactory.create(
                product_type,
                item["product_id"],
                item["name"],
                float(item["price"]),
                int(item["stock"]),
                supplier,
                extra_value
            )

            inventory.add_product(product)

    except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError) as error:
        print(f"Unable to load inventory: {error}")

def save_inventory(inventory: Inventory) -> None:
    """Save all products to the JSON inventory file."""
    data: list[dict[str, object]] = []

    for product in inventory.get_all_products():
        # Append dictionary to data
        data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

# case functions
def handle_display_all(inventory: Inventory) -> None:
    """Display all products currently in the inventory."""
    print("\nCurrent Inventory")
    print("=======================================================")
    inventory.display_all()
    print("=======================================================")

def handle_add_product(inventory: Inventory) -> None:
    """Collect product details and add a new product."""
    print("\nAdd New Product") # header
    print("==================") # separator line

    # Get user inputs
    new_order: tuple[str, str, float, int, float] | None = get_valid_input()

    if new_order is None:
        return

    product_type, stockName, stockPrice, stockQty, extra_value = new_order

    # Generate product ID
    if inventory.get_all_products():
        last_id = max(
            int(product.to_dict()["product_id"][1:])
            for product in inventory.get_all_products()
        )
        orderID = f"P{last_id + 1:03d}"
    else:
        orderID = "P001"

    supplier_id: str = input("Supplier ID: ").strip()
    supplier_name: str = input("Supplier Name: ").strip()
    supplier_email: str = input("Supplier Email: ").strip()

    if not supplier_id or not supplier_name or not supplier_email:
        print("All supplier details are required.")
        return

    supplier: Supplier = Supplier(supplier_id, supplier_name, supplier_email)

    # Create Product object
    match product_type:
        case "1":
            product_type = "physical"
        case "2":
            product_type = "digital"
        case _:
            raise ValueError("Invalid product type.")

    product: Product = ProductFactory.create(
        product_type, orderID, stockName,
        stockPrice, stockQty,
        supplier, extra_value
    )

    # Add product to inventory
    inventory.add_product(product)

    print("Product ID:", orderID)
    print("\nProduct added successfully!")

def handle_update_stock(inventory: Inventory) -> None:
    """Handle updating a product's stock quantity."""
    print("\nUpdate Stock")

    product_id: str = input("Enter Product ID: ").strip().upper()
    result = inventory.search_product(product_id)

    if result is None:
        print("Product not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {result.to_dict()['name']}")
    print(f"Current Stock: {result.to_dict()['stock']}\n")

    new_stock: str = input("New stock quantity: ").strip()

    # Validate new stock
    if not new_stock.isdigit():
        print("Invalid stock quantity.")
        return

    # Update stock
    try:
        result.update_stock(int(new_stock))
        print("\nStock updated successfully.")
    except ValueError as error:
        print(error)

def handle_search_product(inventory: Inventory) -> None:
    """Search for a product by its ID."""
    print("\nSearch Product")
    # Ask User for input
    product_id: str = input("Enter Product ID: ").strip().upper()
    result = inventory.search_product(product_id)

    if result is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("=======================================================")
    result.display_information()
    print("=======================================================")

def test_csv_loading() -> None:
    """Test loading products from a CSV file."""
    inventory: Inventory = Inventory()
    supplier: Supplier = Supplier(
        "S001",
        "Test Supplier",
        "test@example.com"
    )

    print("\nTesting valid CSV:")
    load_products("products.csv", inventory, supplier)

    print(f"Products loaded: {len(inventory.get_all_products())}")

    print("\nTesting missing CSV:")
    load_products("missing.csv", inventory, supplier)

def main() -> None:
    """Run the inventory management menu."""
    inventory: Inventory = Inventory()
    load_inventory(inventory)

    #initial prints
    print("================================")
    print("Inventory Management System")
    print("================================\n")

    # check if file exists and print appropriate message
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")

    #loop
    while True:
        # display menu
        display_menu()
        userInput: int | None = display_input()

        match userInput:
            case 1: # display all products
                handle_display_all(inventory)
            case 2: # add product
                handle_add_product(inventory)
            case 3: # update stock
                handle_update_stock(inventory)
            case 4: # search product
                handle_search_product(inventory)
            case 5: # save inventory
                print("\nSaving inventory...")
                save_inventory(inventory)
                print("Inventory saved successfully to inventory.json.")
            case 6: # exit
                print("\nSaving inventory before exit...")
                save_inventory(inventory)
                print("Inventory saved successfully.\n")

                print("Thank you for using the Inventory Management System. Goodbye!")
                print("Program terminated.\n")
                break
            case _:
                print("Invalid option. Please select a valid option from the menu.\n")

if __name__ == "__main__":
    test_csv_loading()