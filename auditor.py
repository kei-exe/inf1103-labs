#init
inventory = 0
noFE = 0

#loop
while True:
     #check if inv exceed 500 units, break if true
    if inventory >= 500:
        break

    #input
    stockQty = input("Enter the stock quantity (or type 'quit' to quit): ")

    #check if quit
    if stockQty.lower() == 'quit':
        print("Total Units Processed: ", inventory)
        print("Number of Failed/Rejected Entries: ", noFE)
        break

    #check -ve num
    if stockQty.startswith("-") and stockQty[1:].isdigit():
        print("Stock quantity cannot be negative.")
        noFE += 1
        continue
    #check non-digit
    elif not stockQty.isdigit():
        print("Please enter a valid number for stock quantity.")
        noFE += 1
        continue
    #else add to inv
    else:
        stockQty = int(stockQty)
        inventory += stockQty
        print(f"Current inventory: {inventory}")