# Number Guessing Game

A terminal-based Python game where you try to guess a randomly generated number. Choose a difficulty, then play at your own pace in **Classic Mode** or race the clock in **Time Challenge Mode**.

## Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Test Plan](#test-plan)
- [Git Workflow](#git-workflow)
- [Configuration](#configuration)

## Features

### Classic Mode

- Generates a secret number within the range for your selected difficulty.
- Gives a **Too low!** or **Too high!** hint after each valid guess.
- Tracks valid guesses and reports your total attempts if you win.
- Validates input and reveals the secret number if you run out of attempts.

### Difficulty Levels

| Level | Number range | Attempts |
|:------|:-------------|---------:|
| Easy | 1–50 | 10 |
| Medium | 1–100 | 8 |
| Hard | 1–500 | 10 |

Choose a level from the menu. If your selection is invalid, the game prompts you to try again.

### Time Challenge Mode

- Gives you 60 seconds to guess the secret number.
- Shows the remaining time before each guess.
- Ends the round when time or attempts run out.
- Reveals the secret number if you lose.

## Requirements

- Python 3
- No third-party packages

## Getting Started

Clone the repository and start the game:

```bash
git clone https://github.com/Harshithareddy287/number-guessing-game.git
cd number-guessing-game
python3 guess.py
```

## How to Play

1. Choose a difficulty level: Easy, Medium, or Hard.
2. Choose Classic Mode or Time Challenge Mode.
3. Enter a whole number within the displayed range.
4. Use the hints to guide your next guess.
5. Keep guessing until you win, run out of attempts, or run out of time.

Invalid input and guesses outside the selected range do not use an attempt.

## Test Plan

The game was manually tested in the terminal using `DEBUG_SECRET = 42` to verify the expected results.

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | Guess below the secret | Guessed 32 with secret 42 | Display "Too low!" | Displayed "Too low!" | Yes |
| 2 | Guess above the secret | Guessed 45 with secret 42 | Display "Too high!" | Displayed "Too high!" | Yes |
| 3 | Correct guess | Guessed 42 after five valid incorrect guesses | Display success and 6 total attempts | Displayed success and total attempts of 6 | Yes |
| 4 | Letters as input | Entered `fghj` | Reject input without using an attempt | Invalid input message; attempts unchanged | Yes |
| 5 | Blank input | Pressed Enter without entering a number | Reject input without using an attempt | Invalid input message; attempts unchanged | Yes |
| 6 | Below-range number | Entered 0 in Easy Mode | Reject number outside range | Range error; attempts unchanged | Yes |
| 7 | Above-range number | Entered 90 in Easy Mode | Reject number outside range | Range error; attempts unchanged | Yes |
| 8 | Decimal input | Entered `5.00` | Reject invalid input | Invalid input message; attempts unchanged | Yes |
| 9 | Easy difficulty | Selected Easy and Classic Mode | Range 1–50, 10 attempts | Displayed range 1–50 and 10 attempts | Yes |
| 10 | Medium difficulty | Selected Medium and Time Challenge | Range 1–100, 8 attempts | Displayed range 1–100 and 8 attempts | Yes |
| 11 | Hard difficulty | Selected Hard and Time Challenge | Range 1–500, 10 attempts | Displayed range 1–500 and 10 attempts | Yes |
| 12 | Medium attempt limit | Entered 8 incorrect guesses | End game and reveal secret | Displayed loss message and revealed 42 | Yes |
| 13 | Hard attempt limit | Entered 10 incorrect guesses | End game and reveal secret | Displayed loss message and revealed 42 | Yes |
| 14 | Countdown | Played Medium Time Challenge | Display remaining time before guesses | Countdown decreased from 60 seconds | Yes |
| 15 | Timeout | Entered 42 after the time limit | Reject late guess and reveal secret | Displayed "Time is up!" and revealed 42 | Yes |
| 16 | Classic Mode | Selected Easy and Classic Mode | Run without a countdown | Game ran without a timer | Yes |

### Test Summary

All 16 documented manual test cases passed. The tests covered input validation, difficulty levels, attempt counting, countdown behavior, timeout handling, and successful guesses.

During testing, `DEBUG_SECRET` was set to `42`. For normal gameplay, it should be set to `None`.

## Git Workflow

The project was developed using three feature branches:

- `feature/classic-mode`
- `feature/difficulty-levels`
- `feature/time-challenge`

Each feature was committed separately and merged into `main` through a GitHub pull request.

## Configuration

For normal gameplay, `guess.py` uses:

```python
DEBUG_SECRET = None
TIME_LIMIT = 60
```

Set `DEBUG_SECRET = 42` to use a predictable secret number during testing.

