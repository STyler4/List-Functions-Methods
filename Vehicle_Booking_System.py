# Define the function to get the number of seats needed
def get_num_seats():
    num_seats = int(input("Enter the number of seats needed (or -1 to stop): "))
    if num_seats == -1:
        print("Ending input mode.")
        return None
    else:
        return num_seats

# Define the function to display available vehicles
def display_available_vehicles(num_seats):
    print(f"Available vehicles with {num_seats} seats:")
    for vehicle in vehicles.values():
        if vehicle["num_seats"] >= num_seats:
            print(f"{vehicle['car_number']} - {vehicle['car_type']}")

# Define the function to get the vehicle number
def get_vehicle_number():
    vehicle_number = int(input("Enter the number of the vehicle to be booked (or -1 to stop): "))
    if vehicle_number == -1:
        print("Ending input mode.")
        return None
    else:
        return vehicle_number

# Define the function to book a vehicle
def book_vehicle(vehicle_number, name):
    vehicle = vehicles[vehicle_number - 1]
    bookings[vehicle_number] = name
    print(f"Vehicle {vehicle_number} ({vehicle['car_type']}) has been booked for {name}.")

# Define the list of vehicles
vehicles = {
    1: {"car_number": 1, "car_type": "Suzuki Van", "num_seats": 2},
    2: {"car_number": 2, "car_type": "Toyota Corolla", "num_seats": 4},
    3: {"car_number": 3, "car_type": "Honda CRV", "num_seats": 4},
    4: {"car_number": 4, "car_type": "Suzuki Swift", "num_seats": 4},
    5: {"car_number": 5, "car_type": "Mitsubishi Airtrek", "num_seats": 4},
    6: {"car_number": 6, "car_type": "Nissan DC Ute", "num_seats": 4},
    7: {"car_number": 7, "car_type": "Toyota Previa", "num_seats": 7},
    8: {"car_number": 8, "car_type": "Toyota Hi Ace", "num_seats": 12},
    9: {"car_number": 9, "car_type": "Toyota Hi Ace", "num_seats": 12},
}

# Define the dictionary of bookings
bookings = {}

# Main loop
while True:
    # Get the number of seats needed
    num_seats = get_num_seats()
    if num_seats is None:
        break

    # Display available vehicles
    display_available_vehicles(num_seats)

    # Get the vehicle number and book the vehicle
    while True:
        vehicle_number = get_vehicle_number()
        if vehicle_number is None:
            break
        if vehicle_number not in bookings:
            name = input("Enter your name: ")
            book_vehicle(vehicle_number, name)
            break
        else:
            print("Sorry, that vehicle is already booked.")

# Display the bookings at the end of the day
print("Bookings for the day:")
for vehicle_number, name in bookings.items():
    vehicle = vehicles[vehicle_number - 1]
    print(f"Vehicle {vehicle_number} ({vehicle['car_type']}) - {name}")

