import random

# generate random numbers between 1 to 10
secret_number = random.randint(1, 10)

# required variables
attempts = 0
max_attempts = 3
guessed_correctly = False

print("Welcome to the Guessing Game!")
print("Try to guess the secret number between 1 and 10.")

while attempts < max_attempts:
    # Get user input for the guess
    guess = int(input("Enter your guess: "))

    # Check the guess
    if guess == secret_number:
print("Congratulations! You guessed the correct number.")
        guessed_correctly = True
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    # Increment attempts
    attempts += 1

# if attempts are over
if not guessed_correctly:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
