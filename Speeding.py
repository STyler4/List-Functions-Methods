WARRANT_NAMES = ["James Wilson", "Helga Norman", "Zachary Conroy"]
FINE_RATES = {10: 30, 15: 80, 20: 120, 25: 170, 30: 230, 35: 300, 40: 400, 45: 510}

# Initialize variables to keep track of data for summary at the end of the day
total_fines = 0
ticket_count = 0
ticket_data = []

while True:
    name = input("Enter name of speeder: ")
    if not name:
        # Stop input mode when user enters an empty name
        break

    # Check if the person is wanted for arrest
    if name in WARRANT_NAMES:
        print(f"{name.upper()} - WARRANT TO ARREST")

    # Ask for amount over speed limit and calculate fine
    amount_over_limit = int(input("Enter the amount over speed limit: "))
    for limit, rate in sorted(FINE_RATES.items(), reverse=True):
        if amount_over_limit >= limit:
            fine = rate
            break
    else:
        fine = 630
    print(f"{name} to be fined ${fine}")

    # Add data for summary at the end of the day
    ticket_count += 1
    total_fines += fine
    ticket_data.append({"name": name, "amount_over_limit": amount_over_limit})

# Print summary at the end of the day
print(f"Total fines: {ticket_count}")
for i, ticket in enumerate(ticket_data):
    print(f"{i+1}) Name: {ticket['name']}   Amount Over Limit: {ticket['amount_over_limit']}")
print(f"Total amount of fines: ${total_fines}")
