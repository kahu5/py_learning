import random
import time

# Create a set to keep track of displayed numbers
displayed_numbers = int()

# Generate random numbers until all numbers have been displayed three times
while displayed_numbers < 20 * 3:
    # Generate a random number between 1 and 20
    random_number = random.randint(1, 20)

    # Display the random number
    print(f"\t{random_number}")
    print("_\n")

    # Add the number to the set
    displayed_numbers += 1

    # Wait for 10 seconds
    time.sleep(10)

     # Check if we've displayed the numbers 60 times
    if displayed_numbers >= 20 * 3:
        break

print("All numbers have been displayed three times!")
