# external
import os
import json

# classes
from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# 1. get_valid_input(): Handles the prompt, handles input validation, and
# returns a valid integer or a "quit" signal.
def display_menu():
    print("\n------------- MENU -------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------------")

def display_input():
    displayInput = input("\nEnter option: ").strip()

    # check if -ve
    if displayInput.startswith("-") and displayInput[1:].isdigit() or not displayInput.isdigit():
        print("Please enter a valid menu option.")
        return None

    return int(displayInput)

def get_valid_input():
    # select product type
    print("Select Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Enter product type: ").strip()

    match product_type:
        case "1":
            print("Physical Product selected.")
            extra_value = input("Enter weight (kg): ").strip()
        case "2":
            print("Digital Product selected.")
            extra_value = input("Enter download size (MB): ").strip()
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
    stockName = input("Product Name: ").strip()
    
    #check empty
    if not stockName:
        print("Product name cannot be empty.")
        return None
    # check if name contains only letters and spaces
    elif not stockName.replace(" ", "").isalpha():
        print("Product name must contain only letters.")
        return None

    # Price input
    stockPrice = input("Product Price: $").strip()

    try:
        stockPrice = float(stockPrice)

        if stockPrice < 0:
            print("Product price cannot be negative.")
            return None

    except ValueError:
        print("Please enter a valid price.")
        return None

    # qty input    
    stockQty = input("Stock Quantity: ")

    # check if -ve
    if stockQty.startswith("-") and stockQty[1:].isdigit():
        print("Stock quantity cannot be negative.")
        return None
    #check if not digit
    elif not stockQty.isdigit():
        print("Please enter a valid number for stock quantity.")
        return None

    return product_type, stockName, stockPrice, int(stockQty), extra_value

#load_inv
def load_inventory(inventory: Inventory):
    # check if json file exists
    if not os.path.exists("inventory.json"):
        return
            
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            for item in data:
                product = Product(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )

                inventory.add_product(product)

    except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
        print("Unable to load inventory.")

# save_inv
def save_inventory(inventory: Inventory):
    data = []

    for product in inventory.get_all_products():
        # Append dictionary to data
        data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

# case functions
def handle_display_all(inventory: Inventory):
    print("\nCurrent Inventory")
    print("=======================================================")
    inventory.display_all()
    print("=======================================================")

def handle_add_product(inventory: Inventory):
    print("\nAdd New Product") # header
    print("==================") # separator line

    # Get user inputs
    new_order = get_valid_input()

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

    # Create Product object
    match product_type:
        case "1":
            product = PhysicalProduct(orderID, stockName, stockPrice, stockQty, extra_value)
        case "2":
            product = DigitalProduct(orderID, stockName, stockPrice, stockQty, extra_value)

    # Add product to inventory
    inventory.add_product(product)

    print("Product ID:", orderID)
    print("\nProduct added successfully!")

def handle_update_stock(inventory: Inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()
    result = inventory.search_product(product_id)

    if result is None:
        print("Product not found.")
        return

    print("\n Product Found:")
    print(f"Name: {result.to_dict()['name']}")
    print(f"Current Stock: {result.to_dict()['stock']}\n")

    new_stock = input("New stock quantity: ").strip()

    # Validate new stock
    if not new_stock.isdigit():
        print("Invalid stock quantity.")
        return

    # Update stock
    result.update_stock(int(new_stock))
    print("\nStock updated successfully.")

def handle_search_product(inventory: Inventory):
    print("\nSearch Product")
    # Ask User for input
    product_id = input("Enter Product ID: ").strip().upper()
    result = inventory.search_product(product_id)

    if result is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("=======================================================")
    result.display_information()
    print("=======================================================")

def main():
    inventory = Inventory()
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
        userInput = display_input()

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
    main()