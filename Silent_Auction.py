# Store the bidding item
item = input("What is the auction for? ")

# Store the reserve price
reserve_price = float(input("What is the reserve price? "))

# Start the auction
print("The auction for the", item, "has started!")

# Initialize highest bid to 0
highest_bid = 0.0

# Repeat until user inputs -1
while True:
    # Show the highest bid so far
    print("Highest bid so far is $%.2f" % highest_bid)

    # Ask for a bid
    bid = float(input("What is your bid? "))

    # Check if the bid is -1
    if bid == -1:
        break

    # Check if the bid is higher than the highest bid
    if bid > highest_bid:
        highest_bid = bid
    else:
        print("Please enter a higher bid")

# Check if the highest bid beat the reserve price
if highest_bid >= reserve_price:
    print("The auction for the", item, "finished with a bid of $%.2f" % highest_bid)
else:
    print("The", item, "did not sell as the reserve price was not met.")

