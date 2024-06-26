import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
number_of_attempts = 0
guessed_correctly = False

print("Welcome to the Guess the Number Game!")
print("I have generated a random number between 1 and 100.")

# Main game loop
while not guessed_correctly:
    try:
        user_guess = int(input("Please enter your guess: "))
        number_of_attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
            print(f"It took you {number_of_attempts} attempts to guess the number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
