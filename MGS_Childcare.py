"""Creating a program that will be used by a child day-care centre.
It will keep track of children throughout the day."""

# Drop off function
def dropOff():
    child_name = input("Enter the name of the child: ")
    child_list.append(child_name)
    print("Child " + child_name + " added to the roll successfully.")

# Pick up function
def pickUp():
    child_name = input("Enter the name of the child: ")
    if child_name in child_list:
        child_list.remove(child_name)
        print("Child " + child_name + " picked up successfully.")
    else:
        print("Error: Child " + child_name + " not found in the roll.")

# Calculate cost function
def calcCost():
    hours = int(input("Enter the number of hours to charge: "))
    cost = hours * 12 * len(child_list)
    print("The total cost for " + str(hours) + " hours is $" + str(cost))

# Print roll function
def printRoll():
    if len(child_list) == 0:
        print("No children in the roll.")
    else:
        print("Children in the roll:")
        for child in child_list:
            print(child)

# Initialize an empty list to store the names of children
child_list = []

# Main function
choice = 0
while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropOff()

    elif choice == 2:
        pickUp()

    elif choice == 3:
        calcCost()

    elif choice == 4:
        printRoll()

    else:
        print("Goodbye")

