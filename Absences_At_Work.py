def main():
    absences = []
    total_absences = 0
    not_absent = []

    # Get input from the user
    name = input("Enter the employee's name (or '$' to quit): ").strip()
    while name != '$':
        absence = int(input("Enter the number of days absent: "))
        absences.append((name, absence))
        total_absences += absence

        if absence == 0:
            not_absent.append(name)

        name = input("Enter the employee's name (or '$' to quit): ").strip()

    # Calculate the average number of days absent
    average_absence = total_absences / len(absences)

    # Get the employee with the most days absent
    most_absent = max(absences, key=lambda x: x[1])

    # Get a list of employees who were absent more than the average
    above_average = [x for x in absences if x[1] > average_absence]

    # Print the results
    print("Average number of days staff were absent: {:.2f}".format(average_absence))
    print("Person with most days absent: {} with {} days".format(most_absent[0], most_absent[1]))
    print("List of people not absent at all:")
    for name in sorted(not_absent):
        print("\t" + name)
    print("List of people absent above average:")
    for name, days in sorted(above_average, key=lambda x: x[1], reverse=True):
        print("\t{} {}".format(name, days))

if __name__ == '__main__':
    main()
