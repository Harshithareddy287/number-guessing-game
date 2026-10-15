import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # for testing use 42.
TIME_LIMIT = 60

print("Welcome to the Number Guessing Game!!!")

# ---------- Choose a level ----------
# Goal: keep asking until player picks a valid level, then set range and attempt limit.

while True:
    print("\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level = input("Enter your choice 1,2,3: ").strip()

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
        print("Invalid choice. Please select 1, 2, or 3.")


# ---------- Choose a mode ----------
# Goal: keep asking until player picks Classic or Time Challenge modes.
while True:
    print("\nChoose a game mode:")
    print("1. Classic Mode")
    print("2. Time Challenge Mode")

    mode = input("Enter your choice 1,2 : ").strip()

    if mode == "1":
        print("You selected Classic Mode")
        break
    elif mode == "2":
        print("You selected Time Challenge Mode")
        break
    else:
        print("Invalid choice. Please select 1 or 2.")


# ---------- Set up the round ----------
# Goal: pick secret number (use DEBUG_SECRET when it is not None) and start the clock.

if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

attempts = 0
won = False
timed_out = False

# Record when the round starts
start_time = time.time()

print("Guess a number between", low, "and", high)
print("You have", max_attempts, "attempts.")


# ---------- Guess loop ----------
# Goal: keep asking for guesses until player wins, runs out of attempts, or runs out of time.

while attempts < max_attempts:

    # Show remaining time before each guess in Time Challenge
    if mode == "2":
        elapsed_time = time.time() - start_time
        remaining_time = TIME_LIMIT - elapsed_time

        if remaining_time <= 0:
            timed_out = True
            break

        print("Time remaining:", round(remaining_time), "seconds")

    guess_input = input("Enter your guess: ").strip()

    # Checking whether the input is a valid whole number
    if not guess_input.isdecimal():
        print("Invalid input. Please enter a whole number.")
        continue

    guess = int(guess_input)

    # Checking whether number is within allowed range
    if guess < low or guess > high:
        print("Invalid input. Enter a number between", low, "and", high)
        continue

    # Count only valid guesses
    attempts += 1

    # Check time after a valid guess, before checking correctness
    if mode == "2":
        elapsed_time = time.time() - start_time

        if elapsed_time >= TIME_LIMIT:
            timed_out = True
            break

    # Compare the guess with the secret number
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
# Goal: show result that matches how round ended.

if won:
    print("Correct! You guessed the secret number!!!")
    print("Total attempts taken:", attempts)

elif timed_out:
    print("Time is up! You lost!")
    print("The secret number was:", secret_number)

else:
    print("Too many attempts, you lost!!!")
    print("The secret number was:", secret_number)

