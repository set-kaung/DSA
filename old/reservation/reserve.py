def can_insert_reservation(scheduled_reservations, required_interval, new_reservation):
    # Add the new reservation to the list
    scheduled_reservations.append(new_reservation)

    # Perform an insertion sort to place the new reservation in the correct position
    for i in range(1, len(scheduled_reservations)):
        key = scheduled_reservations[i]
        j = i - 1
        while j >= 0 and scheduled_reservations[j] > key:
            scheduled_reservations[j + 1] = scheduled_reservations[j]
            j -= 1
        scheduled_reservations[j + 1] = key

    # Check if the new reservation violates the required time interval constraint
    for i in range(1, len(scheduled_reservations)):
        if scheduled_reservations[i] - scheduled_reservations[i - 1] < required_interval:
            return False

    return True

# Example usage:
scheduled_reservations = [17,21,26,29,36]  # Already scheduled reservations in minutes
required_interval = 3  # Required interval between reservations in minutes
new_reservation = int(input())  # New reservation to be inserted in minutes

if can_insert_reservation(scheduled_reservations, required_interval, new_reservation):
    print("The new reservation can be inserted.")
else:
    print("The new reservation cannot be inserted.")
