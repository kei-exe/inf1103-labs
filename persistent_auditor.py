import os

#init
failed_entries = 0
transaction_history = []  # List to store transaction history   

# 1. get_valid_input(): Handles the prompt, handles input validation, and
# returns a valid integer or a "quit" signal.
def get_valid_input():
    # name input
    stockName = input("Enter product name: (or type 'quit' to quit) ").strip()
    
    #check if quit
    if stockName.lower() == "quit":
        return "quit"
    
    #check empty
    if not stockName:
        print("Product name cannot be empty.")
        return None
    # check if name contains only letters and spaces
    elif not stockName.replace(" ", "").isalpha():
        print("Product name must contain only letters.")
        return None

    # qty input    
    stockQty = input("Enter Quantity: ")

    # check if -ve
    if stockQty.startswith("-") and stockQty[1:].isdigit():
        print("Stock quantity cannot be negative.")
        return None
    #check if not digit
    elif not stockQty.isdigit():
        print("Please enter a valid number for stock quantity.")
        return None

    return stockName, int(stockQty)

#load_inv
def load_inventory():
    if not os.path.exists("inventory.txt"):
        return []

    with open("inventory.txt", "r") as file:
        transaction_history = []

        for line in file:
            transaction_history.append(line.strip())

    return transaction_history

# save_inv
def save_inventory(transaction_history):
    with open("inventory.txt", "w") as file:
        for order in transaction_history:  # go through list and saves every transaction
            file.write(order + "\n") # saves the final inventory total

        print("\nSaved to inventory.txt")

# main
transaction_history = load_inventory()

#initial prints
print("Current orders:\n")
for order in transaction_history:
    print(order)
print()

#loop
while True:
    userInput = get_valid_input()

    if userInput == "quit":
        save_inventory(transaction_history)
        break

    if userInput is None:
        failed_entries += 1
        continue

    stockName, stockQty = userInput
    orderID = 1001 + len(transaction_history)

    newOrder = f"{orderID}, {stockName}, {stockQty}"
    transaction_history.append(newOrder)

    print("\nNew Order Added:")
    print(newOrder + "\n")