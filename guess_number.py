import random

# Generate a random number between 1 and 250
rand_number = random.randint(1, 250)

# Initialize user's guessed number
user_number = 0

# Continue the loop until the user guesses the correct number
while user_number != rand_number:
    # Get user input for guessing the number
    user_number = int(input("Enter the number: "))
    
    # Check if the user's guess is higher than the random number
    if user_number > rand_number:
        print("You need to guess a lower number.")
    
    # Check if the user's guess is lower than the random number
    elif user_number < rand_number:
        print("You need to guess a higher number.")
    
    # Check if the user's guess is equal to the random number (correct guess)
    elif user_number == rand_number:
        print("Congratulations! You guessed the number.")
    
    # Handle invalid input (not necessary in this case since input is cast to int)
    else:
        print("Invalid input")
