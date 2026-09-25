import os

# get_valid_input(): Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal.
def get_valid_input():
# ask for input
    global stockName, stockQty
    stockName = input("Enter the stock name (or type 'quit' to quit): ")
    stockQty = input("Enter the stock quantity: ") 
# check if quit
    if stockName == "quit":
# save the final total and the transaction history list to inventory.txt
        save_inventory(stockName, stockQty)
        return "quit"
# check valid stock name
    if not stockName.strip():
        print("Stock name cannot be empty.")
        return None
    elif not stockName.isalpha():
        print("Stock name must contain only letters.")
        return None
    
# check if negative number
    if stockQty.startswith("-") and stockQty[1:].isdigit():
        print("Stock quantity cannot be negative.")
        return None
# check if non-digit
    elif not stockQty.isdigit():
        print("Please enter a valid number for stock quantity.")
        return None
    
    return str(stockName), int(stockQty)

# save_inventory(total_units, transaction_history): Saves the current total and the transaction history list to the inventory file.
def save_inventory(stockName, stockQty):
    with open("inventory.txt", "a") as file:
        file.write(f"{stockName}, {stockQty}\n")
        for entry in transaction_history:
            file.write(f"{entry}\n")
    print("Inventory saved successfully.")

# load_inventory(): Reads the inventory file and returns the current total and the transaction history list.
def load_inventory():
    global transaction_history
    transaction_history = []
    
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            if lines:
                transaction_history = [line.strip() for line in lines[1:]]
                print("Current Orders:")
                for entry in transaction_history:
                    print(f"{len(transaction_history)}, {entry}")
    else:
        print("No previous history found. Starting with an empty inventory.")

# calculate_tax(amount): A new requirement! This function takes a delivery amount and returns the tax (10% of that specific delivery).

# generate_report(total_units, failed_attempts): A dedicated function to print the final summary.

# main
# initial print (current orders in list)
load_inventory() 
# loop
#while True:
# Persistence: At the start of the program, read the information previously saved in the inventory file. If the inventory file does not exist, 
# start with an empty inventory and continue running without producing an error.

# check if inventory exceeds 500 units, break if true
# call valid input function
# exit if 'quit' was entered
# increment failed entries if input was invalid or 'quit' was entered
# add to inventory if input was valid