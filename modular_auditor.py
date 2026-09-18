#init
inventory = 0
failed_entries = 0

# 1. get_valid_input(): Handles the prompt, handles input validation, and
# returns a valid integer or a "quit" signal.
def get_valid_input():
    #input
    stockQty = input("Enter the stock quantity (or type 'quit' to quit): ")
    
    #check if quit
    if stockQty.lower() == 'quit':
        generate_report(inventory, failed_entries)
        return "quit"
    
    #check -ve num
    if stockQty.startswith("-") and stockQty[1:].isdigit():
        print("Stock quantity cannot be negative.")
        return None
        
    #check non-digit
    elif not stockQty.isdigit():
        print("Please enter a valid number for stock quantity.")
        return None

    return int(stockQty)

# 2. process_delivery(current_total, new_value): Calculates the new total and
# returns it.
def process_delivery(current_total, new_value):
    return current_total + new_value

# 3. calculate_tax(amount): A new requirement! This function takes a delivery
# amount and returns the tax (10% of that specific delivery).
def calculate_tax(amount):
    tax = amount * 0.10
    return tax

# 4. generate_report(total_units, failed_attempts): A dedicated function to print
# the final summary.
def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

#loop
while True:
     #check if inv exceed 500 units, break if true
    if inventory >= 500:
        break

    stockQty = get_valid_input()  # Call the function to get valid input
    if stockQty is "quit":
        break  # Exit the loop if 'quit' was entered
    elif stockQty is None:
        failed_entries += 1
        continue  # Skip processing if input was invalid or 'quit' was entered
    
    inventory = process_delivery(inventory, stockQty)
    print("Tax: ", calculate_tax(stockQty))