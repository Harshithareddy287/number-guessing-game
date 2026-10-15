import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # for testing use 42.
TIME_LIMIT = 60

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

while True:
    print("\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level = input("Enter your choice 1 2 3 : ").strip()

    if level == "1":
        low = 1
        high = 50
        max_attempts = 10
        break

    elif level == "2":
        low = 1
        high = 100
        max_attempts = 8
        break

    elif level == "3":
        low = 1
        high = 500
        max_attempts = 10
        break

    else:
        print("Invalid choice.. Please select 1, 2, or 3.")


# ---------- Choose a mode ----------
# Goal: keep asking until player picks {Classic or Time Challenge}.
# Feature 3 added later steps.


# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

attempts = 0
won = False

print("Guess number between", low, "and", high)
print("You have", max_attempts, "attempts.")

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, check if runs out of attempts
while attempts < max_attempts:
    guess_input = input("Enter your guess : ").strip()

    # Checking whether input is a valid whole number
    if not guess_input.isdecimal():
        print("Invalid input.. Please enter a whole number.")
        continue
    guess = int(guess_input)
    # Checking whether the number is within the allowed range
    if guess < low or guess > high:
        print("Invalid input. Enter a number between", low, "and", high)
        continue

    # Count only valid guesses
    attempts += 1

    # Compare guess with the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        won = True
        print("Correct!")

    # Show remaining attempts
    print("Attempts left:", max_attempts - attempts)

    if won:
        break


# ---------- End of round ----------
# showing result that matches how round ended.

if won:
    print("Correct! You guessed the secret number!")
    print("Total attempts taken:", attempts)
else:
    print("Too many attempts, you lost!!!")
    print("The secret number was:", secret_number)
