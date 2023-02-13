def calculate_cost(time):
  base_cost = 10
  extra_cost = 2 * time
  return base_cost + extra_cost


print("Welcome to the Taxi tracking system!")
driver_name = input("What is the driver's name? ")

total_time = 0
total_income = 0
trip_count = 0

while True:
  new_trip = input("Would you like to start a new trip? (yes/no) ")
  if new_trip == "no":
    break
  elif new_trip == "yes":
    trip_time = int(input("How long was the trip in minutes? "))
    trip_cost = calculate_cost(trip_time)
    print("The cost for this trip is: $" + str(trip_cost))
    total_time += trip_time
    total_income += trip_cost
    trip_count += 1
  else:
    print("Invalid input. Please enter 'yes' or 'no'.")

average_time = total_time / trip_count
average_income = total_income / trip_count

print("Driver's Name: " + driver_name)
print("Total Time of all trips: " + str(total_time) + " minutes")
print("Average Time of all trips: " + str(average_time) + " minutes")
print("Total Income for the day: $" + str(total_income))
print("Average Cost of all trips: $" + str(average_income))
