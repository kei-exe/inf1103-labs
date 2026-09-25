import os

# get_valid_input(): Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal.
def get_valid_input():
    global stockName, stockQty

    stockName = input("Enter Product Name (or type 'quit' to quit): ").strip()

    # check if quit
    if stockName == "quit":
        return "quit"

    # check valid stock name
    if not stockName:
        print("Stock name cannot be empty.")
        return None
    elif not stockName.replace(" ", "").isalpha():
        print("Stock name must contain only letters.")
        return None

    # ONLY ask quantity after name is valid
    stockQty = input("Enter Quantity: ")

    # check if negative number
    if stockQty.startswith("-") and stockQty[1:].isdigit():
        print("Stock quantity cannot be negative.")
        return None
    elif not stockQty.isdigit():
        print("Please enter a valid number for stock quantity.")
        return None

    return stockName, int(stockQty)

# save_inventory(total_units, transaction_history): Saves the current total and the transaction history list to the inventory file.
def save_inventory(stockName, stockQty):
    with open("inventory.txt", "a") as file:
        file.write(f"{stockName}, {stockQty}\n")
        for entry in transaction_history:
            file.write(f"{entry}\n")
    print(f"New Order Added: \n{len(transaction_history) + 1} {stockName}, {stockQty}")
    print("Order successfully saved to inventory.txt.")

# load_inventory(): Reads the inventory file and returns the current total and the transaction history list.
def load_inventory():
    global transaction_history
    transaction_history = []
    
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            if lines:
                transaction_history = [line.strip() for line in lines]
                print("Current Orders:")
                for entry in transaction_history:
                    print(entry)
    else:
        print("No previous history found. Starting with an empty inventory.")

# calculate_tax(amount): A new requirement! This function takes a delivery amount and returns the tax (10% of that specific delivery).

# generate_report(total_units, failed_attempts): A dedicated function to print the final summary.

# main
# Persistence: At the start of the program, read the information previously saved in the inventory file. If the inventory file does not exist, 
# start with an empty inventory and continue running without producing an error. 
load_inventory() 
# loop
while True:
# check if inventory exceeds 500 units, break if true
# call valid input function
    stockName, stockQty = get_valid_input()  # Call the function to get valid input
# exit if 'quit' was entered
    if stockName == "quit":
        save_inventory(stockName, stockQty)  # Save the current inventory before quitting
        break
# increment failed entries if input was invalid or 'quit' was entered
    elif stockName is None or stockQty is None:
        failed_entries += 1
        continue  # Skip processing if input was invalid or 'quit' was entered
# add to inventory if input was valid
    inventory = save_inventory(stockName, stockQty)