import os
import json

#init
failed_entries = 0
inventory = []

# 1. get_valid_input(): Handles the prompt, handles input validation, and
# returns a valid integer or a "quit" signal.
def display_menu():
    print("\n\n------------- MENU -------------")
    print("1. Display All products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")

#load_inv
def load_inventory():
    if not os.path.exists("inventory.json"):
        return []

    try:
        with open("inventory.json", "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Unable to load inventory.")
        return []

# save_inv
def save_inventory(transaction_history):
    with open("inventory.json", "w") as file:
        json.dump(transaction_history, file, indent=4)

def display_input():
    displayInput = input("\nEnter option: ").strip()

    # check if -ve
    if displayInput.startswith("-") and displayInput[1:].isdigit():
        print("Stock quantity cannot be negative.")
        return None
        #check if not digit
    elif not displayInput.isdigit():
        print("Please enter a valid number for stock quantity.")
        return None

    return int(displayInput)


def get_valid_input():
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

    return stockName, stockPrice, int(stockQty)

# 1
def display_all():
    if not inventory:
        print("Inventory is empty.")
        return

    for product in inventory:
        print(
            f"ID: {product['product_id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

# 2
def add_product():
    new_order = get_valid_input()

    if new_order is None:
        return

    stockName, stockPrice, stockQty = new_order

    if inventory:
        last_id = max(int(product["product_id"][1:]) for product in inventory)
        orderID = f"P{last_id + 1:03d}"
    else:
        orderID = "P001"

    inventory.append({
    "product_id": orderID,
    "name": stockName,
    "price": stockPrice,
    "stock": stockQty
    })

    print("Product ID:", orderID)
    print("Product added successfully!")

# 3
def update_stock():
    product_id = input("Enter Product ID: ").strip().upper()

    if not product_id.startswith("P") or not product_id[1:].isdigit():
        print("Invalid Product ID.")
        return

    # Check if product exists
    product = next((item for item in inventory if item["product_id"] == product_id), None)
    if product:
        print("\nProduct Found")
        print("====================")
        print("Product ID:", product["product_id"])
        print("Name:", product["name"])
        print("Current Stock:", product["stock"])
        print("====================")

        new_stock = input("New stock quantity: ").strip()

        # Validate new stock
        if not new_stock.isdigit():
            print("Invalid stock quantity.")
            return

        # Update stock
        product["stock"] = int(new_stock)

        print("\nStock updated successfully.")

    else:
        print("Product not found.")
 
# 4
def search_product():
    product_id = input("Enter Product ID: ").strip().upper()

    if not product_id.startswith("P") or not product_id[1:].isdigit():
        print("Invalid Product ID.")
        return

    product = next((item for item in inventory if item["product_id"] == product_id), None)
    if product:
        print("\nProduct Found")
        print("====================")
        print("Product ID: ", product["product_id"])
        print("Name: ", product["name"])
        print("Price: $", f"{product["price"]:.2f}")
        print("Stock: ", product["stock"])
        print("====================")

    else:
        print("\nProduct not found.")

# main
inventory = load_inventory()

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

    # quit
    match userInput:
        case 1: # display all products
            print("Current Inventory")
            print("====================")
            display_all()
            print("====================")
        case 2: # add product
            print("\nAdd New Product") # header
            add_product()
        case 3: # update stock
            print("Update Stock")
            update_stock()
        case 4: # search product
            print("Search Product")
            search_product()
        case 5: # save inventory
            save_inventory(inventory)
            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json.")

        case 6: # exit
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.\n")

            print("Thank you for using the Inventory Management System. Goodbye!")
            print("Program terminated.")
            break

        case _:
            print("Invalid option. Please select a valid option from the menu.\n")