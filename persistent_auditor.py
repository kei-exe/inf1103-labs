import os

#init
failed_entries = 0
transaction_history = {}  # List to store transaction history   

# 1. get_valid_input(): Handles the prompt, handles input validation, and
# returns a valid integer or a "quit" signal.
def display_menu():
    print("------------- MENU -------------")
    print("1. Display All products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")

#load_inv
def load_inventory():
    transaction_history = {}

    if not os.path.exists("inventory.txt"):
        return transaction_history

    with open("inventory.txt", "r") as file:
        for line in file:
            data = line.strip().split("| ")

            orderID = int(data[0])
            stockName = data[1]
            stockPrice = float(data[2])
            stockQty = int(data[3])

            transaction_history[orderID] = [
                stockName,
                stockPrice,
                stockQty]

    return transaction_history

# save_inv
def save_inventory(transaction_history):
    with open("inventory.txt", "w") as file:

        for product_id, product in transaction_history.items():
            stockName = product[0]
            stockPrice = product[1]
            stockQty = product[2]

            file.write(
                f"{product_id}, {stockName}, {stockPrice}, {stockQty}\n") # saves the final inventory total

        print("\nSaved to inventory.txt")

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

# 1
def display_all():
    if not transaction_history:
        print("Inventory is empty.")
        return

    for product_id, product in transaction_history.items():
        print("Product ID:", product_id)
        print("Name:", product[0])
        print("Stock:", product[1])

# 2
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

# 3
def update_stock():
    with open("inventory.txt", "w") as file:
        product_id = int(input("Enter Product ID: ")).strip()
           
    # Validate Product ID
    if not product_id.isdigit():
        print("Invalid Product ID.")
        return

    product_id = int(product_id)

    # Check if product exists
    if product_id in transaction_history:
        print("Product Found")
        print("====================")
        print("Product ID:", product_id)
        print("Name:", transaction_history[product_id][0])
        print("Current Stock:", transaction_history[product_id][1])
        print("====================")

        new_stock = input("\nNew stock quantity: ").strip()

        # Validate new stock
        if not new_stock.isdigit():
            print("Invalid stock quantity.")
            return

        # Update stock
        transaction_history[product_id][2] = int(new_stock)

        print("\nStock updated successfully.")
    else:
        print("Product not found.")
 
# 4
def search_product():
    product_id = int(input("Enter Product ID: "))

    if product_id in transaction_history:
        print("Product Found")
        print("====================")
        print("Product ID: ", product_id)
        print("Name: ", transaction_history[product_id][0])
        print("Price: $", transaction_history[product_id][1])
        print("Stock: ", transaction_history[product_id][2])
        print("====================")
        print(transaction_history[product_id])

    else:
        print("Product not found.")

# main
transaction_history = load_inventory()

#initial prints
print("================================")
print("Inventory Management System")
print("================================\n")

# check if file exists and print appropriate message
if os.path.exists("inventory.txt"):
    print("inventory.txt found")
    print("inventory loaded successfully\n")
else:
    print("inventory.txt not found")
    print("creating new inventory file\n")

# display menu
display_menu()

#loop
while True:
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
            new_order = get_valid_input()
            if new_order is None:
                continue  # Invalid input, prompt again
            else:
                stockName, stockPrice, stockQty = new_order

                orderID = 000 + len(transaction_history)
                transaction_history[orderID] = [
                    stockName,
                    stockPrice,
                    stockQty]

                print("\nProduct added successfully!")
        case 3: # update stock
            print("Update Stock")
            update_stock()
        case 4: # search product
            print("Search Product")
            search_product()
        case 5: # save inventory
            save_inventory(transaction_history)
            print("Saving inventory...")
            print("Inventory saved successfully to inventory.txt.\n")

        case 6: # exit
            save_inventory(transaction_history)
            print("Saving inventory before exit...")
            print("Inventory saved successfully.\n")

            print("Thank you for using the Inventory Management System. Goodbye!")
            print("Program terminated.")
            break

        case _:
            print("Invalid option. Please select a valid option from the menu.\n")