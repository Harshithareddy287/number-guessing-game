
import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # Set to 42 for testing; restore None before committing.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
# Feature 2: Difficulty levels will be added later.

low = 1
high = 100


# ---------- Choose a mode ----------git 
# Goal: keep asking until the player picks Classic or Time Challenge.
# Feature 3: Mode selection will be added later.


# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

attempts = 0

print("Guess a number between", low, "and", high)


# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

while True:
    guess_input = input("Enter your guess: ").strip()

    # Check whether the input is a valid whole number
    if not guess_input.isdecimal():
        print("Invalid input. Please enter a whole number.")
        continue

    guess = int(guess_input)

    

    # Count only valid guesses
    attempts += 1

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        break


# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

print("Correct! You guessed the secret number!")
print("Total attempts:", attempts)

