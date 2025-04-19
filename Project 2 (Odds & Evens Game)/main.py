
# Game name Odds and Evens

import random

def odds_and_evens():
    print("Welcome to the Odds and Evens Game!")
    print("Choose one between these two options: [O = Odds] [E = Evens]")

    # User chooses Odds or Evens
    youstr = input("Enter your choice: ").strip().lower()
    youdict = {"o": "Odds", "e": "Evens"}

    # Validate user input
    choice = youdict.get(youstr)
    if choice is None:
        print("Invalid choice! Please enter 'O' for Odds or 'E' for Evens.")
        return

    print(f"You chose: {choice}")

    # User choose a number between [1-5]
    try:
        user = int(input("Input a number between 1 to 5: "))
        if user < 1 or user > 5:
            print("Invalid input! Choose a number between 1 and 5.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Computer chooses a random number between [1-5]
    computer = random.randint(1, 5)
    print(f"Computer chose: {computer}")

    # Calculate sum
    total = user + computer
    print(f"Total: {user} + {computer} = {total}")

    # Determine the winner
    winner = "Evens" if total % 2 == 0 else "Odds"
    print(f"It's a {winner} number!")

    if choice == winner:
        print("Congratulations! You win! 🎉")
    else:
        print("Sorry, Computer wins this time!😔\nBetter luck next time.")

odds_and_evens()
