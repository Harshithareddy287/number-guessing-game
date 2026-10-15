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
- [Project Notes](#project-notes)

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

The game was manually tested in the terminal in both modes. For predictable results, the secret number was temporarily set to `42`.

| # | Test | Expected result | Outcome |
|--:|:-----|:----------------|:--------|
| 1 | Guess below the secret (`32`) | Show “Too low!” and use one attempt | Passed |
| 2 | Guess above the secret (`45`) | Show “Too high!” and use one attempt | Passed |
| 3 | Guess correctly after five incorrect valid guesses | Show success and report 6 total attempts | Passed |
| 4 | Enter letters (`fghj`) | Reject input without using an attempt | Passed |
| 5 | Submit blank input | Reject input without using an attempt | Passed |
| 6 | Enter a number below the range (`0` in Easy) | Reject input without using an attempt | Passed |
| 7 | Enter a number above the range (`90` in Easy) | Reject input without using an attempt | Passed |
| 8 | Select Easy | Set range to 1–50 and allow 10 attempts | Passed |
| 9 | Select Medium | Set range to 1–100 and allow 8 attempts | Passed |
| 10 | Select Hard in Time Challenge | Set range to 1–500 and allow 10 attempts | Passed |
| 11 | Use all attempts in Medium Time Challenge | End after 8 valid guesses and reveal the secret | Passed |
| 12 | Guess after the Time Challenge expires | End the game and reveal the secret | Passed |
| 13 | Make multiple guesses in Time Challenge | Display the decreasing remaining time | Passed |
| 14 | Enter a decimal (`5.00`) | Reject input without using an attempt | Passed |
| 15 | Select Classic Mode | Play without a countdown | Passed |

**Test summary:** All 15 documented test cases passed. Testing covered input validation, attempt counting, difficulty settings, countdown behavior, winning, timeout handling, and revealing the secret number.

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

## Project Notes

This project demonstrates Python fundamentals, including variables, conditionals, loops, input validation, random number generation, and time-based game logic. It also uses a Git workflow with feature branches, commits, pull requests, and manual testing.
